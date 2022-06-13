import imp
from rest_framework.viewsets import ModelViewSet
from myApp.models import Offer, FamilyType, ProgressState
from rest_framework.permissions import AllowAny
from myApp.apis.serializers import OfferSerializer, FamilyTypeSerializer, PossibleProgressStateSerializer


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = OfferSerializer  

class FamilyTypeViewSet(ModelViewSet):
    queryset = FamilyType.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = FamilyTypeSerializer

class PossibleProgressStatesViewSets(ModelViewSet):
    queryset = ProgressState.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = PossibleProgressStateSerializer

