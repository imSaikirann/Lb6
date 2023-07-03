#include <stdio.h>
#include <string.h>

char stack[50];
int top = -1;

void push(char ch)
{
    top++;
    stack[top] = ch;
}
char pop()
{
    char ch;
    if(top!=-1)
    {
        ch = stack[top];
        top--;
        return ch;
    }
    return '@';
}
void dis()
{
    int i;
    printf("\n\t$");
    for (i = 0; i <= top; i++)
    {
        printf("%c", stack[i]);
    }
}

void main()
{
    int i,del;
    char str[30];
    printf("The grammar is E -> E + E | E * E | E - E | E / E | id\n");
    printf("Enter string: ");
    scanf("%s", str);
    int len = strlen(str);
    printf("%s", str);
    printf("\n\t$");

    for (i = 0; i < len; i++)
    {
        if (str[i] == 'i' && str[i + 1] == 'd')
        {
            
            str[i] = ' ';
            str[i + 1] = 'E';
            dis();
            printf("id");
            push('E');
            dis();
        }
        else if(str[i] == '+' || str[i] == '-' || str[i] == '*' || str[i] == '/')
        {
            printf("hi");
            push(str[i]);
            dis();
        }
    }
    while(1)
    {
        del=pop();
        if(del=='@')
        {
            printf("\n\t$");
            break;
        }
        else if(del=='+' || del=='*'||del=='/' || del=='-')
        {
            int temp = pop();
            if(temp!='E')
            {
                printf("err");
                exit(1);
            }
            else
            {
                push('E');
                dis();
            }
        }
    }

    
}
