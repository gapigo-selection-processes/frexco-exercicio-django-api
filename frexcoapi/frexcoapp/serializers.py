from rest_framework import serializers
from frexcoapp.models import Region, Fruit

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['name', 'region']