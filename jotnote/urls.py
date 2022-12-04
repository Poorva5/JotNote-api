from django.contrib import admin
from django.urls import path, include
from notes.views import NotesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/note", NotesView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
