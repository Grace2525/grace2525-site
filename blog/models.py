from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
    about = models.CharField(max_length=30)
    def __str__(self):
        return self.about

class Blog(models.Model):
    title = models.CharField(max_length=30)
    date_added = models.DateTimeField()
    about = models.CharField(max_length=30)
    topics = models.ManyToManyField(Topic)
    content = RichTextUploadingField()
    def __str__(self):
        return self.title
    
