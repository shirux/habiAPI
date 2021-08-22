import random

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from properties.views import PropertiesApi
from rest_framework import status
from django.test import SimpleTestCase

# Create your tests here.
class PropertyTest(SimpleTestCase):
    """Using the same scenario HABI.CO provided on database, we developed the next test.
    I will suggest to create a testing database, or using Django ORM (It will create an automatic database for testing)
    """

    def test_api_properties_get(self):
        """Test properties GET API Endpoint.

        Must assert the next conditions:
            - Response have 200 OK status
            - Response have more than 0 results
        """

        # Setup
        url = reverse("properties")
        request_factory = APIRequestFactory()

        # Request section
        request = request_factory.get(url, None, format="json")
        response = PropertiesApi.as_view()(request)

        # Assert with trending category
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data["data"]), 0)

    def test_api_properties_get_city_filter(self):
        """Test properties GET API endpoint city filter
        City filter must be applied.

        Must assert the next conditions:
            - Both responses have 200 OK status
            - Filter response must have more than 0 results
            - Filter response must have less results no filter response
        """

        # Setup
        url = reverse("properties")
        request_factory = APIRequestFactory()
        valid_cities = ["Bogota", "Medellin", "Barranquilla"]

        # Check array of valid cities
        for city in valid_cities:

            # Request section
            request = request_factory.get(url, None, format="json")
            response = PropertiesApi.as_view()(request)
            request = request_factory.get(url, {"city": city}, format="json")
            response_with_filter = PropertiesApi.as_view()(request)

            # Assert with trending category
            self.assertEqual(response_with_filter.status_code, status.HTTP_200_OK)
            self.assertGreater(len(response_with_filter.data["data"]), 0)
            self.assertGreater(len(response.data["data"]), len(response_with_filter.data["data"]))

    # Temporary disabled due to missing state property on database. Test scenario won't work
    # def test_api_properties_get_state_filter(self):
    #     """Test properties GET API endpoint state filter
        # State filter must be applied.

        # Must assert the next conditions:
        #     - Both responses have 200 OK status
        #     - Filter response must have more than 0 results
        #     - Filter response must have less results no filter response
        # """

    #     # Setup
    #     url = reverse("properties")
    #     request_factory = APIRequestFactory()
    #     valid_states = ["Bogota", "Atlantico", "Antioquia"]

    #     # Check array of valid states
    #     for state in valid_states:

        #     # Request section
        #     request = request_factory.get(url, None, format="json")
        #     response = PropertiesApi.as_view()(request)
        #     request = request_factory.get(url, {"state": state}, format="json")
        #     response_with_filter = PropertiesApi.as_view()(request)

        #     # Assert with trending category
        #     self.assertEqual(response_with_filter.status_code, status.HTTP_200_OK)
        #     self.assertGreater(len(response_with_filter.data["data"]), 0)
        #     self.assertGreater(len(response.data["data"]), len(response_with_filter.data["data"]))

    def test_api_properties_get_min_year_filter(self):
        """Test properties GET API endpoint min year filter
        Min year filter must be applied.

        Must assert the next conditions:
            - Both responses have 200 OK status
            - Filter response must have more than 0 results
            - Filter response must have less results no filter response
        """

        # Setup
        url = reverse("properties")
        request_factory = APIRequestFactory()
        valid_years = [2002, 2011, 2015]

        # Check array of valid years
        for year in valid_years:

            # Request section
            request = request_factory.get(url, None, format="json")
            response = PropertiesApi.as_view()(request)
            request = request_factory.get(url, {"min_year": year}, format="json")
            response_with_filter = PropertiesApi.as_view()(request)

            # Assert with trending category
            self.assertEqual(response_with_filter.status_code, status.HTTP_200_OK)
            self.assertGreater(len(response_with_filter.data["data"]), 0)
            self.assertGreater(len(response.data["data"]), len(response_with_filter.data["data"]))

    def test_api_properties_get_max_year_filter(self):
        """Test properties GET API endpoint max year filter.
        Max year filter must be applied.

        Must assert the next conditions:
            - Both responses have 200 OK status
            - Filter response must have more than 0 results
            - Filter response must have less results no filter response
        """

        # Setup
        url = reverse("properties")
        request_factory = APIRequestFactory()
        valid_years = [2002, 2011, 2015]

        # Check array of valid years
        for year in valid_years:

            # Request section
            request = request_factory.get(url, None, format="json")
            response = PropertiesApi.as_view()(request)
            request = request_factory.get(url, {"max_year": year}, format="json")
            response_with_filter = PropertiesApi.as_view()(request)

            # Assert with trending category
            self.assertEqual(response_with_filter.status_code, status.HTTP_200_OK)
            self.assertGreater(len(response_with_filter.data["data"]), 0)
            self.assertGreater(len(response.data["data"]), len(response_with_filter.data["data"]))

    def test_api_properties_get_random_filter(self):
        """Test properties GET API endpoint invalid filters.
        Nothing must happened, filters must not be applied.

        Must assert the next conditions:
            - Both responses have 200 OK status
            - Filter response must have more than 0 results
            - Filter response must have the same amount of results than no filter response (Due to no applied filters)
        """

        # Setup
        url = reverse("properties")
        request_factory = APIRequestFactory()
        invalid_filters = {
            "department": ["Valle", "Amazonas", "NotExisting", "invalid One"],
            "invalid_filter": ["random_data", True, 234, -5, 0]
        }

        # Check ten random cases
        iteration = 10
        while iteration >= 0:

            # Build random filter and appends to data
            random_key = random.choice(list(invalid_filters.keys()))
            random_value = random.choice(list(invalid_filters[random_key]))
            invalid_data = {random_key: random_value}

            # Request section
            request = request_factory.get(url, None, format="json")
            response = PropertiesApi.as_view()(request)
            request = request_factory.get(url, invalid_data, format="json")
            response_with_filter = PropertiesApi.as_view()(request)

            # Assert with trending category
            self.assertEqual(response_with_filter.status_code, status.HTTP_200_OK)
            self.assertGreater(len(response_with_filter.data["data"]), 0)
            self.assertEqual(len(response.data["data"]), len(response_with_filter.data["data"]))

            iteration -= 1

        