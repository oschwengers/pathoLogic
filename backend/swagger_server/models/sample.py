# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Sample(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, author_email: str=None, created: date=None, last_updated: date=None, path_lr: str=None, path_sr1: str=None, path_sr2: str=None):  # noqa: E501
        """Sample - a model defined in Swagger

        :param id: The id of this Sample.  # noqa: E501
        :type id: str
        :param author_email: The author_email of this Sample.  # noqa: E501
        :type author_email: str
        :param created: The created of this Sample.  # noqa: E501
        :type created: date
        :param last_updated: The last_updated of this Sample.  # noqa: E501
        :type last_updated: date
        :param path_lr: The path_lr of this Sample.  # noqa: E501
        :type path_lr: str
        :param path_sr1: The path_sr1 of this Sample.  # noqa: E501
        :type path_sr1: str
        :param path_sr2: The path_sr2 of this Sample.  # noqa: E501
        :type path_sr2: str
        """
        self.swagger_types = {
            'id': str,
            'author_email': str,
            'created': date,
            'last_updated': date,
            'path_lr': str,
            'path_sr1': str,
            'path_sr2': str
        }

        self.attribute_map = {
            'id': 'id',
            'author_email': 'author_email',
            'created': 'created',
            'last_updated': 'last_updated',
            'path_lr': 'path_lr',
            'path_sr1': 'path_sr1',
            'path_sr2': 'path_sr2'
        }

        self._id = id
        self._author_email = author_email
        self._created = created
        self._last_updated = last_updated
        self._path_lr = path_lr
        self._path_sr1 = path_sr1
        self._path_sr2 = path_sr2

    @classmethod
    def from_dict(cls, dikt) -> 'Sample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Sample of this Sample.  # noqa: E501
        :rtype: Sample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Sample.


        :return: The id of this Sample.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Sample.


        :param id: The id of this Sample.
        :type id: str
        """

        self._id = id

    @property
    def author_email(self) -> str:
        """Gets the author_email of this Sample.


        :return: The author_email of this Sample.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email: str):
        """Sets the author_email of this Sample.


        :param author_email: The author_email of this Sample.
        :type author_email: str
        """

        self._author_email = author_email

    @property
    def created(self) -> date:
        """Gets the created of this Sample.


        :return: The created of this Sample.
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created: date):
        """Sets the created of this Sample.


        :param created: The created of this Sample.
        :type created: date
        """

        self._created = created

    @property
    def last_updated(self) -> date:
        """Gets the last_updated of this Sample.


        :return: The last_updated of this Sample.
        :rtype: date
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: date):
        """Sets the last_updated of this Sample.


        :param last_updated: The last_updated of this Sample.
        :type last_updated: date
        """

        self._last_updated = last_updated

    @property
    def path_lr(self) -> str:
        """Gets the path_lr of this Sample.


        :return: The path_lr of this Sample.
        :rtype: str
        """
        return self._path_lr

    @path_lr.setter
    def path_lr(self, path_lr: str):
        """Sets the path_lr of this Sample.


        :param path_lr: The path_lr of this Sample.
        :type path_lr: str
        """

        self._path_lr = path_lr

    @property
    def path_sr1(self) -> str:
        """Gets the path_sr1 of this Sample.


        :return: The path_sr1 of this Sample.
        :rtype: str
        """
        return self._path_sr1

    @path_sr1.setter
    def path_sr1(self, path_sr1: str):
        """Sets the path_sr1 of this Sample.


        :param path_sr1: The path_sr1 of this Sample.
        :type path_sr1: str
        """

        self._path_sr1 = path_sr1

    @property
    def path_sr2(self) -> str:
        """Gets the path_sr2 of this Sample.


        :return: The path_sr2 of this Sample.
        :rtype: str
        """
        return self._path_sr2

    @path_sr2.setter
    def path_sr2(self, path_sr2: str):
        """Sets the path_sr2 of this Sample.


        :param path_sr2: The path_sr2 of this Sample.
        :type path_sr2: str
        """

        self._path_sr2 = path_sr2
