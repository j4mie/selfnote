from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User)
    content = models.TextField()
        
    def __unicode__(self):
        maxchars = 50
        if len(self.content) < maxchars:
            return self.content
        else:
            return self.content[0:50] + ' (...)'