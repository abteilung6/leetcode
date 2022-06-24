import unittest


class Solution:
    @staticmethod
    def validate_parentheses(s: str) -> bool:
        """O(n)"""
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(Solution.validate_parentheses("()"), True)
        self.assertEqual(Solution.validate_parentheses("()[]{}"), True)
        self.assertEqual(Solution.validate_parentheses("()[){}"), False)


if __name__ == '__main__':
    unittest.main()
