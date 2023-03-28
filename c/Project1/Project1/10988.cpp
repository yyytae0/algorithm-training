/*
#include <iostream>
using namespace std;


int count(char *lst) {
	int idx = 0;
	while (lst[idx])
	{
		idx++;
	}
	return idx;
}

int main() {
	int idx = 0;
	char lst[101];
	cin.getline(lst, 101);
	int n = count(lst);
	for (int i = 0; i < n/2; i++)
	{
		if (lst[i] != lst[n-i-1])
		{
			cout << '0';
			return 0;
		}
	}
	cout << '1';
	return 0;
}
*/