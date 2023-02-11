//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
  bool match(const string& w, const string& pat) {
    int j = 0;
    for (int i = 0; i < w.size() && j < pat.size(); ++i) {
      if (w[i] == pat[j]) {
        ++j;
      } else if (isupper(w[i])) {
        return false;
      }
    }
    return j == pat.size();
  }

 public:
  vector<string> CamelCase(int N, vector<string> Dictionary, string Pattern) {
    // code here
    vector<string> ans;
    for (auto& w : Dictionary) {
      if (match(w, Pattern)) {
        ans.push_back(w);
      }
    }
    return ans;
  }
};

//{ Driver Code Starts.
int main() {
  int t;
  cin >> t;
  while (t--) {
    int N;
    cin >> N;
    vector<string> Dictionary(N);
    for (int i = 0; i < N; i++) cin >> Dictionary[i];
    string Pattern;
    cin >> Pattern;
    Solution ob;
    vector<string> ans = ob.CamelCase(N, Dictionary, Pattern);
    sort(ans.begin(), ans.end());
    for (auto u : ans) cout << u << " ";
    cout << "\n";
  }
  return 0;
}
// } Driver Code Ends
