#include <iostream>
using namespace std;

void qsort(int *a, int start, int end) {
	if (start >= end) {
		return;
	}
	int p = start, i = start+1, j = end;
	int temp;

	while (1){
		while (i<=end && a[i] <= a[p]){
			++i;
		}
		while (j > start && a[j] >= a[p]){
			--j;
		}
		if (i>=j){
			break;
		}

		temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	temp = a[j];
	a[j] = a[p];
	a[p] = temp;

	qsort(a, start, j - 1);
	qsort(a, j + 1, end);
}


int main() {
	int ip, n, d, arr[1000001];
	cin >> ip;
	for (int i = 1; i < ip+1; i++)
	{
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> d;
			arr[j] = d;
		}
		qsort(arr, 0, n);
		cout << '#' << i << ' ' << arr[n / 2];
	}
	return 0;
}