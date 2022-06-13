from myApp.models import Offer, FamilyType, ProgressState
from rest_framework import serializers


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'offer_name', 'calculation', 'low', 'high']

class FamilyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyType
        fields = '__all__'

class PossibleProgressStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressState.objects.all()
        fields = '__all__'
