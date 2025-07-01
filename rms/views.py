from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import CategorySerializer,FoodSerializer
from rest_framework import status
from rest_framework.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class CategoryViewset(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
# from rest_framework.mixins
# Create your views here.
# @api_view(['GET','POST'])
class category(ListAPIView,CreateAPIView):
    # if request.method=="GET":
    queryset=Category.objects
    serializer_class=CategorySerializer
    # def get(self,request):
    #     category = self.all()
    #     serializer=CategorySerializer(category,many=True)
    #     return Response(serializer.data)
    
    
    # elif request.method=="POST":
    
    # def post(self,request):
    #     serializer=CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"detail: New Category created"},status = status.Http_201_CREATED)
    
# @api_view(['GET','DELETE','PUT'])
class category_detail  (RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # if request.method == 'GET':
    # def get(self,request,pk):
    #     try:
    #         category=Category.objects.get(pk=pk)
        # if category == None:
        #     raise ValidationError({"detail : Category not found"}, status =status.HTTP_404_NOT_FOUND)
        # serializer = CategorySerializer(category)
        #     serializer = CategorySerializer(category)
        #     return Response(serializer.data)
        # except:
        #     return Response({"detail: Category not found"} , status=status.HTTP_404_NOT_FOUND)
        
        
    # elif request.method == 'DELETE':
    #     category = Category.objects.get(pk=pk)
    
    # def delete(self,request,pk):
    #     category=Category.objects.get(pk=pk)
    #     orderitem=OrderItem.objects.filter(food__category =category).count()
    #     if orderitem>0:
    #         return Response({"details : This category exist in order.Can not delete category"})
    #     category.delete()
    #     return Response({"detail: Category deleted"}, status=status.Http_204_NO_CONTENT)
    
    # # elif request.method =='PUT':
    # #     serializer=CategorySerializer(Category,data = request.data)
    # def put(self,request,pk):
    #     category = Category.objects.get(pk=pk)
    #     serializer=CategorySerializer(category,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
        
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     return Response({
    #         "detail: Category Update"
    #         "data":serializer.data
    #         },status = status.Http_200_OK)
    
class FoodViewset(ModelViewSet):
    queryset=Food.objects.select_related('category').all()
    serializer_class=FoodSerializer
    pagination_class=PageNumberPagination