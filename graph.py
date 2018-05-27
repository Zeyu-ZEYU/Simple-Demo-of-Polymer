from typing import Dict, List


class Graph:
    def __init__(self):
        self.graphInfoList: List[List[int]] = []  # 子列表的第一个值是vertex id，其余表示这个顶点（源点）的目标顶点
        self.graphInfoList.append([1, 2, 3])
        self.graphInfoList.append([2, 3, 5])
        self.graphInfoList.append([3, 2, 5, 6])
        self.graphInfoList.append([4, 1, 3, 5])
        self.graphInfoList.append([5, 1, 2, 3, 6])
        self.graphInfoList.append([6, 2])

        self.vertexNum = len(self.graphInfoList)

        self.vertexList = []
        for ele in self.graphInfoList:
            self.vertexList.append(ele[0])

    def getTargetVertexList(self, vertexID):
        targetVertexList = []
        for ele in self.graphInfoList:
            if ele[0] == vertexID:
                for index in range(1, len(ele)):
                    targetVertexList.append(ele[index])
                break
        return targetVertexList

    def getParIDVertexListMap(self, partitionNum: int) -> Dict[int, List[int]]:
        parIDVertexListMap: Dict[int, List[int]] = {}
        if len(self.graphInfoList) % partitionNum != 0:
            lenPerPar = int(len(self.graphInfoList) / partitionNum) + 1
        else:
            lenPerPar = int(len(self.graphInfoList) / partitionNum)
        for index in range(partitionNum - 1):
            newList = []
            startIndex = lenPerPar * index
            for index2 in range(lenPerPar):
                newList.append(self.vertexList[startIndex + index2])
            parIDVertexListMap[index + 1] = newList
        newList = []
        for index in range((partitionNum - 1) * lenPerPar, len(self.vertexList)):
            newList.append(self.vertexList[index])
        parIDVertexListMap[partitionNum] = newList
        return parIDVertexListMap
