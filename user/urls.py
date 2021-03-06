from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^login/?$', UserLogin.as_view()),
    url(r'^logout/?$', UserLogout.as_view()),
    url(r'^register/?$', UserRegister.as_view()),
    url(r'^activate/?$', UserActivation.as_view()),
    url(r'^form/?$', FormEdit.as_view()),
    url(r'^file/?$', UploadFile.as_view()),
    url(r'^user/?$', GetUser.as_view()),
    url(r'^check/?$', GetFileStatus.as_view()),
    url(r'^status/?$', GetStatus.as_view()),
]
