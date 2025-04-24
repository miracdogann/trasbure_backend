from django.db import models

class Cleanups(models.Model):
    id = models.AutoField(primary_key=True)  # Auto increment id as primary key
    user = models.ForeignKey('Kullanicilar', on_delete=models.CASCADE, blank=True, null=True)
    area = models.ForeignKey('KirliBolgeler', on_delete=models.CASCADE, related_name='cleanups_area_set', blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    ilkfoto = models.TextField(db_column='ilkFoto', blank=True, null=True)
    son_foto = models.TextField(blank=True, null=True)
    kazanilan_puan = models.IntegerField(blank=True, null=True)
    adminonayladimi = models.BooleanField(db_column='adminOnayladiMi', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cleanUps'

class EtinklikKatilimlari(models.Model):
    id = models.AutoField(primary_key=True)
    etkinlik = models.ForeignKey('Etkinlikler', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('Kullanicilar', on_delete=models.CASCADE, related_name='etinklikkatilimlari_user_set', blank=True, null=True)
    katilim_tarihi = models.DateField(blank=True, null=True)
    katildi_mi = models.BooleanField(blank=True, null=True)
    puan_verildimi = models.BooleanField(db_column='puan_verildiMi', blank=True, null=True)

    class Meta:
        db_table = 'etinklik_katilimlari'


class Etkinlikler(models.Model):
    id = models.AutoField(primary_key=True)
    orgranizator = models.ForeignKey('Kullanicilar', on_delete=models.CASCADE, blank=True, null=True)
    etkinlik_title = models.TextField(blank=True, null=True)
    etkinlik_decription = models.TextField(blank=True, null=True)
    etkinlik_yeri = models.TextField(blank=True, null=True)
    etkinlik_date = models.DateTimeField(blank=True, null=True)
    puan = models.IntegerField(blank=True, null=True)
    kontenjan = models.IntegerField(blank=True, null=True)
    ucret = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'etkinlikler'


class KirliBolgeler(models.Model):
    user = models.ForeignKey(
        'Kullanicilar',
        to_field='firebase_uid',  # işte burası önemli
        db_column='user_uid',     # veritabanındaki kolon adı
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    photo_path = models.TextField(blank=True, null=True)
    cop_turu = models.TextField(blank=True, null=True)
    cop_miktari = models.IntegerField(blank=True, null=True)
    temizleme_suresi = models.TextField(blank=True, null=True)
    durum = models.TextField(blank=True, null=True)
    paylasim_tarihi = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'kirli_bolgeler'


class Kullanicilar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    lastname = models.TextField(db_column='lastName', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    firebase_uid = models.TextField(unique=True)

    class Meta:
        db_table = 'kullanicilar'


class Urunler(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    kac_puan = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'urunler'


class UserProfiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Kullanicilar', on_delete=models.CASCADE, blank=True, null=True)
    profil_aciklamasi = models.TextField(blank=True, null=True)
    rozetler = models.IntegerField(blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)
    haftalik_aktiflik = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_profiles'


class UserRewards(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Kullanicilar', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey('Urunler', on_delete=models.CASCADE, related_name='userrewards_product_set', blank=True, null=True)
    satinalmatarihi = models.DateTimeField(db_column='satinAlmaTarihi', blank=True, null=True)
    harcana_puan = models.IntegerField(blank=True, null=True)
    durum = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'user_rewards'
