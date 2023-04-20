/*
#include <string>
#include <vector>
#include <cctype>
using namespace std;

string solution(string s) {
	string answer = "";
	int idx = 0, flag = 0;
	char d = toupper(s[idx]);
	answer.push_back(d);
	for (int i = 1; i < s.size(); i++)
	{
		if (s[i] == ' ')
		{
			flag = 1;
			answer.push_back(' ');
		}
		else
		{
			if (flag)
			{
				answer.push_back((char)toupper(s[i]));
				flag = 0;
			}
			else
			{
				answer.push_back((char)tolower(s[i]));
			}
		}
	}
	return answer;
}
*/