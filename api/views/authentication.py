from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from db.models.user import Admin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import jwt


@api_view(['POST'])
def add_admin(request):
    try:
        name = request.data.get('name')
        user_name = request.data.get('userName')
        password = request.data.get('password')
        encryped_password = make_password(password)
        print(request.data)
        admin = Admin(name=name, user_name=user_name,
                      password=encryped_password)
        admin.save()
        return Response({'statusCode': 200, 'message': 'Admin created successfully'})
    except Exception as e:
        print(e)
        return Response({'statusCode': 500, 'message': 'Internal server error', 'error': str(e)})


@api_view(['POST'])
def login(request):

    try:
        user_type = request.data.get('userType')
        username = request.data.get('email')
        password = request.data.get('password')
        print(request.data)
        if user_type == "admin":
            record = Admin.objects.filter(
                user_name=username)
            print(record)
            if record.exists():
                if check_password(password, record[0].password):
                    payload = {
                        'id': record[0].id,
                        'username':  record[0].user_name,
                        'name':  record[0].name,
                    }

                    token = jwt.encode(
                        payload, settings.SECRET_KEY, algorithm='HS256')
                    return Response({'statusCode': 200, 'message': 'Login successful', 'token': token})
                 
                return Response({'statusCode': 409, 'message': 'Password Incorrect',}) 
            else:
                return Response({'statusCode': 404, 'message': 'User not found'})

    except Exception as e:
        return Response({'statusCode': 500, 'message': 'Internal server error', 'error': str(e)})
