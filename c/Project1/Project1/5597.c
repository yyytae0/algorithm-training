/*
#include <stdio.h>

int main() {
	int a, mn=0, mx;
	int lst[30];
	for (int i = 0; i < 30; i++)
	{
		lst[i] = 1;
	}
	for (int i = 0; i < 28; i++)
	{
		scanf("%d", &a);
		lst[a - 1] = 0;
	}
	for (int i = 0; i < 30; i++){
		if (lst[i]) {
			if (mn > 0) {
				mx = i + 1;
			}
			else
			{
				mn = i + 1;
			}
		}
	}
	printf("%d\n%d", mn, mx);
	return 0;
}
*/