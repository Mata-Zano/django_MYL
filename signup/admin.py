from django.contrib import admin
from .models import compra

class compraAdmin(admin.ModelAdmin):
    readonly_fields= ("fecha",)

admin.site.register(compra, compraAdmin)

# Register your models here.
