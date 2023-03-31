/*
#include <iostream>
#include <deque>
//const int mx = 100001;
using namespace std;
int h, y, dp[11]{}, money[6] = {0, 5, 0, 20, 0, 35};
deque<pair<int, int>> q;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> h >> y;
	for (int i = 0; i < y+1; i++)
	{
		dp[i] = h;
	}
	for (int i = 0; i < y+1; i++)
	{
		int mx = dp[i];
		for (int j = 1; j < 6; j=j+2)
		{
			if (i+j < y+1)
			{
				int d = dp[i] + (dp[i] * money[j]) / 100;
				if (d > dp[i + j])
				{
					dp[i + j] = d;
				}
			}
		}
	}
	cout << dp[y];
	return 0;
}
*/