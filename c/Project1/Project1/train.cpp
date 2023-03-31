#include <iostream>
#include <vector>
const int mx = 100001;
using namespace std;
int n, m, d, ans=0;
vector<int> lst[500];
int arr[9]{};
void check(int, int);
int max(int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> d;
			lst[i].push_back(d);
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			check(i, j);
		}
	}
	cout << ans;
	return 0;
}

void check(int a, int b) {
	if (b+4 <= m)
	{
		arr[0] = ans;
		arr[1] = lst[a][b] + lst[a][b + 1] + lst[a][b + 2] + lst[a][b + 3];
		ans = max(2);
	}
	if (a+4 <= n)
	{
		arr[0] = ans;
		arr[1] = lst[a][b] + lst[a + 1][b] + lst[a + 2][b] + lst[a + 3][b];
		ans = max(2);
	}
	if (b+2 <= m && a+2 <= n)
	{
		arr[0] = ans;
		arr[1] = lst[a][b] + lst[a + 1][b] + lst[a][b + 1] + lst[a + 1][b + 1];
		ans = max(2);
	}
	if (b+2 <= m && a+3 <= n)
	{
		arr[0] = ans;
		arr[1] = lst[a][b] + lst[a + 1][b] + lst[a + 2][b] + lst[a + 2][b + 1];
		arr[2] = lst[a][b] + lst[a][b + 1] + lst[a + 1][b + 1] + lst[a + 2][b + 1];
		arr[3] = lst[a][b] + lst[a + 1][b] + lst[a + 2][b] + lst[a][b + 1];
		arr[4] = lst[a][b + 1] + lst[a + 1][b + 1] + lst[a + 2][b + 1] + lst[a + 2][b];
		arr[5] = lst[a][b + 1] + lst[a + 1][b + 1] + lst[a + 2][b + 1] + lst[a + 1][b];
		arr[6] = lst[a][b] + lst[a + 1][b] + lst[a + 2][b] + lst[a + 1][b + 1];
		arr[7] = lst[a][b] + lst[a + 1][b] + lst[a + 1][b + 1] + lst[a + 2][b + 1];
		arr[8] = lst[a][b + 1] + lst[a + 1][b + 1] + lst[a + 1][b] + lst[a + 2][b];
		ans = max(9);
	}
	if (b+3<=m && a+2<=n)
	{
		arr[0] = ans;
		arr[1] = lst[a][b] + lst[a + 1][b] + lst[a + 1][b + 1] + lst[a + 1][b + 2];
		arr[2] = lst[a][b] + lst[a][b + 1] + lst[a][b + 2] + lst[a + 1][b + 2];
		arr[3] = lst[a][b] + lst[a + 1][b] + lst[a][b + 1] + lst[a][b + 2];
		arr[4] = lst[a + 1][b] + lst[a + 1][b + 1] + lst[a + 1][b + 2] + lst[a][b + 2];
		arr[5] = lst[a][b] + lst[a + 1][b + 1] + lst[a][b + 1] + lst[a][b + 2];
		arr[6] = lst[a][b + 1] + lst[a + 1][b] + lst[a + 1][b + 1] + lst[a + 1][b + 2];
		arr[7] = lst[a][b] + lst[a][b + 1] + lst[a + 1][b + 1] + lst[a + 1][b + 2];
		arr[8] = lst[a + 1][b] + lst[a + 1][b + 1] + lst[a][b + 1] + lst[a][b + 2];
		ans = max(9);
	}
}

int max(int l) {
	int dummy = 0;
	for (int i = 0; i < l; i++)
	{
		if (arr[i] > dummy)
		{
			dummy = arr[i];
		}
	}
	return dummy;
}