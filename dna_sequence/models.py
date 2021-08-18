"""Models for NGS sequencing data"""
from django.db import models

# Create your models here.


class Sequence(models.Model):

    """Abstract sequence model - parent for DNA/Protein Sequence models"""

    DNA = 'D'
    RNA = 'R'
    PEPTIDE = 'P'

    SEQUENCE_CHOICES = [
        (DNA, 'dna'),
        (RNA, 'rna'),
        (PEPTIDE, 'peptide')
    ]

    seq = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000, default="")
    seq_type = models.CharField(
        max_length=10, choices=SEQUENCE_CHOICES, default=DNA)
    user = models.ForeignKey('registration.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True


class GenBankSequence(Sequence):
    """GenBank protein/nucleotide sequence"""


class GenBankAnnotationSet(models.Model):
    """Dictionary-like objects for holding GenBank file annotations"""
    seq = models.ForeignKey('GenBankSequence', on_delete=models.CASCADE)
    molecule_type = models.CharField("", max_length=50)
    topology = models.CharField("", max_length=50)
    date = models.CharField("", max_length=50)
    gi = models.CharField("", max_length=50)
    organism = models.CharField(max_length=1000)


class FastaSequence(Sequence):
    """Fasta protein/nucleotide sequence"""

    header = models.CharField("", max_length=1000)
    accession = models.CharField("", max_length=50)
    organism = models.CharField(max_length=100)
