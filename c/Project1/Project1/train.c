#include <stdio.h>

int main() {
	int n, d, sm=0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%1d", &d);
		sm += d;
	}
	printf("%d", sm);
	return 0;
}

int count(char *str) {
	int idx=0;
	while (str[idx] != 0)
	{
		idx++;
	}
	return idx;
}