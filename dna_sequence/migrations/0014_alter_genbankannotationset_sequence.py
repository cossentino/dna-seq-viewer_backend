# Generated by Django 3.2.5 on 2021-08-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dna_sequence', '0013_alter_genbankannotationset_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genbankannotationset',
            name='sequence',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='dna_sequence.sequence'),
        ),
    ]
