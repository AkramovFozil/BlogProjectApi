from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlogPostListCreateView, BlogPostDetailView, RegisterView, LogOutView

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogOutView.as_view(), name='logout'),
    path('posts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]
