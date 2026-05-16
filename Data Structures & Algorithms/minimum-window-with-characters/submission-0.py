class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        window = {}

        have = 0
        needCount = len(need)

        left = 0

        minLen = float('inf')
        ans = ""

        for right in range(len(s)):

            ch = s[right]

            # add character to window
            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            # check if requirement satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # valid window
            while have == needCount:

                # update answer
                windowLen = right - left + 1

                if windowLen < minLen:
                    minLen = windowLen
                    ans = s[left:right+1]

                # remove left character
                window[s[left]] -= 1

                # if requirement broken
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return ans