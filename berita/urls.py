from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'berita'

urlpatterns = [
    path('', views.daftar_berita, name='daftar'),
    path('favicon.ico', RedirectView.as_view(url='/static/logo/favicon.ico')),
    path('cari/', views.cari_berita, name='cari'),
    path('tentang/', views.tentang, name='tentang'),
    path('redaksi/', views.redaksi, name='redaksi'),
    path('kode-etik/', views.kode_etik, name='kode_etik'),
    path('pedoman-media-cyber/', views.pedoman, name='pedoman'),
    path('kontak/', views.kontak, name='kontak'),
    path('kategori/<slug:kategori_slug>/', views.berita_per_kategori, name='kategori'),
    path('<slug:slug>/', views.detail_berita, name='detail'),
]