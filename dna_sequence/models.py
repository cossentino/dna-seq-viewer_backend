"""Models for NGS sequencing data"""
import pdb
from django.db import models
from dna_seq_viewer.core.services.filter import Filter

# Create your models here.


class Sequence(models.Model, Filter):

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
    input_file_format = models.CharField("", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    seq_type = models.CharField(
        max_length=10, choices=SEQUENCE_CHOICES, default=DNA)
    user = models.ForeignKey('registration.User', on_delete=models.CASCADE)

    # Fields for FASTA only

    header = models.CharField(default="", max_length=1000)
    accession = models.CharField(default="", max_length=50)
    organism = models.CharField(default="", max_length=100)

    def __str__(self):
        return str(self.name)


class GenBankAnnotationSet(models.Model, Filter):
    """Dictionary-like objects for holding GenBank file annotations"""
    molecule_type = models.CharField(default="", max_length=50)
    topology = models.CharField(default="", max_length=50)
    data_file_division = models.CharField(default="", max_length=50)
    date = models.CharField(default="", max_length=50)
    # List
    accessions = models.JSONField(default=str)
    sequence_version = models.IntegerField(blank=True)
    gi = models.CharField(default="", max_length=50)
    # List
    keywords = models.JSONField(default=str)
    source = models.CharField(default="", max_length=100)
    organism = models.CharField(default="", max_length=100)
    # List
    taxonomy = models.JSONField(default=str)
    sequence = models.ForeignKey(
        "Sequence", on_delete=models.CASCADE, default=2, related_name="annotations")


class SequenceFeature(models.Model, Filter):
    """Corresponds to BioPython SeqFeature, simplified for easy database storage"""

    sequence = models.ForeignKey(
        "Sequence", on_delete=models.CASCADE, default=2, related_name="features")
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    feature_type = models.CharField(default="", max_length=50)
    note = models.CharField(default="", max_length=1000)
    db_xref = models.JSONField(default=str)
