// submission link: https://codeforces.com/contest/1372/submission/271861511

#include<cmath>
#include<iostream>

void solve(){
    int n;
    std::cin >> n;
    for (int i = 2; i < sqrt(n) + 1; i ++){
        if (n % i == 0) {
            int k = n / i;
            std::cout << k << ' ' << n - k << std::endl;
            return;
        }
    }
    std::cout << 1 << " " << n - 1 << std::endl;
    return;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    int check;
    std::cin >> check;
    while (check --) {
        solve();
    }
    return 0;
}