class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> seen;
        int ans = 0;
        for (char c : sentence) {
            if (seen.find(c) == seen.end()) {
                ans++;
            }
            seen.insert(c);
        }
        if (ans == 26) {
            return true;
        }
        else {
            return false;
        }
    }
};