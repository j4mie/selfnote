from django.forms import ModelForm

class NoteForm(ModelForm):
    class Meta:
        model = Note