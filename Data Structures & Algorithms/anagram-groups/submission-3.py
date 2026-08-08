class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        return list(dic.values())