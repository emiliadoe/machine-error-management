# Generated by Django 5.1.1 on 2024-10-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_errorcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]