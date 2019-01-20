from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostModelViewset)

urlpatterns = [
    path('', views.post_list, name= 'post_list'),
    path('api/v1/', include(router.urls)),
]
