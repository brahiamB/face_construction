from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Images
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'pages/main.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ExcavationPageView(TemplateView):
    template_name = 'pages/excavation.html'

class DemoPageView(TemplateView):
    template_name = 'pages/demo.html'

class ResidentialPavingPageView(TemplateView):
    template_name = 'pages/residential_paving.html'
class CommercialPavingAsphaltView(TemplateView):
    template_name = 'pages/commercial_paving_asphalt.html'


class SnowView(TemplateView):
    template_name = 'pages/snow.html'
class ElementsPageView(TemplateView):
    template_name = 'pages/elements.html'

class LandScapingPageView(TemplateView):
    template_name = 'pages/landscaping.html'


class GalleryPageView(ListView):
    model = Images
    template_name = 'pages/gallery.html'

def list_items(request):
        queryset = Images.objects.all()
        context = {
            'object_list':queryset
            
        }
        return render(request,"pages/gallery.html",context)


class ConcretePageView(ListView):
    model = Images
    template_name = 'pages/concrete_paving.html'