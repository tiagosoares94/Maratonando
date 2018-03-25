#include <stdio.h>
#include <math.h>

int main() {
 
   int a, b, c, aux;
    scanf("%d %d %d", &a, &b, &c);
    aux = ((a+b+abs(a-b))/2);
    aux = ((aux+c+abs(aux-c))/2);
    printf("%d eh o maior\n", aux); 

    return 0;
}