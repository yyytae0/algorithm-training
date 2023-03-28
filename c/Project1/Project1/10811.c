/*
#include <stdio.h>

int main() {
	int n, m, a, b, d, idx;
	int lst[100];
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		lst[i] = i + 1;
	}

	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);
		idx = 0;
		for (int j = a-1; j < (b+a-1)/2; j++)
		{
			d = lst[j];
			lst[j] = lst[b - idx - 1];
			lst[b - idx - 1] = d;
			idx++;
		}
	}
	for (int j = 0; j < n; j++)
	{
		printf("%d ", lst[j]);
	}

	return 0;
}
*/