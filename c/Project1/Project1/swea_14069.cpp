/*
#include <iostream>
using namespace std;
int** lst = new int*[16];
int n, ans;
int food[16] = {};

int calc(int *arr) {
	int sm = 0;
	for (int i = 0; i < n / 2; i++)
	{
		for (int j = i + 1; j < n / 2; j++)
		{
			sm += lst[arr[i]][arr[j]];
		}
	}
	return sm;
}

int comp() {
	int A[8] = {}, B[8] = {};
	int idx_a = 0, idx_b = 0, a, b;
	for (int i = 0; i < n; i++)
	{
		if (food[i] == 1)
		{
			A[idx_a++] = i;
		}
		else
		{
			B[idx_b++] = i;
		}
	}
	a = calc(A);
	b = calc(B);
	if (a > b)
	{
		return a - b;
	}
	return b - a;
}

void check(int s, int cnt) {
	int dummy;
	if (cnt == n/2)
	{
		dummy = comp();
		if (dummy < ans)
		{
			ans = dummy;
		}
		return;
	}
	for (int i = s+1; i < n; i++)
	{
		food[i] = 1;
		check(i, cnt + 1);
		food[i] = 0;
	}
}

int main() {
	int ip, d;
	cin >> ip;
	for (int i = 1; i < ip+1; i++)
	{
		cin >> n;
		for (int row = 0; row < n; row++)
		{
			lst[row] = new int[n];
			for (int col = 0; col < n; col++)
			{
				cin >> lst[row][col];
			}
		}
		for (int row = 0; row < n; row++)
		{
			for (int col = row; col < n; col++)
			{
				d = lst[row][col] + lst[col][row];
				lst[row][col] = d;
				lst[col][row] = d;
			}
		}
		ans = 1000000;
		check(-1, 0);
		cout << '#' << i << ' ' << ans << endl;
	}
	return 0;
}
*/