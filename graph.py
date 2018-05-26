from typing import List


class Graph:
    def __init__(self):
        self.graphInfoList: List[List[int]] = []  # 子列表的第一个值是vertex id，其余表示这个顶点（源点）的目标顶点
        self.graphInfoList.push([1, 2, 3])
        self.graphInfoList.push([2, 3, 5])
        self.graphInfoList.push([3, 2, 5, 6])
        self.graphInfoList.push([4, 1, 3, 5])
        self.graphInfoList.push([5, 1, 2, 3])
        self.graphInfoList.push([6, 2])

    def getVertexList(self):
        vertexList = []
        for ele in self.graphInfoList:
            vertexList.push(ele[0])
        return vertexList

    def getTargetVertexList(self, vertexID):
        targetVertexList = []
        for ele in self.graphInfoList:
            if ele[0] == vertexID:
                for index in range(1, len(ele)):
                    targetVertexList.push(ele[index])
        return targetVertexList
