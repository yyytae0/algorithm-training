/*
#include<string>
#include <iostream>
#include <deque>
using namespace std;

bool solution(string s)
{
	deque<int> q;
	for (auto i : s)
	{
		if (i == '(')
		{
			q.push_back(1);
		}
		else
		{
			if (q.empty())
			{
				return false;
			}
			q.pop_back();
		}
	}
	if (q.empty())
	{
		return true;
	}
	return false;
}
*/