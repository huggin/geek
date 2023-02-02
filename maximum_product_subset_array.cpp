//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution{
    public:
    long long int findMaxProduct(vector<int>&a, int n){
        //Write your code here  
        int m = 0;
        int z = 0;
        long long t = 1;
        int mi = INT_MIN;
        for(int i = 0; i < n; ++i) {
            if (a[i] == 0) {
                ++z;
                continue;
            }
            if (a[i] < 0) {
                ++m;
                mi = max(a[i], mi);
            }
            t = (t * a[i]) % 1000000007;
        }
        if (m == 1 && m == n) return t;
        if (m + z == n && m == 1) return 0;
        if (t > 0) return t;
        return t / mi;
    }
};



//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<int>arr(n);
	    for(int i = 0 ; i < n; i++){
	        cin >> arr[i];
	    }
	    Solution ob;
	    long long int ans = ob.findMaxProduct(arr, n);
	    cout << ans<<endl;
	}
	return 0;
}

// } Driver Code Ends
