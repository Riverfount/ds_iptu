from django.conf.urls import url
from django.contrib import admin
from iptu.core.views import home, create_file

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^create_file/', create_file, name='create_file'),
    url(r'^admin/', admin.site.urls),
]
