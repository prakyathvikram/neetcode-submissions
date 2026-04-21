class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            key = "".join(sorted(s))

            if not key in seen:
                seen[key] = []
            seen[key].append(s)
        return list(seen.values())

    

        