from django.shortcuts import render
from django.views.generic import CreateView

from main.forms import VisitForm

MENU = [
    {"title": "Главная", "url": "main_page"},
    {'title': 'Мастера', 'url': '#masters'},
    {'title': 'Услуги', 'url': '#services'},
    {'title': 'Запись на стрижку', 'url': '#orderForm'},
]

class MainPageView(CreateView):
    template_name = "main/index.html"
    form_class = VisitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU
        return context
    
