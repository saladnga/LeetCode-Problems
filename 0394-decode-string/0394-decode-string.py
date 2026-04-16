class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack, str_stack = [], []
        curr_num, curr_str = 0, ""
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                count_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif char == "]":
                num = count_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + (num * curr_str)
            else:
                curr_str += char
        return curr_str


        