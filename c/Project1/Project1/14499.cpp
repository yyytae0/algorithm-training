/*
#include <iostream>
#include <vector>
using namespace std;
int n, m, x, y, nx, ny, k, d, now[3] = { 1, 3, 5 }, num[7]{}, dr[4][2] = { {1, 0}, {0, 1}, {0, -1}, {-1, 0} };
vector<int> lst[20];
void move(int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m >> x >> y >> k;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> d;
			lst[i].push_back(d);
		}
	}
	for (int i = 0; i < k; i++)
	{
		cin >> d;
		move(d);
	}
	return 0;
}

void move(int d) {
	nx = x + dr[d % 4][0];
	ny = y + dr[d % 4][1];
	if (0 > nx || nx >= n || ny < 0 || ny >= m) {
		return;
	}
	if (d == 1)
	{
		int d1 = 7 - now[1], d2 = now[0], d3 = now[2];
		now[0] = d1;
		now[1] = d2;
		now[2] = d3;
	}
	else if (d == 2)
	{
		int d1 = now[1], d2 = 7 - now[0], d3 = now[2];
		now[0] = d1;
		now[1] = d2;
		now[2] = d3;
	}
	else if (d == 3)
	{
		int d1 = now[2], d2 = now[1], d3 = 7 - now[0];
		now[0] = d1;
		now[1] = d2;
		now[2] = d3;
	}
	else
	{
		int d1 = 7 - now[2], d2 = now[1], d3 = now[0];
		now[0] = d1;
		now[1] = d2;
		now[2] = d3;
	}
	x = nx;
	y = ny;
	if (lst[x][y] == 0)
	{
		lst[x][y] = num[7 - now[0]];
	}
	else
	{
		num[7 - now[0]] = lst[x][y];
		lst[x][y] = 0;
	}
	cout << num[now[0]] << endl;
}
*/