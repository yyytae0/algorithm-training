/*
#include <iostream>
#include <vector>
#include <deque>
const int mx = 1000000;
using namespace std;
int n;
int lst[125][125]{}, visit[125][125]{}, way[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
void bfs();
deque<pair<int, int>> q;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	int p = 1;
	while (n > 0)
	{
		fill(&visit[0][0], &visit[n - 1][n], mx);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> lst[i][j];
			}
		}
		visit[0][0] = lst[0][0];
		bfs();
		cout << "Problem " << p++ << ": " << visit[n - 1][n - 1] << endl;
		cin >> n;
	}

	return 0;
}

void bfs() {
	q.push_back(make_pair(0, 0));
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (auto i : way)
		{
			int nv[2] = { v[0] + i[0], v[1] + i[1] };
			if (0<=nv[0] && nv[0]<n && 0<=nv[1] && nv[1]<n)
			{
				int d = visit[v[0]][v[1]] + lst[nv[0]][nv[1]];
				if (d < visit[nv[0]][nv[1]])
				{
					q.push_back(make_pair(nv[0], nv[1]));
					visit[nv[0]][nv[1]] = d;
				}
			}
		}
	}
}
*/