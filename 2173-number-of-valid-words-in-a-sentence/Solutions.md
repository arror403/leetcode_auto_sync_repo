# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Regex is quite suitable for this question.
# Approach
By uncomment **print(r.match(s))** in the for loop: <br>
 <br>
sentence = "alice and  bob are playing stone-game10" <br>
Stdout: <br>
<re.Match object; span=(0, 5), match='alice'> <br>
<re.Match object; span=(0, 3), match='and'> <br>
<re.Match object; span=(0, 3), match='bob'> <br>
<re.Match object; span=(0, 3), match='are'> <br>
<re.Match object; span=(0, 7), match='playing'> <br>
None <br>
Output: 5 <br> 
 <br>
sentence = "a-b. afad ba-c a! !" <br>
Stdout: <br>
<re.Match object; span=(0, 4), match='a-b.'> <br>
<re.Match object; span=(0, 4), match='afad'> <br>
<re.Match object; span=(0, 4), match='ba-c'> <br>
<re.Match object; span=(0, 2), match='a!'> <br>
<re.Match object; span=(0, 1), match='!'> <br>
Output: 5 <br>
# Code
```python3 []
class Solution:
    def countValidWords(self, sentence: str) -> int:
        r = re.compile('^[a-z]*([a-z]+\-[a-z]+)?[a-z]*[\!\.\,]?$')
        # ^[a-z]*            - Start with zero or more lowercase letters
        # ([a-z]+\-[a-z]+)?  - Optionally contain a hyphen surrounded by letters on both sides
        # [a-z]*             - Followed by zero or more lowercase letters
        # [\!\.\,]?          - Optionally end with one punctuation mark (!, ., or ,)
        # $                  - End of string
        res = 0
        # Split sentence by whitespace
        for s in sentence.split():
            #print(r.match(s))
            # Check if the token matches the valid word pattern
            if r.match(s):
                # Increment counter if it's a valid word
                res += 1
        
        # Return the total count of valid words
        return res
```
# One-liner
```python3 []
class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len([s for s in sentence.split() if re.match('^[a-z]*([a-z]+\-[a-z]+)?[a-z]*[\!\.\,]?$', s)])
```
