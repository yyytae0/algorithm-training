/*
#include <iostream>
using namespace std;

int main() {
	int a, b, c, d;
	while (1)
	{
		cin >> a >> b >> c;
		if (a == 0)
		{
			break;
		}
		if (a >= b and a >= c)
		{
			d = a;
			a = c;
			c = d;
		}
		else if (b >= a and b >= c)
		{
			d = b;
			b = c;
			c = b;
		}
		if (a + b > c)
		{
			if (a == b && a == c)
			{
				cout << "Equilateral";
			}
			else if (a == b || b == c || a == c)
			{
				cout << "Isosceles";
			}
			else
			{
				cout << "Scalene";
			}
		}
		else
		{
			cout << "Invalid";
		}
		cout << '\n';
	}
	return 0;
}
*/