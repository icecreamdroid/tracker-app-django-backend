from django_filters import rest_framework as filters
# from django.db.models.functions import KeyTransform
from .models import Log
import datetime



class LogFilter(filters.FilterSet):

    date = filters.DateFromToRangeFilter(
        field_name='log__now', method='filter_by_date')

    def filter_by_date(self, queryset, name, value):
        date_from = value.start
        date_to = value.stop

        return queryset.filter(log__now__range=(date_from, date_to))

    class Meta:
        model = Log
        fields = ['date']
