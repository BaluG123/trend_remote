from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Trends(models.Model):
    title=models.CharField(max_length=128)
    link=models.CharField(max_length=1000)
    image=models.FileField(null=True,blank=True,upload_to='images/')
    body=models.TextField()
    source=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    tags=TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']

class Audios(models.Model):
    songname=models.CharField(max_length=256)
    song=models.FileField(null=True,blank=True,upload_to='songs/')
    artistname=models.CharField(max_length=128)
    image=models.FileField(null=True,blank=True,upload_to='images/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    ads=TaggableManager()

    def __str__(self):
        return self.songname

    class Meta:
        ordering=['-created']

class Videos(models.Model):
    videotitle=models.CharField(max_length=256)
    video=models.FileField(null=True,blank=True,upload_to='videos/')
    vimage=models.FileField(null=True,blank=True,upload_to='images/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    vds=TaggableManager()

    def __str__(self):
        return self.videotitle

    class Meta:
        ordering=['-created']    

class Memes(models.Model):
    mimage=models.FileField(null=True,blank=True,upload_to='images/')
    caption=models.CharField(max_length=28,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    mms=TaggableManager()

    def __str__(self):
        return self.caption

    class Meta:
        ordering=['-created']    




