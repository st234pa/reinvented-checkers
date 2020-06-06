""" API requests and responses. """
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import status
from . import serializers


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """ Returns a token or an error based on login POST request. """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(["GET"])
def sample_api(request):
    """ Placeholder protected api endpoint. """
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


class SampleView(APIView):
    """ Placeholder protected api endpoint. """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """ Protected get request handler. """
        user = request.user
        content = {'message': 'Hello, ' + user.username + '!'}
        return Response(content, status=HTTP_200_OK)


class UserCreate(APIView):
    """  Creates the user.  """
    permission_classes = (AllowAny,)

    def post(self, request, _='json'):
        """ Creates response with token based on create user POST request. """
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
