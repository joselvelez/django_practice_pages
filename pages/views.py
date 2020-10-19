from django.shortcuts import render
from django.views.generic import TemplateView

# Page 46 of django for beginners

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'