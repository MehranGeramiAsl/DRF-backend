from django.shortcuts import render
from blog.models import Article
from .seriallizers import ArticleSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,IsStaffOrReadOnly)
    

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        self.request.auth.delete()
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    
class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)
   
    def delete(self,request):
        request.auth.delete()
        return Response(status=204)