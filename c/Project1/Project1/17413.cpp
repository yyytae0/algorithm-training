/*
#include <iostream>
#include <string>
const int mx = 100001;
using namespace std;
char dummy[mx]{};
int flag = 0;
void print(int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string s;
	getline(cin, s);
	int n = s.length();
	int cnt = 0, idx = 0;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == '<')
		{
			print(cnt);
			cout << '<';
			cnt = 0;
			flag = 1;
		}
		else if (s[i] == '>')
		{
			print(cnt);
			cout << '>';
			cnt = 0;
			flag = 0;
		}
		else if (flag == 0 && s[i] == ' ')
		{
			print(cnt);
			cout << ' ';
			cnt = 0;
		}
		else
		{
			dummy[cnt++] = s[i];
		}
	}
	print(cnt);
	return 0;
}

void print(int cnt) {
	if (flag == 1)
	{
		for (int i = 0; i < cnt; i++)
		{
			cout << dummy[i];
		}
	}
	else
	{
		for (int i = cnt - 1; i > -1; i--)
		{
			cout << dummy[i];
		}
	}

}
*/