from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    isi = RichTextField()
    gambar = models.ImageField(upload_to='gambar/')
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ], default='draft')
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    pilihan = models.BooleanField(default=False)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.judul
    
class BannerHeader(models.Model):
    judul = models.CharField(max_length=100, blank=True)
    gambar = models.ImageField(upload_to='banner/')
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.judul or f"Banner {self.id}"

class TextBerjalan(models.Model):
    isi = models.TextField("Teks Berjalan")

    def __str__(self):
        return "Teks Berjalan"

class IklanSidebar(models.Model):
    judul = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='iklan/')
    link = models.URLField(blank=True, null=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.judul