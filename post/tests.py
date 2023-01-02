from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import DevStack


class GenericPostModelViewSetTest(APITestCase):
    '''post/views.py의 GenericPostModelViewSet이 정상적으로 동작하는지를 검증하는 테스트'''

    def setUp(self):
        ''' DevStack 생성, 회원가입 및 로그인 수행'''
        dev_tag=DevStack.objects.create(name="python")
        dev_tag.save()
        User = get_user_model()
        User.objects.create_user(
            email="test@test.com", first_name="test", last_name="user", password="0000"
        )
        self.client.login(email="test@test.com", password="0000")

        data = {
            "post_type": "ST",
            "meet_type": "ON",
            "location_info": "",
            "title": "test1",
            "content": "test1",
            "crew": [1],
            "dev_tag": [1]
        }
        self.client.post(reverse("post-list"), data, format="json")
        
    def test_posting_list(self):
        response = self.client.get(reverse("post-list"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_posting_update(self):
        update_data = {
            "title": "게시글 수정 테스트"
        }
        response = self.client.patch(reverse('post-detail', kwargs={'pk': 1}), update_data)
        print(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    def test_posting_detail(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    
        
