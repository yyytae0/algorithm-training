/*
#include <iostream>
using namespace std;

char dummy[51], grade[3];
double score, ans, total = 0.0, cnt=0.0;


int check() {
	if (grade[0] == 'P') {
		return 0;
	}
	else {
		cnt += score;
		if (grade[0] == 'A') {
			if (grade[1] == '+') {
				total += score * 4.5;
			}
			else {
				total += score * 4.0;
			}
		}
		else if (grade[0] == 'B') {
			if (grade[1] == '+') {
				total += score * 3.5;
			}
			else {
				total += score * 3.0;
			}
		}
		else if (grade[0] == 'C') {
			if (grade[1] == '+') {
				total += score * 2.5;
			}
			else {
				total += score * 2.0;
			}
		}
		else if (grade[0] == 'D') {
			if (grade[1] == '+') {
				total += score * 1.5;
			}
			else {
				total += score * 1.0;
			}
		}
	}
	return 0;
}


int main() {
	for (int i = 0; i < 20; i++)
	{
		cin >> dummy >> score >> grade;
		check();
	}
	ans = total / cnt;
	cout << ans;
	return 0;
}
*/