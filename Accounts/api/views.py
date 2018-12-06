from rest_framework import generics
from .import serializers
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class User_Registration_API_View(generics.CreateAPIView):
    '''
        A class that creates the a Snoze_user instance and stores it to the database
    '''
    serializer_class = serializers.User_Registration_API_Serializer
    # this class specifies that this view is only accessible by staff users
    permission_classes = ('IsAdminUser', )

class User_Deactivate_API_View(APIView):
    permission_classes = ('IsAdminUser', )

    def post(self, request, format=None):
        data = {
                'deactivate failed' :'Account deactivation failed',
            }
        # the token variable will be passed as a post Parameter
        if 'token' in request.POST:
            token = request.POST['token']
            try:
                # check if the token exists 
                user = Token.objects.get(key=token).user
            except ObjectDoesNotExist:
                # if does not exist return 400 error
                return Response(data=data, status=400)
            
            user.is_active = False
            user.save()
            data = {
                'deactivation success' :'Account deactivated successfully',
            }
            # if the user is deactivated successfully return success 200
            return Response(data=data, status=200)
            
