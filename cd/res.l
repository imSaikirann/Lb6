%{
#include<stdio.h>
%}
%%
struct|if|break|continue|do|while|void|float|int|short|long|double|sizeof|goto|static|char{printf("valid res words"):}
[a-z A-Z _]+[a-z A_Z 0-9 _]*{printf("valid res");}
[0-9]+[a-z A-Z 0-9 _]*{printf("not valid");}
%%
int yywrap(void){ }
int main()
{
    yylex();
    return 0;
}