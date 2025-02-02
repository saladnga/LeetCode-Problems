class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        unordered_map<char, char> matching {{'(', ')'}, {'{','}'}, {'[',']'}};

        for (char c : s) {
            if (matching.find(c) != matching.end()) {
                stack.push(c);
            }
            else {
                if (stack.empty()) {
                    return false;
                }
                
                char previous_character = stack.top();
                if (matching[previous_character] != c) {
                    return false;
                }
                else {
                    stack.pop();
                }
            }

        }
        return stack.empty();
    }
};