from django.contrib import admin
from .models import Cropsdetail
from . models import Market_Price
from . models import Farmers
from . models import Government
from . models import Farmer_training
from . models import Newsupdate

admin.site.register(Cropsdetail)
admin.site.register(Market_Price)
admin.site.register(Farmers)
admin.site.register(Government)
admin.site.register(Newsupdate)
@admin.register(Farmer_training)
class Farmer_trainingAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','contact_number','village','taluka','district','crop_detail')


# Register your models here.
