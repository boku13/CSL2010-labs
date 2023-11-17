class kmp:
    def strStr(self, haystack: str, needle: str):
        #needle : AAACAAAA
        lps = [0]*len(needle)
        if needle == "":
            return 0
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                i+=1
                prevLPS+=1
            elif prevLPS == 0:
                lps[i] = 0
                i+=1
            else:
                prevLPS = lps[prevLPS-1]
                
    #time complexity of making lps array is O(2n), where n is the length of the needle
    