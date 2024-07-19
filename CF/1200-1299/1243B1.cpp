// submission link: https://codeforces.com/contest/1243/submission/271338756

#include<bits/stdc++.h>
using namespace std;

void solve(){
    int n, ci = 0;
    cin >> n;
    string s, t;
    cin >> s >> t;

    int flag = -1;
    for(int i = 0; i < n; i ++){
        if (s[i] != t[i]) {
            if (flag == -1) {
                flag = 0;
                ci = i;
            }else if (flag) {
                flag = 0;
                break;
            }else if (!flag && s[i] == s[ci] && t[i] == t[ci]){
                flag = 1;
            }else break;
        }
    }
    if (flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" <<endl;
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int check;
    cin >> check;
    while (check --){
        solve();
    }
}