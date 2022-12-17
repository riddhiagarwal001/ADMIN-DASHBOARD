
from django.contrib import admin
from . import models

admin.site.register(models.Vendor)
admin.site.register(models.Unit)
class ProductAdmin(admin.ModelAdmin):
    search_fields=['title','unit__title']
    list_display=['title','unit']

admin.site.register(models.Product,ProductAdmin)



class InwardingAdmin(admin.ModelAdmin):
    search_fields=['product__title']
    list_display=['id','product','quantity','price','total_amount','vendor','recieved_date']
    
admin.site.register(models.Inwarding,InwardingAdmin)

class DistributionAdmin(admin.ModelAdmin):
    search_fields=['product__title']
    list_display=['id','product','quantity','price','total_amount','issued_date']
admin.site.register(models.Distribution,DistributionAdmin)

class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__title','product__unit__title']
    list_display=['product','recieved_quantity','issued_quantity','total_balance_qty','product_unit','recieved_date','issued_date']
admin.site.register(models.Inventory,InventoryAdmin)



