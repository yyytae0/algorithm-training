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
	int idx = 0;
	char lst[1000001];
	int cnt[26];
	for (int i = 0; i < 26; i++)
	{
		cnt[i] = 0;
	}
	cin.getline(lst, 1000001);
	int n = count(lst, cnt);
	int mx = 0;
	char mxc;
	for (int i = 0; i < 26; i++)
	{
		if (cnt[i] > mx)
		{
			mx = cnt[i];
			mxc = char(i + 65);
		}
		else if (cnt[i] == mx)
		{
			mxc = '?';
		}
	}
	cout << mxc;
	return 0;
}
*/