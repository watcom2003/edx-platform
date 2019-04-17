""" Program Enrollments API v1 URLs. """
from django.conf import settings
from django.conf.urls import url

from lms.djangoapps.program_enrollments.api.v1 import ProgramEnrollmentsView


app_name = 'lms.djangoapps.program_enrollments'

urlpatterns = [
    url(
        r'^programs/{program_key}/enrollments/$', #.format(course_id=settings.COURSE_ID_PATTERN),
        ProgramEnollmentsView.as_view(),
        name='course_grades'
    ),
]
