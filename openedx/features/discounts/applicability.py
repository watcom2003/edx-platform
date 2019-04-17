# -*- coding: utf-8 -*-
"""
Contains code related to computing discount percentage
and discount applicability.
"""
from openedx.core.djangoapps.waffle_utils import WaffleFlag, WaffleFlagNamespace

# .. feature_toggle_name: discounts.enable_discounting
# .. feature_toggle_type: flag
# .. feature_toggle_default: False
# .. feature_toggle_description: Toggle discounts always being disabled
# .. feature_toggle_category: discounts
# .. feature_toggle_use_cases: monitored_rollout
# .. feature_toggle_creation_date: 2019-4-16
# .. feature_toggle_expiration_date: None
# .. feature_toggle_warnings: None
# .. feature_toggle_tickets: REVEM-282
# .. feature_toggle_status: supported
DISCOUNT_APPLICABILITY_FLAG = WaffleFlag(
    waffle_namespace=WaffleFlagNamespace(name=u'discounts'),
    flag_name=u'enable_discounting',
    flag_undefined_default=False
)


def can_recieve_discount(user, course):
    if not DISCOUNT_APPLICABILITY_FLAG.is_enabled():
        return False