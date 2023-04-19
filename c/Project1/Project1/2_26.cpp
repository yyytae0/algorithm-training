#include <iostream>
#include <string>
#include <vector>
using namespace std;
int ans = 0;
string change(string);
vector<int> d;

vector<int> solution(string s) {
	vector<int> answer;
	int cnt = 0;
	while (s != "1")
	{
		cnt++;
		s = change(s);
	}
	answer.push_back(cnt);
	answer.push_back(ans);
	return answer;
}

string change(string s) {
	int cnt = 0;
	for (auto i : s)
	{
		if (i == '1')
		{
			cnt++;
		}
		else
		{
			ans++;
		}
	}
	string ns = "";
	while (cnt > 1)
	{
		string d = to_string(cnt % 2);
		ns = d + ns;
		cnt = cnt / 2;
	}
	return "1" + ns;
}
