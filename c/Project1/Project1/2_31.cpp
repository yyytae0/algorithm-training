/*
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
	vector<int> answer;
	for (int i = 1; i < yellow + 1; i++)
	{
		if (yellow % i == 0)
		{
			if (yellow/i < i)
			{
				break;
			}
			int dummy = (i+2)*2 + (yellow/i + 2)*2 - 4;
			if (dummy == brown)
			{
				answer.push_back(yellow / i + 2);
				answer.push_back(i + 2);
			}
		}
	}
	return answer;
}
*/