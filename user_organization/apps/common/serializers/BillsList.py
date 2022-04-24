from rest_framework import serializers

from user_organization.apps.common import models



class BillOrganizationSerializer(serializers.ModelSerializer):
    client_name= serializers.CharField()
    organization_name = serializers.CharField()

    class Meta:
        model = models.Bill
        exclude = ()