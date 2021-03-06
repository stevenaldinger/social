"""Project_SLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .settings import MEDIA_ROOT
from django.views.static import serve
from core import views as core_views
from feed import views as feed_views
from post import views as post_views
from blog import views as blog_views
from projects import views as projects_views
from softwares import views as softwares_views
from accounts import views
from activities import views as activities_views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'', include('core.urls')),
    url(r'^register/$', core_views.register, name = 'register'),
    url(r'^login/$', core_views.user_login, name='login'),
    url(r'^logout/$', core_views.user_logout, name='logout'),
    url(r'^auth/', include(('social_django.urls', 'social_django'), namespace='social')),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',post_views.post, name='post_by_tag'),
    url(r'^feed/', include(('feed.urls', 'feed'), namespace='home')),
    url(r'^post/', include('post.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^softwares/', include('softwares.urls')),
    url(r'^activities/', include('activities.urls')),
    url(r'^accounts/', include('accounts.urls')),
    # comments
    url(r'^comments/posted/$', blog_views.comment_posted),
    url(r'^comments/posted/$', post_views.comment_posted),
    url(r'^comments/posted/$', projects_views.comment_posted),
    url(r'^comments/posted/$', softwares_views.comment_posted),
    url(r'^comments/posted/$', activities_views.comment_posted),
    url(r'^comments/', include('django_comments.urls')),



]
