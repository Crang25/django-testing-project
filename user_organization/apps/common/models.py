from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name



class Organization(models.Model):

    name = models.CharField(max_length=255, primary_key=True)


    def __str__(self):
        return self.name



class ClientOrganization(models.Model):

    client = models.ForeignKey(
        Client,
        related_name='organizations',
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        Organization,
        related_name='clients',
        on_delete=models.CASCADE
    )

    
    def __str__(self):
        return f'client: {self.client_id}, organization: {self.organization_id}'



class Bill(models.Model):

    number = models.IntegerField(primary_key=True)
    sum = models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return f'{self.number}'



class BillOrganization(models.Model):
    
    bill = models.ForeignKey(
        Bill,
        related_name='organizations',
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        Organization,
        related_name='bills',
        on_delete=models.CASCADE
    )