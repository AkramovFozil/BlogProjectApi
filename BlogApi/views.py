from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from .models import BlogPost
from .serializers import RegisterSerializer, BlogPostSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Tizimdan muvafqqiyatli chiqdingiz.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': "Tokenni bekor qilishda xatolik yuz berdi"}, status=status.HTTP_400_BAD_REQUEST)


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            post = self.get_object()
            if self.request.user.role == 'admin' or self.request.user == post.author:
                return [IsAuthenticated()]
            return [AllowAny()]
