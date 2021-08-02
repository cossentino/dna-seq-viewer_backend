from django.db import models

# Create your models here.


class DNASequence(models.Model):
    raw_sequence = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")

    class SequenceType(models.IntegerChoices):
        DNA = 1
        PROTEIN = 2

    sequence_type = models.IntegerField(
        choices=SequenceType.choices, default=1)
