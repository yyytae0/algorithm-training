/*
#include <iostream>
using namespace std;

int main() {
	int n, a, b, d;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a >> b;
		int copya = a;
		int copyb = b;
		if (a > b)
		{
			d = a;
			a = b;
			b = d;
		}
		while (b%a != 0)
		{
			d = a;
			a = b % a;
			b = d;
		}
		cout << a * (copya / a) * (copyb / a) << endl;
	}
	return 0;
}
*/