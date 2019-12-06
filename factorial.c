#include<stdio.t>
void main()
{
 int i=1,fact=1,n;
 print("Enter number:\n");
 scanf("%d",&n);
 while(i<=n)
 {
  fact=fact*i;
  i++;
 }
 printf("%d",fact);
}
