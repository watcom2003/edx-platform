# -*- coding: utf-8 -*-
"""
ProgramEnrollment Views
"""
from __future__ import unicode_literals

import logging

from django.http import HttpResponse
from rest_framework.views import APIView

LOGGER = logging.getLogger(__name__)

class ProgramEnrollmentsView(APIView):
    """
    POST view for ProgramEnrollments
    """

    def get(self, request, *args, **kwargs):
        LOGGER.info('Rickie is the coolest ever')
        return HttpResponse('result')