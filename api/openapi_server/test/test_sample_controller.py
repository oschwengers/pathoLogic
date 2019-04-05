# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSampleController(BaseTestCase):
    """SampleController integration test stubs"""

    def test_result_sample_idget(self):
        """Test case for result_sample_idget

        Lists results for given sample
        """
        headers = { 
            'Accept': '*/*',
        }
        response = self.client.open(
            '/v1/result/{sample_id}'.format(sample_id='sample_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_samples_sample_id_start_put(self):
        """Test case for samples_sample_id_start_put

        Starts one or multiple sample via ID
        """
        headers = { 
            'Accept': '*/*',
        }
        response = self.client.open(
            '/v1/samples/{sample_id}/start'.format(sample_id='sample_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
