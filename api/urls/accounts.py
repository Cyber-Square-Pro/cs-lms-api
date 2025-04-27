from django.urls import path
from api.views  import accounts

urlpatterns = [
    path('admin/staff/create/', accounts.add_staff),
 
]
