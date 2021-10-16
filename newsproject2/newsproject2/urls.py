"""newsproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/',views.videos_view,name="videos"),
    path('audio/',views.audios_view,name="audio"),
    path('trend/',views.news_view,name="trends"),
    path('memes/',views.memes_view,name="memes"),
    path('tag/(?p<tag_slug>[-\w]/$',views.news_view,name="news_tag"),
    path('tag/(?p<tag_slug1>[-\w]/$',views.videos_view,name="videos_tag"),
    path('tag/(?p<tag_slug3>[-\w]/$',views.memes_view,name="memes_tag")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
