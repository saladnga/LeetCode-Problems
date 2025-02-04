class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> stack;
        vector<int> answer(temperatures.size());
        
        for (int i = 0; i < temperatures.size(); i++) {
            while (stack.empty() == false && temperatures[i] > temperatures[stack.top()]) {
                int j = stack.top();
                answer[j] = i - j;
                stack.pop();
            }
            stack.push(i);
        }
        
        return answer;
    }
};