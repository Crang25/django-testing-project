from django.db.models import F
from django_filters import CharFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from user_organization.apps.common import models
from user_organization.apps.common.serializers import BillsList
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from user_organization.apps.common.forms import client_filter_form, organization_filter_form


class CustomFilter(FilterSet):
    client_name = CharFilter(field_name='client_name', method='get_client_name')
    organization_name = CharFilter(field_name='organization_name', method='get_organization_name')

    class Meta:
        model = models.Bill
        fields = ('client_name', 'organization_name')


    @staticmethod
    def get_client_name(qs, name, value):
        return qs.annotate(
                    client_name=F('organizations__organization__clients__client_id')
                ).filter(client_name=value)

    
    @staticmethod
    def get_organization_name(qs, name, value):
        return qs.annotate(
                    organization_name=F('organizations__organization_id')
                ).filter(organization_name=value)



class BillsListView(ListAPIView):
    queryset = models.Bill.objects.all()\
        .prefetch_related('organizations__organization')\
            .prefetch_related('organizations__organization__clients__client')\
                .annotate(
                    client_name=F('organizations__organization__clients__client_id'),
                    organization_name=F('organizations__organization_id')
                )


    serializer_class = BillsList.BillOrganizationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CustomFilter
    renderer_classes = [TemplateHTMLRenderer]


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        client_form = client_filter_form.ClientFilterForm(request.data)
        organization_form = organization_filter_form.OrganizationFilterForm(request.data)

        return Response({
            'bills': serializer.data,
            'client_form': client_form,
            'organization_form': organization_form,
        }, template_name='bills_table.html')
