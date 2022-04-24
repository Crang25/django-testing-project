from django import forms


class ClientFilterForm(forms.Form):
    client_name = forms.CharField(max_length=255, required=False)