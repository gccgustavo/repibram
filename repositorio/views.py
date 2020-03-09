from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Arquivo

class ArquivoView(TemplateView):
    template_name = "arquivo_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['arquivos'] = Arquivo.objects.all()
        return context
