from django import forms


class OrganizationFilterForm(forms.Form):
    organization_name = forms.CharField(max_length=255, required=False)