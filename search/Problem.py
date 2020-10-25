#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Class for A* algorithm"
__version__ = "1.0"
__update__ = "20-10-20"

from search.SearchNode import SearchNode


class Problem:
    """

    """

    def __init__(self, start, end):
        self._start = SearchNode(start)
        self._end = SearchNode(end)

    @property
    def Start(self):
        return self._start

    @property
    def End(self):
        return self._end.Value

    def _buildNext(self, prev):
        raise NotImplementedError()

    def GetNext(self, prev):
        children = self._buildNext(prev.Value)
        childrenNode = []
        for child in children:
            childrenNode.append(SearchNode(child))

        return childrenNode

    def isEnd(self, node):
        return node == self._end

    def SetHeuristic(self, node):
        return self._computeHeuristic(node.Value)

    def _computeHeuristic(self, value):
        raise NotImplementedError()
