class Solution {
public:
    string reverseOnlyLetters(string s) {
        vector<char> letters;

        for (char c : s) {
            if (isalpha(c)) {
                letters.push_back(c);
            }
        }

        string result;

        for (char c : s) {
            if (isalpha(c)) {
                result.push_back(letters.back());
                letters.pop_back();
            } else {
                result.push_back(c);
            }
        }
        return result;
    }
};