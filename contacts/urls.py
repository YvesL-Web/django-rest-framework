from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact/',views.contact, name = 'contact'),
    path('delete/<int:pk>', views.delete_contact, name="delete")
]