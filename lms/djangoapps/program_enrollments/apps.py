# -*- coding: utf-8 -*-
"""
ProgramEnrollments Application Configuration
"""
from __future__ import unicode_literals

from django.apps import AppConfig


class ProgramEnrollmentsConfig(AppConfig):
    """
    Application configuration for ProgramEnrollment
    """
    name = 'lms.djangoapps.program_enrollments'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: u'programs_api',
                PluginURLs.REGEX: u'api/',
                PluginURLs.RELATIVE_PATH: u'api.urls',
            }
        },
    }
