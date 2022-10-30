class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creatorToBestId = {}
        creatorToPopularity = {}
        
        for i in range(len(creators)):
            if creators[i] in creatorToBestId:
                if views[creatorToBestId[creators[i]]] < views[i]:
                    creatorToBestId[creators[i]] = i
                elif views[creatorToBestId[creators[i]]] == views[i] and ids[creatorToBestId[creators[i]]] > ids[i]:
                    creatorToBestId[creators[i]] = i                                     
            else:
                creatorToBestId[creators[i]] = i
            if creators[i] in creatorToPopularity:
                creatorToPopularity[creators[i]] += views[i]
            else:
                creatorToPopularity[creators[i]] = views[i]
        
        maxPopularity = 0
        maxCreators = []
        for creator in creatorToPopularity:
            if creatorToPopularity[creator] > maxPopularity:
                maxCreators = [creator]
                maxPopularity = creatorToPopularity[creator]
            elif creatorToPopularity[creator] == maxPopularity:
                maxCreators.append(creator)
        
        return [[maxCreator, ids[creatorToBestId[maxCreator]]] for maxCreator in maxCreators]
