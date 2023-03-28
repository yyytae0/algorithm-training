/*
#include <iostream>
using namespace std;
int main() {
	char arr[1000005];
	int idx = 0, cnt=0;
	cin.getline(arr, 1000005);
	if (arr[0] == 32){
		idx++;
		if (arr[idx] == 0)
		{
			cout << 0;
			return 0;
		}
	}
	while (arr[idx] != 0)
	{
		if (arr[idx] == 32)
		{
			cnt++;
		}
		idx++;
	}
	if (arr[idx-1] == 32)
	{
		cnt--;
	}
	cout << cnt+1;
	return 0;
}
*/