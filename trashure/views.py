from django.http import HttpResponse , JsonResponse

from .models import Kullanicilar


def home(request):

    users  =Kullanicilar.objects.all()
    users = list(users.values())
    return HttpResponse(users)