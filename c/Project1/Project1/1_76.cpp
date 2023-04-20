/*
#include <string>
#include <vector>
using namespace std;

int solution(int n, int m, vector<int> section) {
	int answer = 0;
	int now = 0;
	for (int i = 0; i < section.size(); i++)
	{
		if (section[i] > now)
		{
			answer++;
			now = section[i] + m - 1;
		}
		if (now >= n)
		{
			return answer;
		}
	}
	return answer;
}
*/