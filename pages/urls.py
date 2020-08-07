from django.urls import path

from .views import HomePageView, AboutPageView,  ElementsPageView,\
     GalleryPageView,list_items,ExcavationPageView, SnowView,CommercialPavingAsphaltView,\
         ResidentialPavingPageView, DemoPageView,LandScapingPageView, ConcretePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('elements/', ElementsPageView.as_view(), name='elements'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('excavation/', ExcavationPageView.as_view(), name='excavation'),
    path('snow/', SnowView.as_view(), name='snow'),
    path('residentialpaving/', ResidentialPavingPageView.as_view(), name='ResidentialPaving'),
    path('commercialpavingAsphalt/', CommercialPavingAsphaltView.as_view(), name='commercialpavingAsphalt'),
    path('demo/', DemoPageView.as_view(), name='demolition'),
    path('ladnscaping/', LandScapingPageView.as_view(), name='landscaping'),

    path('concrete/', ConcretePageView.as_view(), name='concrete'),


]
