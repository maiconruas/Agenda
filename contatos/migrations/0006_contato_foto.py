# Generated by Django 2.2.3 on 2022-02-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
