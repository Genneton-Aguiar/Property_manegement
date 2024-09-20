from rest_framework import routers
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register(r'user', UsersViewSet, basename = 'user')
router.register(r'property', PropertyViewSet, basename = 'property')
router.register(r'contract', ContractsViewSet, basename = 'contract')
router.register(r'payment', PaymentsViewSet, basename = 'payment')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),
]

