from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'note'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('notes/', NoteListAPIView.as_view(), name='notes-list'),
    path('notes/<int:id>/', NoteDetaiAPIView.as_view(), name='note-detail'),
    # path('auth/logout/', MyLogoutView.as_view()),
    path('', include(router.urls)),
    path('users/<int:id>/notes/', UserNoteListAPIView.as_view(), name='user-note-list')
]