from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from notes.models import Note

def index(request, error=False):
    if request.user.is_authenticated():
        notes = Note.objects.filter(
            created_by = request.user
        ).order_by('-created_at')
        
        return render_to_response('selfnote/index_logged_in.html', { 
            'error': error,
            'notes': notes ,
        })
    else:
        return render_to_response('selfnote/index_not_logged_in.html')
        
def notes(request):
    if request.method == 'POST':
        content = request.POST.get("content", False)
        
        if not content or len(content) == 0:
            return index(request, 'Gimme a note, foo')
        else:
            note = Note(content=content, created_by=request.user)
            note.save()
            return HttpResponseRedirect('/')