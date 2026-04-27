class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"
        vi = []
        vc = []

        for i, c in enumerate(s):
            if c in vowels:
                vi.append(i)
                vc.append(c)
                
        if not vc: return s

        d = Counter(vc)
        first_occurrence = {}
        for i, c in enumerate(s):
            if c in vowels and c not in first_occurrence:
                first_occurrence[c] = i

        unique_vowels = list(d.keys())
        
        def sort_key(v):
            return (-d[v], first_occurrence[v])

        sorted_vowels = sorted(unique_vowels, key=sort_key)

        reordered_vowel_sequence = []
        for v in sorted_vowels:
            reordered_vowel_sequence.extend([v] * d[v])
            
        res = list(s)
        for i, original_vowel_pos in enumerate(vi):
            res[original_vowel_pos] = reordered_vowel_sequence[i]
            

        return "".join(res)