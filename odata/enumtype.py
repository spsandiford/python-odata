# -*- coding: utf-8 -*-

from enum import Enum

from odata.property import PropertyBase


class EnumType(Enum):
    pass


class EnumTypeProperty(PropertyBase):
    """
    A property that contains a ComplexType object

    :param name: Name of the property in the endpoint
    :param enum_class: A subclass of EnumType
    """

    def __init__(self, name, enum_class=EnumType, namespace=None):
        super(EnumTypeProperty, self).__init__(name)
        self.enum_class = enum_class
        self.namespace = namespace

    def serialize(self, value):
        return value.name

    def deserialize(self, value):
        return self.enum_class[value]

    def __eq__(self, other):
        if self.namespace:
            return u"{0} eq {1}.{2}'{3}'".format(self.name, self.namespace, self.enum_class.__name__, other)
        else:
            return super(EnumTypeProperty, self).__eq__(other)

