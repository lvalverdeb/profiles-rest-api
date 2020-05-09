from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)  # no basename required since we have specified a queryset in the viewset

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls) )
]

#Monitoring And Transport Through Intelligent Linking and Directed Assistance