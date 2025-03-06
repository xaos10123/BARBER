from django.urls import path

from main.views import MainPageView, ReviewCreateView, ThanksView, VisitListView

app_name = 'main'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('visits/', VisitListView.as_view(), name='visit_list'),
    path('review/create/', ReviewCreateView.as_view(), name='review_create')
]