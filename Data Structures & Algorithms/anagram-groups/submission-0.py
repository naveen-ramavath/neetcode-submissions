from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=defaultdict(list)
        for i in strs:
            j=''.join(sorted(i))
            k[j].append(i)
        return list(k.values())
        