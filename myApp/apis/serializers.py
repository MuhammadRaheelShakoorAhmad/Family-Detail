from attr import fields
from myApp.models import Offer, FamilyType, ProgressState, Family
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
        model = ProgressState
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
