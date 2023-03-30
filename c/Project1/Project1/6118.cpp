/*
#include <iostream>
#include <deque>
#include <vector>
using namespace std;
vector<int> e[20001];
int visit[20001] = {};
int n, m;
void bfs();
void ans();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		e[a].push_back(b);
		e[b].push_back(a);
	}
	bfs();
	return 0;
}

void bfs() {
	deque<int> q;
	q.push_back(1);
	visit[1] = 1;
	while (!q.empty())
	{
		int v = q.front();
		q.pop_front();
		for (int i:e[v])
		{
			if (visit[i] == 0)
			{
				visit[i] = visit[v]+1;
				q.push_back(i);
			}
		}
	}
	ans();
}

void ans() {
	int mx = 0, cnt = 1, idx;
	for (int i = 1; i < n+1; i++)
	{
		if (visit[i] > mx)
		{
			mx = visit[i];
			idx = i;
			cnt = 1;
		}
		else if (visit[i] == mx)
		{
			cnt++;
		}
	}
	cout << idx << ' ' << mx-1 << ' ' << cnt;
}
*/