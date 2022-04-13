import imp
from re import I
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Product
from .serializer import *
from rest_framework import viewsets
from django.contrib.auth.models import User

# def image_upload(request):
#     if request.method == "POST" and request.FILES["image_file"]:
#         image_file = request.FILES["image_file"]
#         fs = FileSystemStorage()
#         filename = fs.save(image_file.name, image_file)
#         image_url = fs.url(filename)
#         print(image_url)
#         return render(request, "upload.html", {
#             "image_url": image_url
#         })
#     return render(request, "upload.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
