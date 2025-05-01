from rest_framework import serializers
from ..models import Kullanicilar , KirliBolgeler , Cleanups

class KullanicilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanicilar
        fields = ["name","lastname","email","points","firebase_uid"]



class KirliBolgelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KirliBolgeler
        fields = '__all__'



class CleanupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleanups
        fields = '__all__'