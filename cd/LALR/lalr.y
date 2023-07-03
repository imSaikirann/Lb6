%{
    #include <stdio.h>
%}

%union {
    double dval;
}

%token <dval> DIGIT
%type <dval> expr term factor

%%
line :expr '\n'{
    printf("%d\n",$1);
};

expr :expr '+' term {$$ = $1 + $3;}
|term;

term :term '*' factor {$$ = $1 * $3;}
|factor;

factor:'('expr')' {$$=$2};
|DIGIT;
%%

int main()
{
    yyparse();
}
int yywrap()
{
    return 1;
}
yyerror(char *S)
{
    printf("%s",S);
}