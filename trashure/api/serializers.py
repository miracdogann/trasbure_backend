from rest_framework import serializers
from ..models import Kullanicilar , KirliBolgeler

class KullanicilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanicilar
        fields = ["name","lastname","email","firebase_uid"]



class KirliBolgelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KirliBolgeler
        fields = '__all__'
