from django.contrib import admin
from .models import Berita, Kategori, BannerHeader, TextBerjalan, IklanSidebar

class BeritaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("judul",)}
    list_display = ('judul', 'penulis', 'status', 'tanggal_publish', 'pilihan')
    list_filter = ('status', 'tanggal_publish', 'pilihan')
    search_fields = ('judul', 'isi')

@admin.register(TextBerjalan)
class TextBerjalanAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Hanya izinkan tambah jika belum ada satupun
        return not TextBerjalan.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Tidak boleh dihapus
        return False

admin.site.register(Berita, BeritaAdmin)
admin.site.register(Kategori)
admin.site.register(BannerHeader)
admin.site.register(IklanSidebar)

