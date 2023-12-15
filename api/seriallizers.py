from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ("updated","created")
      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"