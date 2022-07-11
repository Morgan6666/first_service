from rest_framework import serializers

from .models import NGSData

class NGSDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NGSData
        fields = ('sequence', )

