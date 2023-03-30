/*
#include <iostream>
#include <deque>
#include <vector>
const int mx = 100001;
using namespace std;
int a, b, n, m, visit[1001]{};
deque<int> q;
vector<int> lst[1001];
int bfs();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> a >> b >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int d1, d2;
		cin >> d1 >> d2;
		lst[d1].push_back(d2);
		lst[d2].push_back(d1);
	}
	if (a == b)
	{
		cout << 0;
	}
	else
	{
		cout << bfs() - 1;
	}
	return 0;
}


int bfs() {
	q.push_back(a);
	visit[a] = 1;
	while (!q.empty())
	{
		int v = q.front();
		q.pop_front();
		for (int i:lst[v])
		{
			if (!visit[i])
			{
				visit[i] = visit[v] + 1;
				q.push_back(i);
				if (i == b)
				{
					return visit[i];
				}
			}
		}
	}
	return 0;
}
*/