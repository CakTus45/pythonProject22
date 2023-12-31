# Generated by Django 4.2.3 on 2023-08-20 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default=None, upload_to='advertisments', verbose_name='изображение'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='advertisements',
        ),
    ]
