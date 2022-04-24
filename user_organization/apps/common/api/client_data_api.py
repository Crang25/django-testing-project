from django.db.models import Count, Sum
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

from user_organization.apps.common import models

@api_view()
@renderer_classes([TemplateHTMLRenderer])
def get_clients_table(request):

    qs = models.Client.objects.prefetch_related('organizations__organization')\
        .prefetch_related('organizations__organization__bills')\
        .all()\
        .annotate(
            organizations_count=Count('organizations'),
            bills_summ=Sum('organizations__organization__bills__bill__sum')
        ).values('name', 'organizations_count', 'bills_summ')

    return Response({
        'clients': list(qs)
    }, template_name='clients_table.html')