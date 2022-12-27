from django.shortcuts import render
from .models import (
    BIZ_HAQIMIZDA, ISH_JARAYONI, PROEKTLARIMIZ, Video, IjtimoiyTarmoqLink,
    BIZ_HAQIMIZDA_IMAGE
)



def index(request):
    biz_haqda = BIZ_HAQIMIZDA.objects.all()[:1]
    ish_jarayoni = ISH_JARAYONI.objects.all()
    projects = PROEKTLARIMIZ.objects.all()
    videolar = Video.objects.all()
    links = IjtimoiyTarmoqLink.objects.all()
    biz_haqda_image = BIZ_HAQIMIZDA_IMAGE.objects.all()


    context = {
        'biz_haqda': biz_haqda,
        'ish_jarayoni': ish_jarayoni,
        'projects': projects,
        'videolar': videolar,
        'links': links,
        'biz_haqda_image': biz_haqda_image,
    }




    return render(request, 'blog/index.html', context)