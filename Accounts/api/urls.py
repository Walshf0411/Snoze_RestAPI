from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import User_Registration_API_View, User_Deactivate_API_View

urlpatterns = [
    # authtoken view to retrieve the user token 
    # username, password, <admin token> POST
    url(r'^login/$', obtain_auth_token, name='obtain_token'),
    # username, password, first_name, last_name, email, phone_number POST
    url(r'^register/$',User_Registration_API_View.as_view(), name='register_user'),
    # token of the user through POST 
    url(r'^deactivate/$', User_Deactivate_API_View.as_view(), name='deactivate'),
]