# Generated by Django 3.2.5 on 2021-08-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DNASequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_sequence', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=1000)),
                ('sequence_type', models.IntegerField(choices=[(1, 'Dna'), (2, 'Protein')], default=1)),
            ],
        ),
    ]
