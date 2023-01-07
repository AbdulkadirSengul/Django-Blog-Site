from django.db import models

# Create your models here.
class Proje(models.Model):
    author_prj = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Yazar")
    title_prj = models.CharField(max_length=50, verbose_name="Baslık")
    content_prj = models.TextField( verbose_name="İçerik")
    created_date_ptj = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulduğu tarih")
    proje_image = models.FileField(blank=True, verbose_name="Projeye Foto EKLE")

    def __str__(self):
        return self.title_prj
