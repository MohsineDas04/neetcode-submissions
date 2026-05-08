class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded = ""
        self.ll = strs
        for s in strs:
            self.encoded = self.encoded + f"{s}20041707"
        # print(f"encoded : {self.encoded}")
        return self.encoded
    def decode(self, s: str) -> List[str]:
        self.decoded = self.encoded.split("20041707")
        self.decoded.pop(-1)
        return self.decoded