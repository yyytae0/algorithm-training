/*
#include <stdio.h>

int main() {
	int ans[26], d;
	char str[101];
	scanf("%s", str);
	for (int i = 0; i < 26; i++)
	{
		ans[i] = -1;
	}
	for (int i = 0; str[i]; i++)
	{
		d = (int)str[i] - 97;
		if (ans[d] == -1)
		{
			ans[d] = i;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		printf("%d ", ans[i]);
	}
	return 0;
}
*/