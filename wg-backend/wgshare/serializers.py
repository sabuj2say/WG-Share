from rest_framework import serializers
from .models import wgshare

class wgshareSerializer(serializers.ModelSerializer):

    class Meta:
        model = wgshare 
        fields = ('pk', 'name', 'email', 'details', 'cost', 'registrationDate')


