from .models import Kategori, BannerHeader, TextBerjalan, IklanSidebar

def kategori_context(request):
    return {
        'daftar_kategori': Kategori.objects.all()
    }

def banner_header(request):
    banner = BannerHeader.objects.filter(aktif=True).first()
    return {'banner': banner}

def teks_berjalan_context(request):
    teks = TextBerjalan.objects.first()
    return {'teks_berjalan': teks}

def iklan_sidebar_context(request):
    return {
        'iklan_sidebar': IklanSidebar.objects.filter(aktif=True)
    }