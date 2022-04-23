from django.urls import path

from . import upload

urlpatterns = [
    path(
        'clients-organizations/',
        upload.upload_clients_and_organizations
    ),
    path(
        'bills/',
        upload.upload_bills
    ),
]