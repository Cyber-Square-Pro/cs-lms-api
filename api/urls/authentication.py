from django.urls import path
from api.views  import authentication

urlpatterns = [
    path('user/login/', authentication.login),
    path('admin/add/', authentication.add_admin),
]
