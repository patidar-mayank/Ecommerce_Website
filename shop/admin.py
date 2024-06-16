from django.contrib import admin
from .models import Products,Order
# Register your models here.



#change header of admin panel name
admin.site.site_header="E-Commerce Site"
admin.site.site_title="Magical Menagerie"
admin.site.index_title="Magical Menagerie Shop"

class ProductAdmin(admin.ModelAdmin):
    #change category fucntion
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")


    list_display=('title','price','discount_price','category','description')
    search_fields=('title',)
    actions=('change_category_to_default',)
    #hiding specific field
    fields=('title','price',)
    list_editable=('price',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)    
