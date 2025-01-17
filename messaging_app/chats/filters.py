import django_filters
from .models import Message
from django.utils import timezone

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name='sender__username', lookup_expr='icontains')
    created_at_min = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_max = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'created_at_min', 'created_at_max']