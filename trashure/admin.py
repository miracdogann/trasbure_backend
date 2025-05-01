from django.contrib import admin
from .models import Kullanicilar , KirliBolgeler , Cleanups , UserProfiles , Urunler , Etkinlikler , EtinklikKatilimlari , UserRewards
# Register your models here.

admin.site.register(Kullanicilar)
admin.site.register(KirliBolgeler)
admin.site.register(Cleanups)
admin.site.register(UserProfiles)
admin.site.register(Urunler)
admin.site.register(Etkinlikler)
admin.site.register(EtinklikKatilimlari)
admin.site.register(UserRewards)