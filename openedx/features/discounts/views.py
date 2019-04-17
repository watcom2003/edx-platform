"""
The Discount API Views should return information about discounts that apply to the user and course.

"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .applicability import can_recieve_discount

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import SessionAuthenticationAllowInactiveUser

from openedx.core.djangoapps.oauth_dispatch.jwt import create_jwt_for_user
from openedx.core.lib.api.authentication import OAuth2AuthenticationAllowInactiveUser
from openedx.core.lib.api.permissions import ApiKeyHeaderPermissionIsAuthenticated
from openedx.core.lib.api.view_utils import DeveloperErrorViewMixin

from rest_framework.response import Response
from rest_framework.views import APIView



class CourseUserDiscount(DeveloperErrorViewMixin, APIView):
    """
    **Use Cases**

        Request discount information for a user and course

    **Example Requests**

        GET /api/discounts/v1/course/{course_key}

    **Response Values**

        Body consists of the following fields:


    **Parameters:**

        username:
            The username of the specified user for whom the discount data
            is being accessed.
        auth_token:
            Token used to sign the jwt that is returned.

    **Returns**

        * 200 on success with above fields.
        * 400 if an invalid parameter was sent or the username was not provided
          for an authenticated request.
        * 403 if a user who does not have permission to masquerade as
          another user specifies a username other than their own.
        * 404 if the course is not available or cannot be seen.

        Example response:
        {
            "discount_applicable": false,
            "discount_percent": 0
        }
    """
    authentication_classes = (JwtAuthentication, OAuth2AuthenticationAllowInactiveUser,
                              SessionAuthenticationAllowInactiveUser,)
    permission_classes = ApiKeyHeaderPermissionIsAuthenticated,


    def get(self, request, course_key_string=None):
        """
        Return the discount percent, if the user has appropriate
        permissions.
        """
        username = request.GET.get('user', request.user.username)
        discount_applicable = can_recieve_discount(user=username, course=course_key_string)
        payload = {'discount_applicable': discount_applicable, 'discount_percent': 0}
        return Response({'jwt': create_jwt_for_user(request.user, additional_claims=payload),
                        'applicability':payload})