#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Main algorithm"
__version__ = "1.0"
__update__ = "20-10-24"

from search.ProblemTaquin import ProblemTaquin
from search.Search import aStarSearch

problemTaquin = ProblemTaquin('38261574-', '12345678-')
result = aStarSearch(problemTaquin)
print(result)
print(result.Path)

