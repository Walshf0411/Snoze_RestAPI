from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import User_Registration_API_View, User_Deactivate_API_View

urlpatterns = [
    # authtoken view to retrieve the user token 
    url(r'^login/$', obtain_auth_token, name='obtain_token'),
    url(r'^register/$',User_Registration_API_View.as_view(), name='register_user'),
    url(r'^deactivate/$', User_Deactivate_API_View.as_view(), name='deactivate'),
]