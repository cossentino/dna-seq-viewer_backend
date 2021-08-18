from django.contrib import admin
from .models import GenBankSequence, FastaSequence

# Register your models here.
admin.site.register(GenBankSequence)
admin.site.register(FastaSequence)
