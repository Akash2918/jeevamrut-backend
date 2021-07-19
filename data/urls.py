from .views import DataViewSet
from django.urls import path, include

urlpatterns = [
    path('all/', DataViewSet.as_view(), name='all_data'),
]
