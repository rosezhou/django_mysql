from django.contrib import admin
from .models import *

# Register your models here.

class HeroInfolnline(admin.StackedInline):
    model = HreoInfo
    extra = 2

class AdminInterface(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub']
    list_filter = ['btitle']
    search_fields = ['btitle']
    inlines = [HeroInfolnline]
class AdminHeroinfo(admin.ModelAdmin):
    list_display = ['pk','hname','gender','hcontent']
    list_filter = ['hname']
    search_fields = ['hname']

admin.site.register(BookInfo,AdminInterface)
admin.site.register(HreoInfo,AdminHeroinfo)

