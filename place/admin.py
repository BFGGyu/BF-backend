from django.contrib import admin
from .models import Facility, Station, FacAmenity, StatAmenity

# Register your models here.
admin.site.register(Facility)
admin.site.register(Station)
admin.site.register(FacAmenity)
admin.site.register(StatAmenity)