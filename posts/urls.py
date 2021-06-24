from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('users/', UserList.as_view(), name='users'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('', PostList.as_view(), name='posts'),
#     path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
# ]
