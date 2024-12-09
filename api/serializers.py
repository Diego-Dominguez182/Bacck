from rest_framework import serializers
from base.models import Build

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ['id', 'champion_name', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6']
