from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title
class Answer(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Reply(models.Model):
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
