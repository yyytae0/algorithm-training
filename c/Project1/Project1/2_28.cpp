/*
#include <string>
#include <vector>
using namespace std;
vector<int> dp;

int solution(int n) {
	int answer = 0;
	dp.push_back(0);
	dp.push_back(1);
	for (int i = 2; i < n+1; i++)
	{
		dp.push_back((dp[i - 2] + dp[i - 1])%1234567);
	}
	answer = dp[n];
	return answer;
}
*/