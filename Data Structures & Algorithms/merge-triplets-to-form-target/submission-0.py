class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]

        for trip in triplets:
            if any(trip[i] > target[i] for i in range(3)):
                continue
            for i in range(3):
                if trip[i] == target[i]:
                    found[i] = True
        
        return found[0] and found[1] and found[2]