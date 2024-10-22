from django.contrib import admin
from .models import News

# Register your models here.
# News modelini admin panelda sozlash uchun
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Admin panelda title ko'rinadi


admin.site.register(News, NewsAdmin)