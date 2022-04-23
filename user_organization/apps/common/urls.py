from django.urls import include, path

urlpatterns = [
    path('api/', include('user_organization.apps.common.api.urls'), name='api'),
]