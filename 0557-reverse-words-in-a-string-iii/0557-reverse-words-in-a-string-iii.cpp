class Solution {
public:
    string reverseWords(string s) {
        string word;
        stringstream ss(s);
        string result;
        while(getline(ss, word, ' ')) {
            int left = 0;
            int right = word.size() - 1;
            while (left < right) {
                char temp = word[left];
                word[left] = word[right];
                word[right] = temp;
                left++;
                right--;
            }
            if (!result.empty()) {
                result += " ";
            }
            result += word;
        }
        return result;
        
    }
};