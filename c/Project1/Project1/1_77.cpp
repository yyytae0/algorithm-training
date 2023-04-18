#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
	vector<int> answer;
	for (vector<string> i : photo)
	{
		int ans = 0;
		for (auto j : i)
		{
			for (int idx = 0; idx < name.size(); idx++)
			{
				if (name[idx] == j)
				{
					ans += yearning[idx];
					break;
				}
			}
		}
		answer.push_back(ans);
	}
	return answer;
}