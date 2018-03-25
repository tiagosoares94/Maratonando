#include <stdio.h>
 
int main() {
 
    int km;
    double comb, total;
    printf("");
    scanf("%i",&km);
    printf("");
    scanf("%lf",&comb);
    total = km / comb;
    printf("%.3lf km/l\n",total);
 
    return 0;
}