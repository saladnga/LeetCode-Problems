class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first_overlap_second = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            second_overlap_first = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]

            if (first_overlap_second or second_overlap_first):
                result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return result
        