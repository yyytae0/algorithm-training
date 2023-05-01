#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string ntobi(int);
int check(string);

int solution(int n) {
	int answer = 0;
	string s;
	s = ntobi(n);
	return check(s);
}

string ntobi(int n) {
	string s = "";
	while (true)
	{
		if (n == 1)
		{
			s = "1" + s;
			break;
		}
		int d = n % 2;
		s = to_string(d) + s;
		n = n / 2;
	}
	return s;
}

int check(string s) {
	int cnt1 = 0, cnt0 = 0, idx = 0, idx0 = 0, d = 0;
	cout << s << endl;
	for (auto i : s)
	{
		if (i == '1')
		{
			cnt1++;
		}
		else
		{
			cnt0++;
			d = idx0;
			idx0 = idx;
		}
		idx++;
	}
	if (cnt0 == 0 || (cnt0 == 1 && idx0 + 1 == s.length()))
	{
		string ans = "10";
		for (int i = 0; i < cnt1 - 1; i++)
		{
			ans += "1";
		}
	}
	else if(idx0 + 1 == s.length()) {
		s.replace(d, 2, "10");
	}
	else {
		s.replace(idx0, 2, "10");
	}
	int now = 1, ans = 0;
	cout << s.length() << endl;
	cout << s << endl;
	for (int i = s.length() - 1; i >= 0; i--)
	{
		cout << s[i];
		// int n = stoi(dummy) * now;
		now *= 2;
		// ans += num;
	}
	return ans;
}

int main() {
	cout << endl << solution(78);
}