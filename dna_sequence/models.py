import pdb
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_sequence(seq_string):
    for char in seq_string:
        if char not in ['A', 'T', 'C', 'G']:
            raise ValidationError(
                "We came across a character %s that is not valid" % char)


class Sequence(models.Model):
    raw_sequence = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    fasta_header = models.CharField(max_length=1000, default="")
    user = models.ForeignKey('registration.User', on_delete=models.CASCADE)
    sequences = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class DNASequence(Sequence):
    pass


class ProteinSequence(Sequence):
    pass
