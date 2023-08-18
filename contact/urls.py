
from django.urls import path
from contact.views import index, contact

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('<int:contact_id>/', contact, name='contact'),
]
