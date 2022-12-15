from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NotesView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class MyNotes(APIView):

    def get(self, request, *args, **kwargs):
        notes_list = Note.objects.filter(users=request.user)
        pinned_notes_list = notes_list.filter(pin=True)
        unpinned_notes_list = notes_list.filter(pin=False)
        pinned_notes_serializer = NoteSerializer(pinned_notes_list, many=True)
        unpinned_notes_serializer = NoteSerializer(unpinned_notes_list, many=True)
        return Response(
            {
                'pinned_notes_list': pinned_notes_serializer.data,
                'unpinned_notes_list': unpinned_notes_serializer.data
            }
        , status=status.HTTP_200_OK)
class CreateNote(APIView):
    
    def post(self, request):
        try: 
            note_serialzier = NoteSerializer(data=request.data)
            print(request.data, 'data')
            note_serialzier.is_valid(raise_exception=True)
            note_instance = note_serialzier.save(users=request.user)

            return Response(
                NoteSerializer(note_instance).data, status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                note_serialzier.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
class UpdatePinnedNote(APIView):

    def put(self, request, pk):
        note_instance = Note.objects.filter(id=pk).first()
        data = {"pin": not note_instance.pin}
        note_serializer = NoteSerializer(note_instance, data=data, partial=True)
        note_serializer.is_valid(raise_exception=True)
        note_serializer.save()
        return Response(note_serializer.data, status=status.HTTP_200_OK)

