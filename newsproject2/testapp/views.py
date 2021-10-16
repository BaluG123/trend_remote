from django.shortcuts import render,get_object_or_404
from . models import Trends,Audios,Videos,Memes
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from taggit.models import Tag

# Create your views here.
def news_view(request,tag_slug=None):
    trends_list=Trends.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        trends_list=trends_list.filter(tags__in=[tag])
    paginator=Paginator(trends_list,4)
    page_number=request.GET.get('page')
    try:
        trends_list=paginator.page(page_number)
    except PageNotAnInteger:
        trends_list=paginator.page(1)
    except EmptyPage:
        trends_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/news.html',{'trends_list':trends_list,'tag':tag})

def videos_view(request,tag_slug1=None):
    videos_list=Videos.objects.all()
    vd=None
    if tag_slug1:
        vd=get_object_or_404(Tag,slug=tag_slug1)
        videos_list=videos_list.filter(vds__in=[vd])
    paginator=Paginator(videos_list,4)
    page_number=request.GET.get('page')
    try:
        videos_list=paginator.page(page_number)
    except PageNotAnInteger:
        videos_list=paginator.page(1)
    except EmptyPage:
        videos_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/video.html',{'videos_list':videos_list,'vd':vd}) 

def audios_view(request,tag_slug2=None):
    audios_list=Audios.objects.all()
    ad=None
    if tag_slug2:
        ad=get_object_or_404(Tag,slug=tag_slug2)
        audios_list=audios_list.filter(ads__in=[ad])
    paginator=Paginator(audios_list,4)
    page_number=request.GET.get('page')
    try:
        audios_list=paginator.page(page_number)
    except PageNotAnInteger:
        audios_list=paginator.page(1)
    except EmptyPage:
        audios_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/audio.html',{'audios_list':audios_list,'ad':ad})
   

def memes_view(request,tag_slug3=None):
    memes_list=Memes.objects.all()
    mm=None
    if tag_slug3:
        mm=get_object_or_404(Tag,slug3=tag_slug3)
        memes_list=memes_list.filter(mms__in=[mm])
    paginator=Paginator(memes_list,4)
    page_number=request.GET.get('page')
    try:
        memes_list=paginator.page(page_number)
    except PageNotAnInteger:
        memes_list=paginator.page(1)
    except EmptyPage:
        memes_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/memes.html',{'memes_list':memes_list,'mm':mm})  