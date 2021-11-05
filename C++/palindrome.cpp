/*	heck for PALINDROME	*/
#include<iostream.h>
#include<string.h>
#include<stdio.h>
#include<conio.h>

void check_pal(char str[20]);

void main()
{
 clrscr();
  char str[20];
  cout<<"Enter the string: ";
  gets(str);
  check_pal(str);
 getch();
}

void check_pal(char str[20])
{
 int i,j,len;
  len=strlen(str);
  j=len-1;
  for(i=0;i<len/2;i++)
  {
    if(str[i]==str[j-i])
     continue;
    else
     break;
  }
  if(i==len/2)
   cout<<"Palindrome";
  else
   cout<<"Non-Palindrome";
}