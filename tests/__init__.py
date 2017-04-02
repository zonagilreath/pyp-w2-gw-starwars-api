import re
import os
import json
import unittest

import responses

from starwars_api import settings
from starwars_api.client import SWAPIClient


class BaseStarWarsAPITestCase(unittest.TestCase):

    def setUp(self):
        self.api_client = SWAPIClient()

        fake_responses = [
            # (:method, :uri, :status, :fixture)

            # DETAIL /people
            ('GET', r'{}/people/100', 404, 'not_found.json'),
            ('GET', r'{}/people/1', 200, 'people_id_1.json'),

            # LIST /people
            ('GET', r'{}/people\?page=(?![12]$).+', 404, 'not_found.json'),
            ('GET', r'{}/people\?page=1$', 200, 'people_page_1.json'),
            ('GET', r'{}/people\?page=2$', 200, 'people_page_2.json'),
            ('GET', r'{}/people', 200, 'people_page_1.json'),

            # DETAIL /films
            ('GET', r'{}/films/100', 404, 'not_found.json'),
            ('GET', r'{}/films/1', 200, 'films_id_1.json'),

            # LIST /films
            ('GET', r'{}/films\?page=(?!1$).+', 404, 'not_found.json'),
            ('GET', r'{}/films\?page=1', 200, 'films_page_1.json'),
            ('GET', r'{}/films', 200, 'films_page_1.json'),
        ]
        for method, uri, status, fixture_file in fake_responses:
            fixture_path = os.path.join(settings.BASE_DIR, 'tests',
                                        'fixtures', fixture_file)
            with open(fixture_path) as f:
                json_fixture = json.load(f)
            responses.add(method, re.compile(uri.format(settings.BASE_URL)),
                          json=json_fixture, status=status,
                          content_type='application/json')
