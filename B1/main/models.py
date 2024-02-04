from django.db import models
from django.urls import reverse
#from attachments.models import Attachment
#from attachments.field import AttachmentField

#class TipAttachments(models.Model):
    #file = models.FileField(upload_to='attachments/')


class Tip(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    CHOICES = [
        ('DTW','Data Transfer Workbench'),
        ('B1Up','Boyum B1Up')
    ]
    category = models.CharField(max_length=100, choices=CHOICES)
    file_attachment = models.FileField(upload_to='main/attachments/')
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search(cls, query):
        return cls.objects.filter(title__icontains=query)
    
    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])
# Create your models here.
