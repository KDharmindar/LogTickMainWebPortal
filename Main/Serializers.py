from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from Main.main_models import ProcessData
# Serializers define the API representation.
class ProcessDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProcessData
        fields = '__all__'
        