/*
#include <iostream>
using namespace std;
long int n, lst[100001], mn = 1000000000;

int check(long int a) {
	int ans = 0;
	for (int i = 0; i < n-1; i++)
	{
		if (lst[i] % a != 0)
		{
			return 0;
		}
		ans += (lst[i] / a) - 1;
	}
	return ans;
}

int main() {
	int ans, dummy1, dummy2;
	cin >> n;
	cin >> dummy1;
	for (int i = 0; i < n-1; i++)
	{
		cin >> dummy2;
		lst[i] = dummy2 - dummy1;
		dummy1 = dummy2;
		if (lst[i] < mn)
		{
			mn = lst[i];
		}
	}
	for (int i = mn; i > 0; i--)
	{
		if (mn % i == 0)
		{
			ans = check(i);
			if (ans > 0)
			{
				cout << ans;
				return 0;
			}
		}
	}
	return 0;
}
*/