from django.contrib import admin
from .models import Order
from .forms import OrderForm
from .admin_site import custom_admin_site

class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    fieldsets = (
        ('Personal Info:', {
            'fields': ('name', 'contact_phone', 'email', 'job_name', 'date', 'ordered_by', 'ship_to', 'address','QO','signature')
        }),
        ('First Row:', {
            'fields': ('quantity1','width1','height1','tempgl1','window_type1','rh1','bnb1','notes1','Size_Options1','color1','Frame_Options1','Grille_Options1','Glass_Options1')
        }),
        ('Second Row:', {
            'fields': ('quantity2','width2','height2','tempgl2','window_type2','rh2','bnb2','notes2','Size_Options2','color2','Frame_Options2','Grille_Options2','Glass_Options2')
        }),
        ('Third Row:', {
            'fields': ('quantity3','width3','height3','tempgl3','window_type3','rh3','bnb3','notes3','Size_Options3','color3','Frame_Options3','Grille_Options3','Glass_Options3')
        }),
        ('Forth Row:', {
            'fields': ('quantity4','width4','height4','tempgl4','window_type4','rh4','bnb4','notes4','Size_Options4','color4','Frame_Options4','Grille_Options4','Glass_Options4')
        }),
        ('Fifth Row:', {
            'fields': ('quantity5','width5','height5','tempgl5','window_type5','rh5','bnb5','notes5','Size_Options5','color5','Frame_Options5','Grille_Options5','Glass_Options5')
        }),

    )

custom_admin_site.register(Order, OrderAdmin)
