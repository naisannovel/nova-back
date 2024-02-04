from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserModelSerializer
from rest_framework.authtoken.models import Token
from .models import CustomUserModel


@api_view(['POST'])
def signup(request):
    serializer = CustomUserModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    serializer.save()
    token, created = Token.objects.get_or_create(user=serializer.instance)
    new_data = serializer.data
    del new_data['password']
    response_data = {
        'message': 'User created successfully',
        'data': new_data,
        'token': token.key
    }
    return Response(data=response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = CustomUserModel.objects.filter(email=email).first()
    if user is None:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(password):
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserModelSerializer(user)
    new_data = serializer.data
    del new_data['password']
    response_data = {
        'message': 'Login successful',
        'data': new_data,
        'token': token.key
    }
    return Response(data=response_data, status=status.HTTP_200_OK)

