from django.urls import path

from . import upload

urlpatterns = [
    path(
        'upload-clients-organizations/',
        upload.UploadOrganizationClients.as_view(),
        name='upload_clients_organizations'
    ),
    path(
        'clients-organizations/',
        upload.UploadOrganizationClients.as_view(),
        name='clients_organizations_form'
    ),
    path(
        'upload-bills/',
        upload.BillsUpload.as_view(),
        name='upload_bills'
    ),
    path(
        'bills-page/',
        upload.BillsUpload.as_view(),
        name='bills_form'
    ),
]