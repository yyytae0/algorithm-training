/*
#include <iostream>
using namespace std;

int main() {
	int n, cnt, lst[10000], sm, idx;
	while (1)
	{
		cin >> n;
		if (n == -1){
			break;
		}
		sm = 0;
		cnt = 0;
		idx = 0;
		for (int i = 1; i < n; i++)
		{
			if (n%i == 0)
			{
				sm += i;
				lst[idx] = i;
				idx++;
			}
			if (sm > n){
				break;
			}
		}
		if (sm == n)
		{
			cout << n << " = " << lst[0];
			for (int i = 1; i < idx; i++)
			{
				cout << " + " << lst[i];
			}
		}
		else
		{
			cout << n << " is NOT perfect.";
		}
		cout << '\n';
	}
	return 0;
}
*/