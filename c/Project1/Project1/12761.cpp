/*
#include <iostream>
#include <deque>
const int mx = 100001;
using namespace std;
int a, b, n, m;
int lst[mx]{};
deque<int> q;
int bfs();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> a >> b >> n >> m;
	lst[n] = 1;
	cout << bfs() - 1;
	return 0;
}


int bfs() {
	q.push_back(n);
	while (!q.empty())
	{
		int v = q.front();
		q.pop_front();
		int way[8] = {v+1, v-1, v*a, v*b, v+a, v-a, v+b, v-b};
		for (int i = 0; i < 8; i++)
		{
			int nv = way[i];
			if (nv>=0 && nv<mx && !lst[nv])
			{
				q.push_back(nv);
				lst[nv] = lst[v] + 1;
				if (nv == m)
				{
					return lst[nv];
				}
			}
		}
	}
	return 0;
}
*/