#include <stdio.h>

int main() {
	int n, m, a, b;
	int lst[100];
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		lst[i] = i + 1;
	}
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);
		for (int i = a-1; i < b; i++)
		{
			printf("");
		}
	}
	return 0;
}