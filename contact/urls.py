
from django.urls import path
from contact.views import index, contact, search, create, delete

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    
    # contact (CRUD)
    path('<int:contact_id>/detail/', contact, name='contact'),
    path('create/', create, name='create'),
    path('<int:contact_id>/delete/', delete, name='delete'),
    # path('<int:contact_id>/update/', update, name='update'),
    # path('<int:contact_id>/delete/', delete, name='delete'),
]
