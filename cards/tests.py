from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
import time
from .serializers import CardSerializer

class CardValidationTest(APITestCase):
    def test_validation(self):
        fake = Faker()
        url = reverse('cards-list')


        # invalid card number length
        invalid_data = {
            'censored_number': '123456789012345',
            'ccv': '123',
        }
        invalid_serializer = CardSerializer(data=invalid_data)
        self.assertFalse(invalid_serializer.is_valid())

        # invalid ccv length
        invalid_data = {
            'censored_number': '1234567890123456',
            'ccv': '12',  
        }
        invalid_serializer = CardSerializer(data=invalid_data)
        self.assertFalse(invalid_serializer.is_valid())

        # invalid ccv value
        invalid_data = {
            'censored_number': '1234567890123456',
            'ccv': '9999', 
        }
        invalid_serializer = CardSerializer(data=invalid_data)
        self.assertFalse(invalid_serializer.is_valid())

        #timer  measuring the validation time
        timer = time.time()  
        
        #  100 random card numbers + cvv
        for _ in range(100):
            card_data = {
                'censored_number': fake.credit_card_number(card_type=None),
                'ccv': fake.credit_card_security_code(),
            }
            response = self.client.post(url, card_data)
            self.assertEqual(response.status_code, 400)  
        
        end_timer = time.time()  
        time_needed = end_timer - timer
        print(f"time for validation of 100 cards: {time_needed} seconds")