from rest_framework import serializers
from jsondata.models import EnergyInsight

class DataItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyInsight
        fields = '__all__'
