import random

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.test import APIRequestFactory

import json

from .models import Snippet


class SnippetListTest(APITestCase):
    """
    Snippet List 요청에 대한 테스트
    """

    def test_status_code(self):
        """
        요청 결과의 HTTP 상태 코드가 200인지 확인
        :return:
        """

        response = self.client.get('/snippets/django_view/snippets/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_snippet_list_count(self):
        """
        Snippet List 를 요청시 DB 에 있는 자료수와 같은 갯수가 리턴되는 테스트
        :return:
        """

        self.create_dummy_data()

        response = self.client.get('/snippets/django_view/snippets/')

        python_data = json.loads(response.content)

        self.assertEqual(len(python_data), Snippet.objects.count())

    def create_dummy_data(self):

        [Snippet.objects.create(code=f'a = {i}') for i in range(random.randint(5, 10))]

    def test_snippet_list_order_by_created_descending(self):
        """
        Snippet List 의 결과가 생성일자 내림차순인지 확인
        :return:
        """

        self.create_dummy_data()

        response = self.client.get('/snippets/django_view/snippets/')

        python_data = json.loads(response.content)

        # print(Snippet.objects.values_list('pk', flat=True).order_by('-pk'))

        # print(Snippet.objects.order_by('-created').values_list('pk', flat=True))

        self.assertEqual(
            [item['pk'] for item in python_data],
            list(Snippet.objects.order_by('-created').values_list('pk', flat=True))
        )


class SnippetCreateTest(APIRequestFactory):

    def test_snippet_create_status_code(self):
        """
        201이 돌아오는지
        :return:
        """
        pass

    def test_snippet_create_save_db(self):
        """
        요청 후 실제 DB 에 저장 되었는지
        :return:
        """
        pass

    def test_snippet_create_missing_code_raise_exception(self):
        """
        'code'에 데이터가 주어지지 않으 경우 적절한 Exception 이 발생 하는지
        :return:
        """
        pass