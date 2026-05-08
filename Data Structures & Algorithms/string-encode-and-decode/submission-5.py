from random import randint
class Solution:

    def encode(self, strs: List[str]) -> str:
        self.key = randint(0, 9999999) + randint(0, 9999999) + randint(0, 9999999) - randint(0, 659) / randint(10, 555)
        self.key = str(self.key)
        self.encoded = ""
        self.ll = strs
        for s in strs:
            self.encoded = self.encoded + f"{s}{self.key}"
        # print(f"encoded : {self.encoded}")
        return self.encoded
    def decode(self, s: str) -> List[str]:
        self.decoded = self.encoded.split(self.key)
        self.decoded.pop(-1)
        return self.decoded