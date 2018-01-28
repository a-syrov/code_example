from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'bash', views.BashQuoteViewSet)
router.register(r'bashabyss', views.BashAbyssQuoteViewSet)

urlpatterns = [
	path('', include(router.urls)),
]