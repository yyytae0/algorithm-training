/*
#include <iostream>
#include <deque>
using namespace std;
int n;
int lst[3][3]{};
deque<pair<int, int>> q;
int bfs();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> lst[i][j];
		}
	}
	if (lst[0][0] != 0 && bfs() == 1)
	{
		cout << "HaruHaru";
	}
	else
	{
		cout << "Hing";
	}
	return 0;
}


int bfs() {
	int way[2][2] = { {0, 1}, {1, 0} };
	q.push_back(make_pair(0, 0));
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (int i = 0; i < 2; i++)
		{
			int nv[2] = { v[0] + lst[v[0]][v[1]] * way[i][0], v[1] + lst[v[0]][v[1]] * way[i][1] };
			if (nv[0] >= 0 && nv[0] < n && nv[1] >= 0 && nv[1] < n && lst[nv[0]][nv[1]] != 0)
			{
				q.push_back(make_pair(nv[0], nv[1]));
				if (lst[nv[0]][nv[1]] == -1)
				{
					return 1;
				}
			}
		}
	}
	return 0;
}
*/