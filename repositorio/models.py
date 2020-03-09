from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Arquivo(models.Model):
    class Meta:
        verbose_name_plural = "Arquivos"
        ordering = ['nome']
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.dono.id, filename)

    dono = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    convidados = models.ManyToManyField(User, related_name='rconvidados', blank=True)
    nome = models.CharField(max_length=10, blank=True, null=True)

    arquivos = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return  self.arquivos.url




