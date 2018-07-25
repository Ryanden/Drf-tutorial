from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from ..models import Snippet
from ..serializers import (
    SnippetDetailSerializer,
    SnippetListSerializer,
)
from ..serializers.users import UserListSerializer

from ..serializers.pagination import LargeResultsSetPagination

User = get_user_model()

__all__ = (
    'SnippetList',
    'SnippetDetail',
    'UserList',
    'UserDetail',
)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        # GET, POST요청 (List, Create)시마다 다른 Serializer를 쓰도록
        # get_serializer_class()를 재정의
        if self.request.method == 'GET':
            return SnippetListSerializer
        elif self.request.method == 'POST':
            return SnippetDetailSerializer

    def perform_create(self, serializer):
        # SnippetListSerializer로 전달받은 데이터에
        # 'owner'항목에 self.request.user데이터를 추가한 후
        # save() 호출, DB에 저장 및 인스턴스 반환
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetDetailSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class SnippetPagination(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class =