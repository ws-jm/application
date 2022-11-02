// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;

int main()
{

	int decimalnum, remainder, quotient, octalnum = 0;
	int octalNumber[100], i = 1, j, num,c_num ,view;
	float poinbelow;
	printf("Enter the decimal number: ");
	scanf("%d.%d", &decimalnum, &num);
	quotient = decimalnum;
	//Storing remainders until number is equal to zero
	while (quotient != 0)
	{
		octalNumber[i++] = quotient % 8;
		quotient = quotient / 8;
	}

	//Converting stored remainder values in corresponding octal number
	for (j = i - 1; j > 0; j--)
		octalnum = octalnum * 10 + octalNumber[j];

	poinbelow = num;
	while (num > 0) {
		num /= 10;
		poinbelow /= 10;
	}
	int count = 6;

	printf("Equivalent octal value of decimal no %d is: %d", decimalnum, octalnum);

	printf(".");
	while (count)
	{
		poinbelow *= 8;
		view = poinbelow;
		int roop = view % 8;
		poinbelow -= view;
		printf("%d", roop);
		count--;

	}
	return 0;

}


