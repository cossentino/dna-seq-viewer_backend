# Generated by Django 3.2.5 on 2021-08-06 15:11

from django.db import migrations, models
import django.db.models.manager
import dna_sequence.models


class Migration(migrations.Migration):

    dependencies = [
        ('dna_sequence', '0003_proteinsequence'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='dnasequence',
            managers=[
                ('sequences', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='dnasequence',
            name='fasta_header',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='dnasequence',
            name='raw_sequence',
            field=models.TextField(default=''),
        ),
    ]
