class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        stringstream ss(path);
        string temp;

        while (getline(ss, temp, '/')) {
            if (temp == "." || temp.empty() == true) {
                continue;
            }
            else if (temp == "..") {
                if (stack.empty() == false) {
                    stack.pop_back();
                }
            }
            else {
                stack.push_back(temp);
            }
        }

        string ans = "";
        for (string dir : stack) {
            ans += "/" + dir;
        }
        if (ans.empty() == true) {
            return "/";
        }
        else {
            return ans;
        }

    }
};