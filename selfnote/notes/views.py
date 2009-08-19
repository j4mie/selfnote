from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from notes.models import Note


     
def _get_index(request, message=False):
    if request.user.is_authenticated():
        notes = Note.objects.filter(
            created_by = request.user
        ).order_by('-created_at')
        
        return render_to_response('selfnote/index_logged_in.html', { 
            'message': message,
            'notes': notes ,
        })
    else:
        return render_to_response('selfnote/index_not_logged_in.html')
   
def _post_index(request):
    content = request.POST.get("content", False)
    
    if not content or len(content) == 0:
        message = {'class': 'error', 'content': 'Please supply a note'}
        return _get_index(request, message)
    else:
        note = Note(content=content, created_by=request.user)
        note.save()
        return HttpResponseRedirect('/')
            
def index(request):
    if request.method == 'GET':
        return _get_index(request)
    else:
        return _post_index(request)