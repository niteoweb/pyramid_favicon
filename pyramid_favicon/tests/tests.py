# -*- coding: utf-8 -*-
"""Test that favicon.ico is served at application root."""

from pyramid import testing

import unittest
import webtest


class FaviconTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        
        self.config.include('pyramid_chameleon')
        self.config.include('pyramid_favicon')
        
        #self.config.scan()
        app = self.config.make_wsgi_app()
        self.testapp = webtest.TestApp(app)

    def tearDown(self):
        testing.tearDown()

    def test_favicon(self):
        response = self.testapp.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/x-icon')

if __name__=="__main__":
    unittest.main()
