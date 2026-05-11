class Solution:
    def isValid(self, s: str) -> bool:
        br = {"{": "}", "(": ")", "[": "]"}
        vs = []
        for c in s:
            print(f"c is : {c}")
            if len(vs) == 0 and c in br.values():
                return False
            if c in br.keys():
                vs.append(c)
            else:
                if c != br[vs[-1]]:
                    return False
                else:
                    vs.pop(-1)
        return True if len(vs) == 0 else False