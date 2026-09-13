class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        maps={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in maps:
                if not st or st[-1] != maps[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)
        return len(st)==0


            