# -*- coding: utf-8 -*-
"""
ProgramEnrollment Views
"""
from __future__ import unicode_literals

from django.http import HttpResponse

class ProgramEnrollmentsView(APIView):
    """
    POST view for ProgramEnrollments
    """

    def post(self, request, *args, **kwargs):
        return HttpResponse('result')