/*
#include <iostream>
#include<string>
#include<deque>
using namespace std;

int solution(string s)
{
	deque<char> stk;
	int answer = 0;
	for (auto i:s)
	{
		if (stk.empty())
		{
			stk.push_back(i);
		}
		else
		{
			if (stk.back() == i)
			{
				stk.pop_back();
			}
			else
			{
				stk.push_back(i);
			}
		}
	}
	if (stk.empty())
	{
		answer = 1;
	}

	// [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
	cout << "Hello Cpp" << endl;

	return answer;
}
*/