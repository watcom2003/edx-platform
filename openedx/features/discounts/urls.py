"""
Discount API URLs
"""
from django.conf import settings
from django.conf.urls import include, url

from .views import CourseUserDiscount

urlpatterns = [
    url(r'^{}'.format(settings.COURSE_KEY_PATTERN), CourseUserDiscount.as_view(), name="discounts"),
]
