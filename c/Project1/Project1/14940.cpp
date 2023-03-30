/*
#include <iostream>
#include <deque>
using namespace std;
int n, m;
int lst[1000][1000];
int visit[1000][1000]{};
deque<pair<int, int>> q;
void bfs();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> lst[i][j];
			if (lst[i][j] == 2)
			{
				q.push_back(make_pair(i, j));
				lst[i][j] = 0;
				visit[i][j] = 1;
			}
		}
	}
	bfs();
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lst[i][j] == 1 && !visit[i][j])
			{
				lst[i][j] = -1;
			}
			cout << lst[i][j] << ' ';
		}
		cout << '\n';
	}
	return 0;
}

void bfs() {
	int way[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (int i = 0; i < 4; i++)
		{
			int nv[2] = { v[0] + way[i][0], v[1] + way[i][1] };
			if (nv[0]>=0 && nv[0]<n && nv[1]>=0 && nv[1]<m && !visit[nv[0]][nv[1]] && lst[nv[0]][nv[1]]==1)
			{
				lst[nv[0]][nv[1]] = lst[v[0]][v[1]] + 1;
				visit[nv[0]][nv[1]] = 1;
				q.push_back(make_pair(nv[0], nv[1]));
			}
		}
	}
}
*/