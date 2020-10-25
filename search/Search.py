#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Gabriel Nativel-Fontaine"
__date__ = "20-10-20"
__usage__ = "Collection of search algorithms"
__version__ = "2.0"
__update__ = "25-10-2020"

from search.SearchHistory import SearchHistory


def aStarSearch(problem, heuristic):
    history = SearchHistory()

    # initialize lists
    openedList = [problem.Start]
    closedList = []

    current = problem.Start
    marked = [current]
    current.setH(problem.SetHeuristic(current))

    history.StartRecording()
    while (len(openedList) > 0) and not any(problem.isEnd(x) for x in closedList):
        # sort open list according F value
        openedList.sort(key=lambda x: x.F)

        # get best node
        current = openedList[0]
        history.AddNode()

        # stop the algorithm when goal state is reached
        if problem.isEnd(current):
            break

        # update lists
        openedList.remove(current)
        closedList.append(current)

        children = problem.GetNext(current)

        # for all successors, build node
        for child in children:
            child.Parent = current
            child.setG(current.G + 1)
            child.setH(problem.SetHeuristic(child))

            if child not in marked:
                marked.append(child)
                openedList.append(child)
            else:
                for i in range(len(openedList)):
                    if openedList[i] == child:
                        if child.G < openedList[i].G:
                            openedList[i] = child

    history.StopRecording()

    # rebuild the path
    path = []
    while current.Parent is not None:
        path.insert(0, current)
        current = current.Parent

    history.SetPath(path)
    return history


def breadthFirstSearch(problem, heuristic):
    pass


def ipa_star(problem, heuristic):
    pass
