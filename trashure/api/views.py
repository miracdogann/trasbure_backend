from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Kullanicilar , KirliBolgeler , Cleanups
from .serializers import KullanicilarSerializer , KirliBolgelerSerializer


@api_view(['POST'])
def kullanici_kayit(request):
    print("istek atıldı")
    # Serializer ile gelen veriyi doğrula
    print("kayıt apisine gelen veriler ",request.data)
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
    # alan_bilgileri = request.data.get("alanBilgileri", {})
    serializer = KirliBolgelerSerializer(data=request.data)

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


@api_view(['POST'])
def kullanici_bilgileri(request):
    email = request.data.get('email')  # POST verisinden email çekiyoruz
    print("email adresiiii:",email)
    try:
        kullanici = Kullanicilar.objects.get(email=email)  # email'e göre kullanıcıyı buluyoruz
        serializer = KullanicilarSerializer(kullanici)
        return Response(serializer.data)
    except Kullanicilar.DoesNotExist:
        return Response({'error': 'Kullanıcı bulunamadı'}, status=404)
    


@api_view(["POST"])
def kullanicinin_atiklari(request):

    user_id = request.data.get("user_id")  # frontend'den uid olarak gelsin
    print("Kullanıcı firebase_uid -->", user_id)
    
    try:
        bolgeler = KirliBolgeler.objects.filter(user=user_id)
        if not bolgeler.exists():
            return Response([], status=202)

        serializer = KirliBolgelerSerializer(bolgeler, many=True)
        print("veriler geldi")
        return Response(serializer.data, status=200)

    except Exception as e:
        print("Sunucu hatası:", e)
        return Response({'error': 'Sunucu hatası oluştu.'}, status=500)
    
    
    
@api_view(["POST"])
def atik_temizleme(request):

    try:
        print("atik temizlemeye istek atıldı")
        user_uid = request.data.get("user_uid")
        print("useri uid miz ", user_uid)
        # user_uid ye göre arama yapalım user ın id sine erişelim ve ismine 
        user = Kullanicilar.objects.get(firebase_uid = user_uid)
        print("user id ", user.id)
        userId = user.id


        org_photo_url = request.data.get("org_photo_url")
        bolge = KirliBolgeler.objects.get(photo_path= org_photo_url) 
        org_photo_id = bolge.id

        print("orijinal fotoğraf id  " , org_photo_id)
    
        photo1 = request.data.get("photo1")
        photo2 = request.data.get("photo2")
        kazanilan_puan = 25
        # Cleanups tablosuna kayıt ekleniyor
        cleanup = Cleanups.objects.create(
                user_id=userId,
                area_id=org_photo_id,
                ilkfoto=photo1,
                son_foto=photo2,
                kazanilan_puan = kazanilan_puan
            )
        bolge.durum = "Temizlendi"
        bolge.save()
        print("son duurum",bolge.durum)
        # Eğer kullanıcı puanı None ise 0 olarak ata
        if user.points is None:
            user.points = 0

        user.points += kazanilan_puan
        user.save()
        return Response({"message": "Kayıt başarıyla oluşturuldu."}, status=status.HTTP_201_CREATED)
    except Kullanicilar.DoesNotExist:
        return Response({"error": "Kullanıcı bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
    except KirliBolgeler.DoesNotExist:
        return Response({"error": "Kirli bölge bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




