from django.contrib import admin
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
	ordering = ['-created_at']
	list_display = ['__unicode__', 'created_by', 'created_at']
	
admin.site.register(Note, NoteAdmin)