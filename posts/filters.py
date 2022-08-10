from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget

from posts.models.like import Like


class LikeAnaliticsFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(
        field_name="date_created",
        widget=RangeWidget(attrs={"placeholder": "YYYY-MM-DD"}),
    )

    class Meta:
        model = Like
        fields = ["date"]
