from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from main.forms import VisitForm
from main.models import Master, Service

MENU = [
    {"title": "Главная", "url": "#main_page"},
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
        context["masters"] = Master.objects.all()
        context['services'] = Service.objects.all()

        return context
    
class ThanksView(TemplateView):
    template_name = 'main/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU
        return context
    
    class VisitListView(ListView):
    model = Visit
    template_name = 'visit_list.html'
    context_object_name = 'visits'
    paginate_by = 5

    def get_queryset(self):
        """Формируем QuerySet с учетом поиска и фильтрации по мастеру"""
        queryset = Visit.objects.all().order_by('-created_at')

        # Получаем параметры из GET-запроса
        search_query = self.request.GET.get('q', '')
        master_id = self.request.GET.get('master', '')

        # Фильтрация по поисковому запросу (имя или телефон)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(phone__icontains=search_query))

        # Фильтрация по мастеру
        if master_id:
            queryset = queryset.filter(master_id=master_id)

        return queryset

    def get_context_data(self, **kwargs):
        """Добавляем в контекст список мастеров и текущие фильтры"""
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_master'] = self.request.GET.get('master', '')
        return context

    def dispatch(self, request, *args, **kwargs):
        """Запрещаем доступ не-администраторам"""
        if not request.user.is_staff:
            return redirect('main_page')  # Перенаправляем на главную
        return super().dispatch(request, *args, **kwargs)


class ReviewCreateView(CreateView):
    template_name = 'review_form.html'
    form_class = ReviewForm
    success_url = '/#reviews'  # Редирект на секцию с отзывами

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context
    
