from django.urls import path
from . import views


urlpatterns = [
    path("kullanici-kayit/",views.kullanici_kayit , name="kullanici-kayit"),
    path("kirli-bolge-ekleme/",views.kirli_bolge_ekleme , name="kirli-bolge-ekleme"),
    path("kirli-bolgeler/",views.kirli_bolgeler , name="kirli-bolgeler"),
    path("kullanici-bilgisi/",views.kullanici_bilgileri,name="kullanici-bilgisi"),
    path("kullanici-atiklari/",views.kullanicinin_atiklari,name="kullanici-atiklari"),
    path("kullanici-atik-temizleme/",views.atik_temizleme,name="kullanici-atik-temizleme"),

]
