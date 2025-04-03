from rest_framework import serializers
from .models import Project, HomePageTxts

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TxtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageTxts
        fields = '__all__'
