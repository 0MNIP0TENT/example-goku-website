from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse

class Videos(models.Model):
    name = models.CharField(max_length=255)
    videofile = models.FileField(upload_to='videos', null=True,verbose_name="")
    date = models.DateTimeField(auto_now_add=True)
    verbose_name = 'videos'
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.name + ': ' + str(self.videofile)

class Comment(models.Model):
    video = models.ForeignKey(
        Videos,
        on_delete = models.CASCADE,
        related_name = 'Comments',
    )
    comment = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.comment
    
    def get_absolute_url():
        return reverse('videos')
