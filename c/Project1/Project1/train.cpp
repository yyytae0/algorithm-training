#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n) {
	int answer = 0;
	string s;
	s = ntobi(n);
	return answer;
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
	int cnt1 = 0, cnt0 = 0, idx = 0, idx0 = 0;;
	for (auto i:s)
	{
		if (i == '1')
		{
			cnt1++;
		}
		else
		{
			cnt0++;
			idx0 = idx;
		}
		idx++;
	}
	if (cnt0 == 0 || (cnt0 == 1 && idx0+1 == s.length()))
	{
		// 1011111...
	}
	else if (true)
	{

	}
}