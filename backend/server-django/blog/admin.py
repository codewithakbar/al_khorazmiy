from django.contrib import admin

from .models import (
    BIZ_HAQIMIZDA, BIZ_HAQIMIZDA_IMAGE, ISH_JARAYONI, 
    PROEKTLARIMIZ, Video, IjtimoiyTarmoqLink
)


class BIZ_HAQIMIZDA_IMAGE_Inline(admin.TabularInline):
    model = BIZ_HAQIMIZDA_IMAGE
    extra = 8


@admin.register(BIZ_HAQIMIZDA)
class BizHaqimizdaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    inlines = [BIZ_HAQIMIZDA_IMAGE_Inline]


@admin.register(BIZ_HAQIMIZDA_IMAGE)
class BIZ_HAQIMIZDA_IMAGEAdmin(admin.ModelAdmin):
    list_display = ['biz_haqda']


admin.site.register(ISH_JARAYONI)
admin.site.register(PROEKTLARIMIZ)
admin.site.register(Video)
admin.site.register(IjtimoiyTarmoqLink)
