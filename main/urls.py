from django.urls import path

from main.views import MainPageView, ThanksView

app_name = 'main'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]