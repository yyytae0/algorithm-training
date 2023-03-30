/*
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int n, m, st=0, ed=0;
vector<int> q[1000000];
int** visit = new int*[1000];
int** lst = new int*[1000];
int bfs();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		visit[i] = new int[m] {};
		lst[i] = new int[m] {};
	}
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			if (s[j] == '0')
			{
				lst[i][j] = 0;
			}
			else
			{
				lst[i][j] = 1;
			}
		}
	}
	for (int j = 0; j < m; j++)
	{
		if (lst[0][j] == 0)
		{
			q[ed].push_back(0);
			q[ed].push_back(j);
			ed++;
		}
	}
	if (bfs() == 1)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}
	delete[] visit;
	delete[] lst;
	return 0;
}

int bfs() {
	int way[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
	while (st != ed)
	{
		int v[2] = { q[st][0], q[st][1] };
		st++;
		for (int i = 0; i < 4; i++)
		{
			int nv[2] = { v[0] + way[i][0], v[1] + way[i][1] };
			if (nv[0]>=0 && nv[0]<n && nv[1]>=0 && nv[1]<m && !lst[nv[0]][nv[1]] && !visit[nv[0]][nv[1]])
			{
				visit[nv[0]][nv[1]] = 1;
				q[ed].push_back(nv[0]);
				q[ed].push_back(nv[1]);
				ed++;
			}
			if (nv[0] == n)
			{
				return 1;
			}
		}
	}
	return 0;
}
*/