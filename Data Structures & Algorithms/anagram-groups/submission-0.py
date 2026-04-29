class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            answer[sortedWord].append(word)
        return list(answer.values())