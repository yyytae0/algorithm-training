/*
#include <stdio.h>

int main() {
	int n;
	float lst[1000], sm=0.0, mx=0.0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%f", &lst[i]);
		if (mx < lst[i])
		{
			mx = lst[i];
		}
	}
	for (int i = 0; i < n; i++)
	{
		lst[i] = (lst[i] / mx) * 100;
		sm += lst[i];
	}
	printf("%f", sm / n);
	return 0;
}
*/