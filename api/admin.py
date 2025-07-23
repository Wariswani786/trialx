

from django.contrib import admin
from .models import PatientProfile
from .models import ClinicalTrial

admin.site.register(PatientProfile)
admin.site.register(ClinicalTrial)