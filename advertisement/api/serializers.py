from rest_framework import serializers
from advertisement.models import Advertisement, AdvertisementImage


class AdvertisementSerializer(serializers.ModelSerializer):
  class Meta:
    model = Advertisement
    fields = ['title', 'user', 'description', 'head_image']


class AdvertisementImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = AdvertisementImage
    fields = ['advertisement', 'image']