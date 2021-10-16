from os import utime
from django.contrib import admin
from . models import Trends,Audios,Videos,Memes

class TrendAdmin(admin.ModelAdmin):
    list_display=['id','link','body','source','created','updated']

class AudioAdmin(admin.ModelAdmin):
    list_display=['id','song','artistname','image','created','updated']

class VideoAdmin(admin.ModelAdmin):
    list_display=['id','video','vimage','created','updated']

class MemeAdmin(admin.ModelAdmin):
    list_display=['id','mimage','caption','created','updated']    


# Register your models here.
admin.site.register(Trends,TrendAdmin)
admin.site.register(Audios,AudioAdmin)
admin.site.register(Videos,VideoAdmin)
admin.site.register(Memes,MemeAdmin)