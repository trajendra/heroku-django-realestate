"""raj_django_realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
#from django.contrib.auth.views import login,logout
import realestate.views as prop_ref

urlpatterns = [
        # URL for uploading an image
    url(r'^upload/$', prop_ref.upload),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^login/$', login, name='login'),
    #url(r'^logout/$',logout,{'next_page': '/'}, name='logout'),
    #url(r'^captcha/', include('captcha.urls')),
   
    url(r'^',include("realestate.urls")),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)