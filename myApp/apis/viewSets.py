from rest_framework.viewsets import ModelViewSet
from myApp.models import Offer, FamilyType, ProgressState, Family
from rest_framework.permissions import AllowAny
from myApp.apis.serializers import OfferSerializer, FamilyTypeSerializer, PossibleProgressStateSerializer, FamilySerializer
from rest_framework.response import Response
from rest_framework import status


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = OfferSerializer

class FamilyTypeViewSet(ModelViewSet):
    queryset = FamilyType.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = FamilyTypeSerializer

class PossibleProgressStatesViewSets(ModelViewSet):
    queryset = ProgressState.objects.filter().all()
    permission_classes = [AllowAny, ]
    serializer_class = PossibleProgressStateSerializer


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = FamilySerializer

    def create(self, request, *args, **kwargs):
        """You can implement the price ranges here according to your logic"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

