# Generated by Django 5.2.4 on 2025-07-21 02:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('isi', models.TextField()),
                ('gambar', models.ImageField(upload_to='gambar/')),
                ('tanggal_publish', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berita.kategori')),
            ],
        ),
    ]
