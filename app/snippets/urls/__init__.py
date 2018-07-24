
from django.urls import path, include
from . import django_view, api_view, mix_in, generic_cbv

app_name = 'snippets'

urlpatterns = [
    path('django_view/', include(django_view)),
    path('api_view/', include(api_view)),
    path('mix_in_view/', include(mix_in)),
    path('generic_cbv/', include(generic_cbv)),

]
