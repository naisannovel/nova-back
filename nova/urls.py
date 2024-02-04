from django.urls import path, include

urlpatterns = [
    path('', include('customuser.urls')),
    path('category', include('category.urls')),
    path('product', include('product.urls')),
]
