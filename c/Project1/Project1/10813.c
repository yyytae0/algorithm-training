/*
#include <stdio.h>

int main() {
	int n, m, a, b, d;
	int lst[101];
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		lst[i] = i + 1;
	}
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);
		d = lst[a - 1];
		lst[a - 1] = lst[b - 1];
		lst[b - 1] = d;
	}
	for (int i = 0; i < n; i++)
	{
		printf("%d ", lst[i]);
	}
	return 0;
}
*/