/*
#include <iostream>
using namespace std;
int prime[1000001] = {};

int main() {
	for (int i = 4; i < 1000001; i=i+2)
	{
		prime[i] = 1;
	}
	for (int i = 3; i < 1001; i=i+2)
	{
		if (prime[i] == 0)
		{
			for (int j = 3; j < 500001; j++)
			{
				if (i*j > 1000000)
				{
					break;
				}
				else
				{
					prime[i*j] = 1;
				}
			}
		}
	}
	int ip, n;
	cin >> ip;
	for (int i = 0; i < ip; i++)
	{
		cin >> n;
		int cnt = 0;
		for (int i = 2; i < n/2+1; i++)
		{
			if (prime[i] == 0)
			{
				if (prime[n-i] == 0)
				{
					cnt++;
				}
			}
		}
		cout << cnt << endl;
	}
}
*/