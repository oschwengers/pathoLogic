# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.status import Status
from openapi_server import util

from openapi_server.models.status import Status  # noqa: E501

class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, status=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param id: The id of this InlineResponse200.  # noqa: E501
        :type id: str
        :param status: The status of this InlineResponse200.  # noqa: E501
        :type status: Status
        """
        self.openapi_types = {
            'id': str,
            'status': Status
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status'
        }

        self._id = id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this InlineResponse200.


        :return: The id of this InlineResponse200.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200.


        :param id: The id of this InlineResponse200.
        :type id: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this InlineResponse200.


        :return: The status of this InlineResponse200.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200.


        :param status: The status of this InlineResponse200.
        :type status: Status
        """

        self._status = status
