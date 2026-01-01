from .models import Women , Category
from rest_framework import serializers



class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'content', 'cat')

