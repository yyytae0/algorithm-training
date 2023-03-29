/*
#include <iostream>
#include <algorithm>
using namespace std;
long int n, mn = 1000000000, mx = 0;
long int* lst = new long int[100001] {};

int check(int a, long int *lst) {
	int ans = 0;
	for (int i = 0; i < n-1; i++)
	{
		ans += (lst[i] / a) - 1;
	}
	return ans;
}

int gcd(int a, int b) {
	if (a == 0)
	{
		return b;
	}
	return gcd(b%a, a);
}

int main() {
	int ans;
	long int dummy;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> lst[i];
	}
	sort(lst, lst + n);
	for (int i = 0; i < n-1; i++)
	{
		dummy = lst[i];
		lst[i] = lst[i + 1] - dummy;
		if (lst[i] < mn)
		{
			mn = lst[i];
		}
		if (lst[i] > mx)
		{
			mx = lst[i];
		}
	}
	lst[n-1] = 0;
	ans = check(gcd(mn, mx), lst);
	cout << ans;
	delete[] lst;
	return 0;
}
*/