# Generated by Django 3.2.5 on 2021-08-13 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dna_sequence', '0005_auto_20210806_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnasequence',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proteinsequence',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.user'),
            preserve_default=False,
        ),
    ]
