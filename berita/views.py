from django.shortcuts import render, get_object_or_404, redirect
from .models import Berita, Kategori

def daftar_berita(request):
    berita_list = Berita.objects.filter(status='published').order_by('-tanggal_publish')[:6]
    berita_pilihan = Berita.objects.filter(pilihan=True, status='published')[:5]
    return render(request, 'berita/daftar_berita.html', {'berita_list': berita_list, 'berita_pilihan': berita_pilihan})

def berita_per_kategori(request, kategori_slug):
    kategori = get_object_or_404(Kategori, slug__iexact=kategori_slug)
    if kategori_slug.lower() == "home":
        return redirect('berita:daftar')
    berita_list = Berita.objects.filter(kategori=kategori, status='published').order_by('-tanggal_publish')
    return render(request, 'berita/daftar_berita.html', {
        'berita_list': berita_list,
        'kategori': kategori
    })

def detail_berita(request, slug):
    berita = get_object_or_404(Berita, slug=slug)
    return render(request, 'berita/detail_berita.html', {'berita': berita})

def cari_berita(request):
    query = request.GET.get('q')
    hasil = Berita.objects.filter(judul__icontains=query)
    return render(request, 'berita/cari.html', {
        'query': query,
        'hasil': hasil
    })

def tentang(request):
    return render(request, 'berita/tentang.html')

def redaksi(request):
    return render(request, 'berita/redaksi.html')

def kode_etik(request):
    return render(request, 'berita/kode_etik.html')

def pedoman(request):
    return render(request, 'berita/pedoman.html')

def kontak(request):
    return render(request, 'berita/kontak.html')