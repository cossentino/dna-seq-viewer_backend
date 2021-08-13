from django.contrib import admin
from .models import DNASequence, ProteinSequence

# Register your models here.
admin.site.register(DNASequence)
admin.site.register(ProteinSequence)
