from django.contrib import admin
from .models import Note
from django.contrib.admin import TabularInline
from taggit.models import Tag

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'user']