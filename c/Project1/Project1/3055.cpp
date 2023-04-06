/*
#include <iostream>
#include <vector>
#include <deque>
const int mx = 100001;
using namespace std;
int n, m, si, sj, ei, ej;
char d;
vector<int> lst[50];
deque<pair<int, int>> wq;
deque<pair<int, int>> q;
int way[4][2] = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };
void water();
int move();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> d;
			if (d == 'D')
			{
				ei = i;
				ej = j;
				lst[i].push_back(0);
			}
			else if (d == 'S')
			{
				si = i;
				sj = j;
				lst[i].push_back(0);
				q.push_back(make_pair(si, sj));
			}
			else if (d == '.')
			{
				lst[i].push_back(0);
			}
			else if (d == '*')
			{
				wq.push_back(make_pair(i, j));
				lst[i].push_back(1);
			}
			else {
				lst[i].push_back(-1);
			}
		}
	}
	water();
	int ans = move();
	if (ans == -1)
	{
		cout << "KAKTUS";
	}
	else
	{
		cout << ans;
	}
	return 0;
}

void water() {
	while (!wq.empty()) {
		int v[2] = { wq.front().first, wq.front().second };
		wq.pop_front();
		for (auto i : way)
		{
			int nv[2] = { v[0] + i[0], v[1] + i[1] };
			if (0 <= nv[0] && nv[0] < n && 0 <= nv[1] && nv[1] < m && lst[nv[0]][nv[1]] != -1)
			{
				if (lst[nv[0]][nv[1]] == 0 && (nv[0] != ei || nv[1] != ej)) {
					wq.push_back(make_pair(nv[0], nv[1]));
					lst[nv[0]][nv[1]] = lst[v[0]][v[1]] + 1;
				}
			}
		}
	}
}

int move() {
	lst[si][sj] = 1;
	while (!q.empty())
	{
		int v[2] = { q.front().first, q.front().second };
		q.pop_front();
		for (auto i : way)
		{
			int nv[2] = { v[0] + i[0], v[1] + i[1] };
			if (nv[0] == ei && nv[1] == ej)
			{
				return lst[v[0]][v[1]];
			}
			if (0 <= nv[0] && nv[0] < n && 0 <= nv[1] && nv[1] < m && lst[nv[0]][nv[1]] != -1)
			{
				if (lst[nv[0]][nv[1]] == 0 || lst[nv[0]][nv[1]] > lst[v[0]][v[1]] + 1)
				{
					q.push_back(make_pair(nv[0], nv[1]));
					lst[nv[0]][nv[1]] = lst[v[0]][v[1]] + 1;
				}
			}
		}
	}
	return -1;
}
*/