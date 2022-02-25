from django.contrib import admin
from main.models import Note



class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')

admin.site.register(Note, NoteAdmin)
