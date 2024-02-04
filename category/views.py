from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .permissions import CustomIsAdminUser


class CategoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, CustomIsAdminUser]

    def get_authenticators(self):
        if self.request.method == 'POST':
            # self.authentication_classes = []
            self.request.user = 'naisan@mail.com'
        return super().get_authenticators()

    def get_permissions(self):
        print(self.request.user)
        if self.request.method == 'GET':
            self.permission_classes = []
        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
            'message': 'Category created successfully',
            'data': serializer.data
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

