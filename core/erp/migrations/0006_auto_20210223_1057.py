# Generated by Django 3.0.4 on 2021-02-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20210223_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mascot/%Y/%m/%d', verbose_name='Imagen Mascota'),
        ),
    ]