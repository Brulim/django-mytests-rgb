from django.urls import path
from . import views

urlpatterns = [
    path('rgb/', TemplateView.as_view(template_name="rgb/index.html")),
]