# -*- coding: utf-8 -*-
"""Test that favicon.ico is served at application root."""

from pyramid import testing

import os
import unittest
import webtest


class FaviconTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        
        self.config.include('pyramid_chameleon')
        self.config.include('pyramid_favicon')
        
        app = self.config.make_wsgi_app()
        self.testapp = webtest.TestApp(app)

    def tearDown(self):
        testing.tearDown()

    def test_favicon(self):
        response = self.testapp.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/x-icon')

    def test_favicon_customabspath(self):
        here = os.path.dirname(os.path.realpath(__file__))
        my_path = os.path.join(here, 'mystaticfiles')

        config = testing.setUp(settings={'favicon_path':my_path})
        config.include('pyramid_chameleon')
        config.include('pyramid_favicon')

        app = config.make_wsgi_app()
        testapp = webtest.TestApp(app)

        response = testapp.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/x-icon')

    def test_favicon_custompath(self):
        test_paths = [
            'pyramid_favicon:tests/favicon.ico',
            'pyramid_favicon:tests/mystaticfiles/favicon.ico'
            ]

        for my_path in test_paths:
            my_path = 'pyramid_favicon:tests/favicon.ico'
            settings = {'favicon_path':my_path}

            config = testing.setUp(settings=settings)
            config.include('pyramid_chameleon')
            config.include('pyramid_favicon')

            app = config.make_wsgi_app()
            testapp = webtest.TestApp(app)

            response = testapp.get('/favicon.ico')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'image/x-icon')


if __name__=="__main__":
    unittest.main()
