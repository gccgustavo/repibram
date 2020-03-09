from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from repositorio.views import ArquivoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', ArquivoView.as_view(), name='listar_arquivos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
