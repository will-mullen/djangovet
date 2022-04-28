from django.contrib import admin
from django.contrib.auth.models import Group 
from .models import FB_N_01, Red_Line_Tracking, Visits, Customers


admin.site.site_header = 'Admin Sample SDV Page'
admin.site.register(Visits)
admin.site.register(Customers)
admin.site.register(FB_N_01)
admin.site.register(Red_Line_Tracking)

# Register your models here.
