from django.test import TestCase
from .models import Contribution

class ContributionTestCase(TestCase):
    def setUp(self):
        # Create test data for the Contribution model
        Contribution.objects.create(amount=100.0, contributor_email="test@example.com")
        Contribution.objects.create(amount=200.0, contributor_email="test2@example.com")

    def test_contributions_exist(self):
        contribution1 = Contribution.objects.get(contributor_email="test@example.com")
        contribution2 = Contribution.objects.get(contributor_email="test2@example.com")

        self.assertEqual(contribution1.amount, 100.0)
        self.assertEqual(contribution2.amount, 200.0)
