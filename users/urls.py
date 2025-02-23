from django.urls import path, include
from .views import UserViewSet, SignUpView
from rest_framework.routers import SimpleRouter


router_user = SimpleRouter()
router_user.register(r'userlist', UserViewSet)


urlpatterns = [
    path('', include(router_user.urls)),
    path('my_profile/', UserViewSet.as_view({'get':'my_profile'})),
    path('user_registration/', SignUpView.as_view(), name='user_registration')
]