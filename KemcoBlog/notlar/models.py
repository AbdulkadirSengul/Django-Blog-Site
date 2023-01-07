from django.db import models

# Create your models here.
class Notlar(models.Model):
    author_nt = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title_nt = models.CharField(max_length=50, verbose_name="Başlık")
    content_nt = models.TextField(verbose_name="İçerik")
    created_date_nt = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    not_image = models.FileField(blank = True, verbose_name="Nota Foto Ekleyin")
    def __str__(self):
        return self.title_nt
