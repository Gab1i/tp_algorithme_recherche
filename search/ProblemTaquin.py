#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Class for A* algorithm"
__version__ = "1.0"
__update__ = "20-10-20"

from math import sqrt
from search.Problem import Problem


class ProblemTaquin(Problem):
    """

    """

    def __init__(self, start, end):
        super().__init__(start, end)

    def _findHole(self, prev):
        hole = None
        for i in range(len(prev)):
            if prev[i] == '-':
                return i

        return None

    def _getHoleNeighbors(self, pos, prev):
        neighbors = []
        n = int(sqrt(len(prev)))

        x = pos // n
        y = pos % n

        if x - 1 >= 0:
            neighbors.append((x - 1) * n + y)
        if x + 1 < n:
            neighbors.append((x + 1) * n + y)
        if y - 1 >= 0:
            neighbors.append(x * n + (y - 1))
        if y + 1 < n:
            neighbors.append(x * n + (y + 1))

        return neighbors

    def _switchChr(self, prev, pos1, pos2):
        newString = ''
        for i in range(0, len(prev)):
            if i == pos1:
                newString += prev[pos2]
            elif i == pos2:
                newString += prev[pos1]
            else:
                newString += prev[i]

        return newString

    def _buildNext(self, prev):
        hole = self._findHole(prev)
        neighbors = self._getHoleNeighbors(hole, prev)
        children = []

        for n in neighbors:
            children.append(self._switchChr(prev, hole, n))

        return children

    def _computeHeuristic(self, state):
        return self._manhattanHeuristic(state)

    def _wrongPlaceHeuristic(self, state):
        wrong = 0
        for i in range(0, len(state)):
            if state[i] != self.End[i]:
                wrong += 1

        return wrong

    def _manhattanHeuristic(self, state):
        distance = 0

        for i in range(len(state)):
            if state[i] != self.End[i]:
                shouldBeAt = self.End.find(state[i])
                distance += self._manhattanDistance(i, shouldBeAt, len(state))

        return distance

    def _manhattanDistance(self, a, b, n):
        size = int(sqrt(n))

        xa = a // size; ya = a % size
        xb = b // size; yb = b % size

        return abs(xb - xa) + abs(yb - ya)
