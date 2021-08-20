from django.contrib import admin
from .models import Sequence, GenBankAnnotationSet

# Register your models here.
admin.site.register(Sequence)
admin.site.register(GenBankAnnotationSet)
