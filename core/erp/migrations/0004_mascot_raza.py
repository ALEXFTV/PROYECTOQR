# Generated by Django 3.0.4 on 2021-02-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20210219_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascot',
            name='raza',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Raza'),
        ),
    ]
