/*
#include <iostream>
#include <deque>

using namespace std;
int n, m, lst[250][250] = {}, visit[250][250] = {};
deque<pair<int, int>> q;
void bfs(int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int cnt = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> lst[i][j];
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lst[i][j] == 1 && !visit[i][j])
			{
				visit[i][j] = 1;
				bfs(i, j);
				cnt++;
			}
		}
	}
	cout << cnt;
	return 0;
}

void bfs(int a, int b) {
	int way[8][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1} };
	q.push_back(make_pair(a, b));
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (int i = 0; i < 8; i++)
		{
			int nv[2] = { v[0] + way[i][0], v[1] + way[i][1] };
			if (nv[0] >= 0 && nv[0] < n && nv[1] >= 0 && nv[1] < m && lst[nv[0]][nv[1]] && !visit[nv[0]][nv[1]]) {
				visit[nv[0]][nv[1]] = 1;
				q.push_back(make_pair(nv[0], nv[1]));
			}
		}
	}
}
*/