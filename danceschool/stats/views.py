from django.views.generic import TemplateView
from django.db.models import Count
from django.utils import timezone

from datetime import datetime
import six
from braces.views import PermissionRequiredMixin

from danceschool.core.models import Instructor, SeriesTeacher, Customer
from danceschool.core.utils.timezone import ensure_timezone

if six.PY3:
    # Ensures that checks for Unicode data types (and unicode type assignments) do not break.
    unicode = str


class SchoolStatsView(PermissionRequiredMixin, TemplateView):
    template_name = 'stats/schoolstats.html'
    permission_required = 'core.view_school_stats'

    def get_context_data(self, **kwargs):
        from .stats import getGeneralStats

        request = self.request
        context_data = kwargs

        (totalStudents,numSeries,totalSeriesRegs,totalTime) = getGeneralStats(request)

        context_data.update({
            'totalStudents':totalStudents,
            'numSeries':numSeries,
            'totalSeriesRegs':totalSeriesRegs,
            'totalTime':totalTime,
        })
        return context_data
