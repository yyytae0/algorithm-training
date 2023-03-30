/*
#include <iostream>
using namespace std;
int** lst = new int*[10];
int n, ans, chk[10] = {};
void dfs(int);
int check(int, int);

int main() {
	int ip;
	cin >> ip;
	for (int i = 1; i < ip+1; i++)
	{
		cin >> n;
		for (int row = 0; row < n; row++)
		{
			lst[row] = new int[n] {};
		}
		ans = 0;
		dfs(0);
		cout << '#' << i << ' ' << ans << endl;
	}
	return 0;
}

void dfs(int row) {
	int idx1, idx2;
	if (row == n)
	{
		ans++;
		return;
	}
	for (int i = 0; i < n; i++)
	{
		if (chk[i] == 0)
		{
			if (check(row, i) == 1)
			{
				chk[i] = 1;
				lst[row][i] = 1;
				dfs(row + 1);
				chk[i] = 0;
				lst[row][i] = 0;
			}
		}
	}
}


int check(int row, int idx) {
	int idx1 = idx, idx2 = idx;
	while (row > 0)
	{
		row--;
		idx1--;
		idx2++;
		if (idx1 >= 0)
		{
			if (lst[row][idx1] == 1)
			{
				return 0;
			}
		}
		if (idx2 < n)
		{
			if (lst[row][idx2] == 1)
			{
				return 0;
			}
		}
	}
	return 1;
}
*/