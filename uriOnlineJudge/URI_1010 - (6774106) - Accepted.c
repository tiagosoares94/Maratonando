#include <stdio.h>
 
int main() {
 
    int codp1, np1,codp2,np2;
    float vp1,vp2,total;
    printf("");
    scanf("%i %i %f",&codp1,&np1,&vp1);
    printf("");
    scanf("%i %i %f",&codp2,&np2,&vp2);
    total = (np1*vp1)+(np2*vp2);
    printf("VALOR A PAGAR: R$ %.2f\n",total);
 
    return 0;
}