#include <stdio.h>
 
int main() {
 
    int tempo,vm;
    double dist,litros;
    printf("");
    scanf("%i",&tempo);
    printf("");
    scanf("%i",&vm);

    dist = vm*tempo;
    litros = dist/12;

    printf("%.3lf\n",litros);
 
    return 0;
}