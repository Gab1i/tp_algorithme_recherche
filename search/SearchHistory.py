#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Node class for A* algorithm"
__version__ = "1.0"
__update__ = "20-10-20"

import time


class SearchHistory(object):
    id = 0

    def __init__(self):
        SearchHistory.id += 1
        self._id = SearchHistory.id
        self._time1 = 0
        self._time2 = 0
        self._nodes = 0
        self._path = None

    @property
    def Path(self):
        return self._path

    @property
    def EllapsedTime(self):
        return self._time2 - self._time1

    def StartRecording(self):
        self._time1 = time.process_time()

    def StopRecording(self):
        self._time2 = time.process_time()

    def AddNode(self):
        self._nodes += 1

    def __str__(self):
        return f"Solution found in {self.EllapsedTime} seconds\n" \
               f"Length of the solution: {len(self._path)}\n" \
               f"Nodes opened: {self._nodes}"

    def SetPath(self, path):
        self._path = path
