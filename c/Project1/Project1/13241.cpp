/*
#include <iostream>
using namespace std;

int main() {
	long long int a, b, d;
	cin >> a >> b;
	long long int copya = a;
	long long int copyb = b;
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

	return 0;
}
*/