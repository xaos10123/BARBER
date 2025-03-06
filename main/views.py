from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from main.forms import ReviewForm, VisitForm
from main.models import Master, Service, Visit

MENU = [
    {"title": "Главная", "url": reverse_lazy("main:main_page")},
    {'title': 'Мастера', 'url': '#masters'},
    {'title': 'Услуги', 'url': '#services'},
    {'title': 'Записи', 'url': reverse_lazy("main:visit_list")},
    {'title': 'Отзыв', 'url': reverse_lazy("main:review_create")},
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
    template_name = 'main/include_visit_list.html'
    context_object_name = 'visits'
    paginate_by = 5

    def get_queryset(self):
        queryset = Visit.objects.all().order_by('-created_at')


        search_query = self.request.GET.get('q', '')
        master_id = self.request.GET.get('master', '')

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(phone__icontains=search_query))

        if master_id:
            queryset = queryset.filter(master_id=master_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        context['masters'] = Master.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_master'] = self.request.GET.get('master', '')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)


class ReviewCreateView(CreateView):
    template_name = 'main/include_review_form.html'
    form_class = ReviewForm
    success_url = '/#reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context
    
