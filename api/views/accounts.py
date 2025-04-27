from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from db.models.user import Admin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer.user import StaffSerializer
from db.models import Staff
from django.conf import settings
import jwt


@api_view(['POST'])
def add_staff(request):

    try:

        email = request.data.get('email')
        record_exist = Staff.objects.filter(email=email).exists()

        if  record_exist:
            return Response({'statusCode': 502, 'message': 'Email already exists'})
            
        
        serializer = StaffSerializer(data = request.data)
        
        if serializer.is_valid():
            instance = serializer.save()
            payload = {
                    'id': instance.id,
                    'email':  instance.email,
                }

            token = jwt.encode(
                    payload, settings.SECRET_KEY, algorithm='HS256')
            
            return Response({'statusCode': 201, 'message': 'Account created successfully', 'token': token})
        else:
            print(serializer.errors)
    except Exception as e:
        print(e)
        return Response({'statusCode': 500, 'message': 'Internal server error', 'error': str(e)})
    