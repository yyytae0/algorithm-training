/*
#include <iostream>
#include <string>
#include <deque>
const int mx = 100001;
using namespace std;
deque<pair<int, int>> q;
int n, dp[1000]{};
char lst[1000]{}, chk[3] = { 'B', 'O', 'J' };
int bfs();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> lst[i];
	}
	int ans = bfs();
	if (ans > 0)
	{
		cout << ans;
	}
	else
	{
		cout << -1;
	}
	return 0;
}

int bfs() {
	q.push_back(make_pair(0, 0));
	int d;
	while (!q.empty())
	{
		int v = q.front().first;
		int idx = q.front().second;
		q.pop_front();
		int nidx = (idx + 1) % 3;
		for (int i = v+1; i < n; i++)
		{
			if (lst[i] == chk[nidx])
			{
				d = dp[v] + (i - v)*(i - v);
				if (dp[i] == 0)
				{
					dp[i] = d;
					q.push_back(make_pair(i, nidx));
				}
				else if (d < dp[i])
				{
					dp[i] = d;
					q.push_back(make_pair(i, nidx));
				}
			}
		}
	}
	return dp[n-1];
}
*/