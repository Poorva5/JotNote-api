from django.contrib import admin
from django.urls import path, include
from notes.views import NotesView
from rest_framework.routers import DefaultRouter
from notes.views import MyNotes, CreateNote, UpdatePinnedNote

router = DefaultRouter()
router.register("api/note", NotesView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('my-notes/', MyNotes.as_view()),
    path('create/my-notes/', CreateNote.as_view()),
    path('pin-note/<int:pk>/', UpdatePinnedNote.as_view())
]