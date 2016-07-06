"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include,url


import polls
from polls.views import index,html,modify_html,hello_1,Contact_Form,html1,User_Login,Entry_one,\
login_view,logout_view,register_view,contact,mainpage,detailedRange,uday_login,uday_authenticate,\
File_Upload_View,File_Upload_Html_To_Other,home_view,Audio_Video_View



#importten to learn this include
# url(r'^',include('posturs',namespace='posts'))




urlpatterns = [
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^hello/', index),
    url(r'^html/', html),
    url(r'^audio/', Audio_Video_View),
    url(r'^home_view/', home_view),
    url(r'^Entry_one/', Entry_one),
    url(r'^html1/', html1),
    url(r'^hello_1/', hello_1),
    url(r'^Contact_Form/',Contact_Form),
    url(r'^User_Login/', User_Login),
    url(r'^logout/', logout_view),
    url(r'^register/', register_view),
    url(r'^contact/', contact),
    url(r'^mainpage/', mainpage),
    url(r'^Login/', login_view ),
    url(r'^detailedRange/', detailedRange),
    # url(r'^',include('Login',namespace='login_view',app_name='polls')),
    url(r'^modify_html/', modify_html),
    url(r'^uday_login/', uday_login),
    url(r'^uday_auth/', uday_authenticate),
    url(r'^fileupload/',File_Upload_View ),
    url(r'^otherhtml/', File_Upload_Html_To_Other),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



