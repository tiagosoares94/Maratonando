#include <stdio.h>
 
int main() {
 
    char nome[100];
    double salario,vendas, total;
    printf("");
    scanf("%s",&nome);
    printf("");
    scanf("%lf",&salario);
    printf("");
    scanf("%lf",&vendas);
    total = salario + (vendas*15/100);
    printf("TOTAL = R$ %.2lf\n",total);
 
    return 0;
}