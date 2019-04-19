"""Tests of openedx.features.discounts.views"""
# -*- coding: utf-8 -*-
import jwt

from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from student.tests.factories import UserFactory
from xmodule.modulestore.tests.factories import CourseFactory
from rest_framework.test import APIRequestFactory

from openedx.features.discounts.views import CourseUserDiscount


class TestCourseUserDiscount(ModuleStoreTestCase):
    """
    CourseUserDiscount should return a jwt with the information if this combination of user and 
    course can receive a discount, and how much that discount should be.
    """

    def setUp(self):
        super(TestCourseUserDiscount, self).setUp()
        self.user = UserFactory.create()
        self.course = CourseFactory.create(run='test', display_name='test')
        self.request_factory = APIRequestFactory()

    def test_course_user_discount(self):
        """
        Test that the api returns a jwt with the discount information
        """
        fake_request = self.request_factory.get('')
        fake_request.user = self.user
        response = CourseUserDiscount.as_view()(fake_request)
        self.assertEqual(response.status_code, 200)
        
        expected_payload = {'discount_applicable': False, 'discount_percent': 15}
        response_payload = jwt.decode(response.data, verify=False)
        self.assertTrue(all(item in response_payload.items() for item in expected_payload.items()))

