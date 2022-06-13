import unittest


class Solution:
    @classmethod
    def longest_substring_bruteforce(cls, s: str) -> int:
        """Brute force with O(n^3)"""
        n = len(s)
        result = 0

        for i in range(0, n):
            for j in range(i + 1, n):
                if cls._unique_chars(s[i:j]):
                    result = max(result, j - i)
        return result

    @staticmethod
    def _unique_chars(s: str) -> bool:
        chars = [0] * 128  # set
        for i in range(0, len(s)):
            c = s[i]
            if chars[ord(c)] > 0:
                return False
            else:
                chars[ord(c)] += 1
        return True

    @staticmethod
    def longest_substring_sliding_window(s: str) -> int:
        """Sliding window with O(n)"""
        result = 0
        chars = [0] * 128
        left, right = 0, 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1
        return result


class TestSolution(unittest.TestCase):
    def test_longest_substring_bruteforce(self):
        self.assertEqual(Solution.longest_substring_bruteforce("abcabcbb"), 3)
        self.assertEqual(Solution.longest_substring_bruteforce("bbbbb"), 1)
        self.assertEqual(Solution.longest_substring_bruteforce("pwwkew"), 3)
        self.assertEqual(Solution.longest_substring_bruteforce(""), 0)

    def test_longest_substring_sliding_window(self):
        self.assertEqual(Solution.longest_substring_sliding_window("abcabcbb"), 3)
        self.assertEqual(Solution.longest_substring_sliding_window("bbbbb"), 1)
        self.assertEqual(Solution.longest_substring_sliding_window("pwwkew"), 3)
        self.assertEqual(Solution.longest_substring_sliding_window(""), 0)


if __name__ == '__main__':
    unittest.main()
