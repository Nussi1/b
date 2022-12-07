from rest_framework import generics
from advertisement.models import Advertisement
from advertisement.api.serializers import AdvertisementSerializer


class AdvertisementList(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all().order_by('-id')[:10]
    serializer_class = AdvertisementSerializer


class AdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


