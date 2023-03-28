/*
#include <iostream>
using namespace std;

int count(char *lst, int *cnt) {
	int idx = 0;
	while (lst[idx])
	{
		int d = (int)lst[idx];
		if (d >= 65 && d <= 90)
		{
			cnt[d - 65] += 1;
		}
		else if (d >= 97 && d <= 122)
		{
			cnt[d - 97] += 1;
		}
		idx++;
	}
	return idx;
}

int main() {
	int c, n, lst[1001], cnt;
	float sm, ans;
	cin >> c;
	for (int i = 0; i < c; i++)
	{
		sm = 0.0;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> lst[j];
			sm += lst[j];
		}
		cnt = 0;
		float avg = sm / n;
		for (int j = 0; j < n; j++)
		{
			if (lst[j] > avg)
			{
				cnt++;
			}
		}
		ans = ((float)cnt / (float)n);
		cout << fixed;
		cout.precision(3);
		cout << ans*100 << '%' << endl;
	}
	return 0;
}
*/