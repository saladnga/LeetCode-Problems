class Solution {
public:
    string reversePrefix(string word, char ch) {
        int index = word.find(ch);
        if (index == -1) {
            return word;
        }
        
        string pre_reversed = word.substr(0, index + 1);
        reverse(pre_reversed.begin(), pre_reversed.end());

        return pre_reversed + word.substr(index+1);
    }
};