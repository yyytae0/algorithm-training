/*
#include <iostream>
#include <vector>
#include <deque>
using namespace std;
int n, visit[10]{};
long long int mx = 0, mn = 10000000000;
char lst[9], sm[10];
void dfs(int, int, long long int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> lst[i];
	}
	for (int i = 0; i < 10; i++)
	{
		visit[i] = 1;
		dfs(i, 0, (long long int)i);
		visit[i] = 0;
	}
	int d = 1;
	for (int i = 0; i < n; i++)
	{
		d = d * 10;
	}
	cout << mx << endl;
	if (mn < d)
	{
		cout << 0 << mn;
	}
	else
	{
		cout << mn;
	}
	return 0;
}

void dfs(int now, int cnt, long long int sm) {
	if (cnt == n)
	{
		if (sm < mn)
		{
			mn = sm;
		}
		if (sm > mx)
		{
			mx = sm;
		}
		return;
	}
	if (lst[cnt] == '<')
	{
		for (int i = now+1; i < 10; i++)
		{
			if (visit[i] == 0)
			{
				visit[i] = 1;
				dfs(i, cnt + 1, sm*10+i);
				visit[i] = 0;
			}
		}
	}
	else
	{
		for (int i = now-1; i > -1; i--)
		{
			if (visit[i] == 0)
			{
				visit[i] = 1;
				dfs(i, cnt + 1, sm*10+i);
				visit[i] = 0;
			}
		}
	}
}
*/