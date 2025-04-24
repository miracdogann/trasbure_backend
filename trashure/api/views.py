from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Kullanicilar , KirliBolgeler
from .serializers import KullanicilarSerializer , KirliBolgelerSerializer


@api_view(['POST'])
def kullanici_kayit(request):
    print("istek atıldı")
    # Serializer ile gelen veriyi doğrula
    serializer = KullanicilarSerializer(data=request.data)
    
    if serializer.is_valid():  # Veriler geçerliyse
        print("veriler doğru")
        # Veriyi kaydet
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print("yanklışşşşşş")
    # Veriler geçerli değilse hata döndür
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def kirli_bolge_ekleme(request):

    print("kirli bölge eklemeye istek atıldı ")
    # Serializer ile gelen veriyi doğrula
    serializer = KirliBolgelerSerializer(data=request.data)
    print("Gelen veri:", request.data)
    alan_bilgileri = request.data.get("alanBilgileri", {})
    serializer = KirliBolgelerSerializer(data=alan_bilgileri)

    if serializer.is_valid():  # Veriler geçerliyse
        print("veriler doğru")
        # Veriyi kaydet
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print("yanlışşşşşş")
    print("Hatalar:", serializer.errors)  # Hangi alanlarda hata olduğunu görmek için
    # Veriler geçerli değilse hata döndür
    # Veriler geçerli değilse hata döndür
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def kirli_bolgeler(request):
    bolgeler = KirliBolgeler.objects.all()  # KirliBolgeler modelinden tüm veriyi alıyoruz
    serializer = KirliBolgelerSerializer(bolgeler, many=True)  # Veriyi JSON formatına dönüştürüyoruz
    print("serializer",serializer)
    return Response(serializer.data)  # JSON formatında döndürüyoruz