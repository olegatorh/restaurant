from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()
router.register(r'menu', MenuView)
router.register(r'restaurant', RestaurantView)
router.register(r'vote_menu', VoteMenuView)
router.register(r'employee', EmployeeView)

urlpatterns = [
    path('auth/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegistrationAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
