class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> counts;
        for (char c : s) {
            counts[c]++;
        }
        unordered_set<int> frequencies;
        for (auto [key,val]: counts) {
            frequencies.insert(val);
        }
        return frequencies.size() == 1;
    }
};