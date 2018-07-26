from django.urls import path, include
from . import django_view, api_view, mixins, generic_cbv, viewsets_router

app_name = 'snippets'

urlpatterns = [
    path('django_view/', include(django_view)),
    path('api_view/', include(api_view)),
    path('mixins_view/', include(mixins)),
    path('generic_cbv/', include(generic_cbv)),
    path('viewsets_router/', include(viewsets_router))

]
