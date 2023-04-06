/*
#include <iostream>
#include <vector>
using namespace std;
int n, m, a, b, v[2000]{};
vector<int> lst[2000];
int check();
int dfs(int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b;
		lst[a].push_back(b);
		lst[b].push_back(a);
	}
	cout << check();
	return 0;
}

int dfs(int now, int cnt) {
	if (cnt == 4)
	{
		return 1;
	}
	for (auto i:lst[now])
	{
		if (v[i] == 0)
		{
			v[i] = 1;
			if (dfs(i, cnt + 1))
			{
				return 1;
			}
			v[i] = 0;
		}
	}
	return 0;
}

int check() {
	for (int i = 0; i < n; i++)
	{
		v[i] = 1;
		if (dfs(i, 0)) {
			return 1;
		}
		v[i] = 0;
	}
	return 0;
}
*/