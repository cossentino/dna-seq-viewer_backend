import pdb
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_sequence(seq_string):
    for char in seq_string:
        if char not in ['A', 'T', 'C', 'G']:
            raise ValidationError(
                "We came across a character %s that is not valid" % char)


def parse_fasta(fasta_string):
    header = ""
    i = 0
    while not fasta_string[i] == "\n":
        header += fasta_string[i]
        i += 1
    sequence = fasta_string[i + 1:]
    return (header, sequence)


class DNASequence(models.Model):
    raw_sequence = models.TextField(default="", validators=[validate_sequence])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    sequences = models.Manager()

    def __str__(self):
        return self.name


class ProteinSequence(models.Model):
    raw_sequence = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
