# Generated by Django 3.1 on 2020-09-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_processeddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='processeddata',
            name='image_data',
            field=models.TextField(default=''),
        ),
    ]