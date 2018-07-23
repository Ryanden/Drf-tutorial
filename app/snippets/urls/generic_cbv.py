from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import generic_cbv as views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='Snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='Snippet-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
