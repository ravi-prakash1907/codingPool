// Swap 2 numbers

#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
   int num,mod,new_num=0;
   cout<<"Enter a number:";
   cin>>num;
   while(num!=0)
   {
     mod=num%10;
     new_num=new_num*10+mod;
     num/=10;
   }
   cout<<"The reversed form of the entered no. is: "<<new_num;
  getch();
}