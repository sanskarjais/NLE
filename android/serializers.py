from rest_framework import serializers

from .models import App

class AppSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = App
        fields = ['name','applink','app_category','sub_category','points']