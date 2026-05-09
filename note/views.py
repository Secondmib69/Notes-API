from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from note.permissions import IsNoteUserOrStaffReadOnly, IsSuperUserOrStaffReadOnly
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .pagination import CustomPagination, CursorPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from dj_rest_auth.views import LogoutView
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets
from .serializers import User




# class CustomFilterBackend(DjangoFilterBackend):
     
#      def get_filterset_class(self, view, queryset = None):
#          return view.StaffOnlyFilter if (view.request.user and view.request.user.is_staff) else None




# Create your views here.


class NoteListAPIView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'tags__name', 'user__username']
    ordering_fields = ['created', 'updated']
    ordering = ['-created']
    pagination_class = CursorPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTCookieAuthentication]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        qs = Note.objects.all()
        if self.request.user and self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)
    

    # class StaffOnlyFilter(FilterSet):
    #     class Meta:
    #         model = Note
    #         fields = ['user']
    

class NoteDetaiAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsNoteUserOrStaffReadOnly]
    # authentication_classes = []



# @extend_schema(
#     parameters=[
#         OpenApiParameter(
#             name="X-CSRFToken",
#             type=str,
#             location=OpenApiParameter.HEADER,
#             required=True,
#             description="CSRF token (same as csrftoken cookie)",
#         ),
#     ]
# )
# class MyLogoutView(LogoutView):
#     pass
 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]
    authentication_classes = [JWTCookieAuthentication]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name', 'email']
    filterset_fields = ['is_staff']
    ordering_fields = ['id']


class UserNoteListAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'tags__name']
    ordering_fields = ['created', 'updated']
    ordering = ['-created']

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('id'))
        qs = Note.objects.filter(user=user)
        return qs
    

