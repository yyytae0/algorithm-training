/*
#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;
//int** lst = new int*[100001];
int* visit = new int[100001]{};
vector<int> e[100001];
int n, m, r;
void bfs(int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int a, b;
	cin >> n >> m >> r;
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b;
		e[a].push_back(b);
		e[b].push_back(a);
	}
	for (int i = 1; i < n + 1; i++)
	{
		sort(e[i].begin(), e[i].end());
	}
	bfs(r);
	cout << visit[1];
	for (int i = 2; i < n + 1; i++)
	{
		cout << '\n' << visit[i];
	}
	return 0;
}

void bfs(int r) {
	int cnt = 0;
	deque<int> q;
	q.push_back(r);
	visit[r] = ++cnt;
	while (!q.empty())
	{
		int v = q.front();
		q.pop_front();
		for (int i : e[v])
		{
			if (visit[i] == 0)
			{
				visit[i] = ++cnt;
				q.push_back(i);
			}
		}
	}
}
*/