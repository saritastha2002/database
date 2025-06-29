from django.urls import path
# from .views import category, category_detail
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
router.register('category',CategoryViewset)
urlpatterns = [
#     path("category/",CategoryViewset.as_view({'get':'list' ,'post':'create','destroy':'destroy()'}))
#     # path('category/', category.as_view(), name='category_list'),
#     # path('category_detail/<pk>/', category_detail.as_view(), name='category_detail'),
 ]+router.urls
