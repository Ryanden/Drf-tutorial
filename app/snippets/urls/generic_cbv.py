from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import generic_cbv as views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-List'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


urlpatterns = format_suffix_patterns(urlpatterns)
