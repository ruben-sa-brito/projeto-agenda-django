
from django.urls import path
from contact.views import index, contact, search

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('<int:contact_id>/', contact, name='contact'),
]
