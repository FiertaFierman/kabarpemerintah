from django.urls import path
from . import views

app_name = 'berita'

urlpatterns = [
    path('', views.daftar_berita, name='daftar'),
    path('cari/', views.cari_berita, name='cari'),
    path('<int:berita_id>/', views.detail_berita, name='detail'),
    path('<slug:kategori_slug>/', views.berita_per_kategori, name='kategori'),
    path('tentang/', views.tentang, name='tentang'),
    path('redaksi/', views.redaksi, name='redaksi'),
    path('kode-etik/', views.kode_etik, name='kode_etik'),
    path('pedoman-media-cyber/', views.pedoman, name='pedoman'),
    path('kontak/', views.kontak, name='kontak'),
]