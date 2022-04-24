from django.db.models import Count, Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_organization.apps.common import models

@api_view()
def get_clients_table(request):


    qs = models.Client.objects.prefetch_related('organizations__organization')\
        .prefetch_related('organizations__organization__bills')\
        .all()\
        .annotate(
            organizations_count=Count('organizations'),
            bills_summ=Sum('organizations__organization__bills__bill__sum')
        )

    for client in qs:
        print(f'client: {client.name}, {client.organizations_count}, {client.bills_summ}')

    return Response({
        'ok': True
    })