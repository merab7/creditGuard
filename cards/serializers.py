from rest_framework import serializers
from .models import Card
import sys
sys.set_int_max_str_digits(0)



class CardSerializer(serializers.ModelSerializer):

    card_number = serializers.CharField(write_only=True)
    ccv = serializers.CharField(write_only=True)
    censored_number = serializers.CharField(read_only=True)
    is_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = Card
        fields = ( 'user', 'title',   'card_number', 'ccv', 'censored_number', 'is_valid', 'date_created')



    #validate card_number
    def validate_card_number(self, value):
         
         if len(value) !=16:
            raise serializers.ValidationError(f'the count of curd numbers should be 16. instead it is {len(value)} ')
         for x in value:
            if not x.isnumeric():
                raise serializers.ValidationError('the numbers in card number should be in range (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)')
         return value  
    

    #validate ccv 
    def validate_ccv(self, value):
        if len(value) !=3 or int(value) not in range(100, 1000):
            raise serializers.ValidationError('cvv number should contain 3 character and should be in range 100-999')
        return value
    


    #checking if the card in general is valid
    def validate(self, data):
        
        card_number = data.get('card_number')
        ccv = data.get('ccv')
        result_card_number = []
        couple = []

        #getting form '1234567890'   this:   ['12', '34', '56', '78', '90']
        n=2
        modified_list = [card_number[i:i+n] for i in range(0, len(card_number), n)]
       
        for x in modified_list:
            couple.append(int(x))
            if len(couple) == 2:
                result_card_number.append(tuple(couple))
                couple.clear()

        #checking if the card is valid 
        #11^(22^3) % 103 if result value is even then it is valid else it is not
        for x in result_card_number:
            if ((list(x)[0]**(list(x)[1]**3)) % int(ccv)) % 2 != 0:
                raise serializers.ValidationError('this card is not valid check the card number and the cvv')
            

        # mask the card number with *****
        masked_value = card_number[:4] + '*' * (len(card_number) - 8) + card_number[-4:]

        # save the masked card number to the database
        data['censored_number'] = masked_value
        data.pop('card_number')
        data.pop('ccv')      
        data['is_valid'] = True

       
        return data





        
                




