// submission link: https://codeforces.com/contest/1167/submission/271163646

#include<bits/stdc++.h>
using namespace std;

struct node{
    long long l, r, v;
    node(): l(INT_MAX), r(-1) {}
};

int main(){
    long long n, x, y;
    cin >> n >> x;
    node* ps = new node[x + 1];
    for(int i = 0; i < n; i++){
        cin >> y;
        if(ps[y].l == INT_MAX){
            ps[y].l = i;
            ps[y].v = y;
        }
        ps[y].r = i;
    }
    vector<node> b;
    for(int i = 1; i <= x; i ++){
        if(ps[i].r >= 0){
            b.emplace_back(ps[i]);
        }
    }
    n = b.size();
    int i = 0, j = n - 1;
    while(i < n - 1 && b[i].r < b[i + 1].l) i ++;
    if(i == n - 1){
        cout << x * (x + 1) / 2 << endl;
        return 0;
    }
    long long ans = b[i + 1].v * (x + 1 - b[n - 1].v);
    while(j >= 0 && (j == n - 1 || b[j].r < b[j + 1].l)){
        while(i >= 0 && b[i].r >= b[j].l) i --;
        ans += b[i + 1].v * (b[j].v - b[j - 1].v);
        j --;
    }
    cout << ans << endl;
    delete[] ps;
    return 0;
}
