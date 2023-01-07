# Generated by Django 4.1.3 on 2023-01-02 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_nt', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content_nt', models.TextField(verbose_name='İçerik')),
                ('created_date_nt', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('not_image', models.FileField(blank=True, upload_to='', verbose_name='Nota Foto Ekleyin')),
                ('author_nt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
    ]