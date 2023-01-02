from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Create your tests here.

class testListCreateToDo(APITestCase):

    def testCreateToDo(self):
        sample_toDo = {'id': 1, 'Title': 'go to workstation', 'Decription': 'go to workstation at 7am',
        'Date': '2022-10-25', 'compeleted': 'false'}
        response = self.client.post(reverse('ListCreateToDo'),sample_toDo) #ListCreateToDo = path name
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

