from rest_framework import serializers
from administrator.models import *


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = (
            'DNI', 'Name', 'Last_Name', 'Email', 'Password'
        )
