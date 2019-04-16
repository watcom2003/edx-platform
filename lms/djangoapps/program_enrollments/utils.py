"""
utility functions for program enrollments
"""
import logging
from openedx.core.djangoapps.catalog.utils import get_programs
from organizations.models import Organization
from social_django.models import UserSocialAuth

log = logging.getLogger(__name__)


class UserLookupException(Exception):
    pass


class ProgramDoesNotExistException(UserLookupException):
    pass


class OrganizationDoesNotExistException(UserLookupException):
    pass


class ProviderDoesNotExistException(UserLookupException):
    pass


def get_platform_user(external_user_id, program_uuid):
    """
    Returns a User model for an external_user_id mapping to a social auth entry.

    This function looks at a programs authoring_organization, finds a matching SAML Provider, and finally looks
    for a social auth entry corresponding to the provided exernal id.

    Args:
        external_user_id: external user id used for social auth
        program_uuid: a program this user is/will be enrolled in

    Returns:
        A User object.

    Raises:
        ProgramDoesNotExistException if no such program exists.
        OrganizationDoesNotExistException if no organization exists.
        ProviderDoesNotExistException if there is no SAML provider configured for the related organization.
    """

    program = get_programs(uuid=program_uuid)
    if program is None:
        log.error(u'Unable to find catalog program matching uuid [%s]', program_uuid)
        raise ProgramDoesNotExistException

    try:
        org_key = program['authoring_organizations'][0]['key']
    except (KeyError, IndexError):
        log.error(u'Cannot determine authoring organization key for catalog program [%s]')
        raise OrganizationDoesNotExistException

    try:
        organization = Organization.objects.get(short_name=org_key)
        provider_slug = organization.samlproviderconfig.provider_id.strip('saml-')
    except Organization.DoesNotExist:
        log.error(u'Unable to find organization for short_name [%s]', org_key)
        raise OrganizationDoesNotExistException
    except Organization.samlproviderconfig.RelatedObjectDoesNotExist:
        log.error(u'No SAML provider found for organization id [%s]', organization.id)
        raise ProviderDoesNotExistException

    try:
        return UserSocialAuth.objects.get(provider=provider_slug, uid=external_user_id).user
    except UserSocialAuth.DoesNotExist:
        return None
