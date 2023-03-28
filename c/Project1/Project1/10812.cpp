/*
#include <iostream>
using namespace std;
int main() {
	int n, m, a, b, c;
	int lst[101];
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		lst[i] = i + 1;
	}
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b >> c;
		int dummy[101];
		int idx = 0;
		for (int j = c-1; j < b; j++)
		{
			dummy[idx] = lst[j];
			idx++;
		}
		for (int j = a-1; j < c; j++)
		{
			dummy[idx] = lst[j];
			idx++;
		}
		idx = 0;
		for (int j = a-1; j < b; j++)
		{
			lst[j] = dummy[idx];
			idx++;
		}
	}
	for (int i = 0; i < n; i++)
	{
		cout << lst[i] << ' ';
	}
	return 0;
}
*/