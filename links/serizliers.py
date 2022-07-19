from rest_framework import serializers
from .models import Link 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'