from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(admin.AdminSite):
    site_title = _('Order Analytics')  # The title displayed on the login page and browser tab
    site_header = _('Order Analytics')  # The header displayed on the admin dashboard
    index_title = _('Welcome to Order Analytics')  # The title displayed on the home page of the admin interface

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')
