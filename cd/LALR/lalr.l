%{
    #include <stdio.h>
    #include "ytab.h"
%}
%%
[0-9]+{yyval.dval = atof(yytext);
return DIGIT;
}
\n\. return yytext[0];
%%