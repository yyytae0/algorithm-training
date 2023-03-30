/*
#include <iostream>
#include <string>
#include <deque>
using namespace std;
int n, m, sheep=0, wolf=0;
char lst[250][250];
int visit[250][250];
deque<pair<int, int>> q;
void bfs(int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			lst[i][j] = s[j];
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lst[i][j] == 'v' && !visit[i][j])
			{
				visit[i][j] = 1;
				bfs(i, j);
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lst[i][j] == 'k' && !visit[i][j])
			{
				sheep++;
			}
		}
	}
	cout << sheep << ' ' << wolf;
	return 0;
}


void bfs(int a, int b) {
	int sd=0, wd=1, way[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
	q.push_back(make_pair(a, b));
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (int i = 0; i < 4; i++)
		{
			int nv[2] = { v[0] + way[i][0], v[1] + way[i][1] };
			if (nv[0]>=0 && nv[0]<n && nv[1]>=0 && nv[1]<m && lst[nv[0]][nv[1]] != '#' && !visit[nv[0]][nv[1]])
			{
				visit[nv[0]][nv[1]] = 1;
				q.push_back(make_pair(nv[0], nv[1]));
				if (lst[nv[0]][nv[1]] == 'v')
				{
					wd++;
				}
				else if (lst[nv[0]][nv[1]] == 'k')
				{
					sd++;
				}
			}
		}
	}
	if (sd > wd)
	{
		sheep += sd;
	}
	else
	{
		wolf += wd;
	}
}
*/