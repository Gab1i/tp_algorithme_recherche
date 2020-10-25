#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Node class for A* algorithm"
__version__ = "1.0"
__update__ = "20-10-20"


class SearchNode(object):
    def __init__(self, v):
        self._value = v

        self.Parent = None

        self._h = 0
        self._g = 0

        self._distance = None

    @property
    def Value(self):
        return self._value

    @property
    def F(self):
        return self._g + self._h

    def setH(self, value):
        self._h = value

    def setG(self, value):
        self._g = value

    @property
    def G(self):
        return self._g

    @property
    def H(self):
        return self._h

    def __eq__(self, n2):
        if n2 is None:
            return False

        return n2.Value == self._value

    def __ne__(self, n2):
        return not n2 == self

    def __str__(self):
        return f"{self._value} (G={self._g}, H={self._h})"

    def __repr__(self):
        return f"{self._value} (G={self._g}, H={self._h})"

    @G.setter
    def G(self, value):
        self._G = value

    @H.setter
    def H(self, value):
        self._H = value
