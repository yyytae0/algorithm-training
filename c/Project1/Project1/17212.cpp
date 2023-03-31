/*
#include <iostream>
#include <deque>
const int mx = 100001;
using namespace std;
int n, step[4] = { 1, 2, 5, 7 }, dp[mx]{};
deque<int> q;
void bfs();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	bfs();
	cout << dp[n];
	return 0;
}

void bfs() {
	q.push_back(0);
	while (!q.empty())
	{
		int v = q.front();
		q.pop_front();
		for (int i:step)
		{
			int nv = v + i;
			if (nv <= n && dp[nv] == 0) {
				dp[nv] = dp[v] + 1;
				q.push_back(nv);
				if (nv == n)
				{
					return;
				}
			}
		}

	}
}
*/