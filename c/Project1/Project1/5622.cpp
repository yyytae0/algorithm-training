/*
#include <iostream>
using namespace std;
int main() {
	int word[26] = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9};
	int sm=0, idx = 0;
	char str[16];
	cin >> str;
	while (str[idx] != 0)
	{
		int d = (int)str[idx];
		sm += word[d - 65]+1;
		idx++;
	}
	cout << sm;
	return 0;
}
*/