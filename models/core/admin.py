from django.contrib import admin
from .models import *


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_name', 'dc', 'on_sale', )
    list_display_links = ('id', 'phone_name', )
    search_fields = ('phone_name', )
    list_editable = ('on_sale', )
    list_filter = ('on_sale', 'dc', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_company', )
    list_display_links = ('name_company', )
    search_fields = ('name_company', )


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Company, CompanyAdmin)