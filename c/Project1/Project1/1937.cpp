/*
#include <iostream>
#include <vector>
using namespace std;
int n, d, way[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} }, ans=0;
vector<int> lst[500];
auto dp = new int[500][500]{};
int dfs(int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> d;
			lst[i].push_back(d);
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			dfs(i, j);
			if (dp[i][j] > ans)
			{
				ans = dp[i][j];
			}
		}
	}
	cout << ans;
	//delete[] lst;
	return 0;
}

int dfs(int si, int sj) {
	if (dp[si][sj] > 0)
	{
		return dp[si][sj];
	}
	int cnt = 0;
	for (auto i:way)
	{
		int ni = si + i[0];
		int nj = sj + i[1];
		if (0<=ni && ni<n && 0<=nj && nj<n && lst[ni][nj] > lst[si][sj])
		{
			int d = dfs(ni, nj);
			if (cnt < d)
			{
				cnt = d;
			}
		}
	}
	dp[si][sj] = cnt+1;
	return cnt+1;
}
*/