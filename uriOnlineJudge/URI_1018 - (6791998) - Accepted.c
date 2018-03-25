#include <stdio.h>
 
int main() {
 
   int vetor[7] = {100,50,20,10,5,2,1}, vetor2[7]={0,0,0,0,0,0,0}, i, n, n2;
    printf("");
    scanf("%i",&n);
    n2 = n;
    for(i = 0;i<7;i++){
        while(n!=0 && n-vetor[i]>=0){
            n = n - vetor[i];
            vetor2[i] = vetor2[i] + 1;
        }
    }
    printf("%i\n%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00\n",n2,vetor2[0],vetor2[1],vetor2[2],vetor2[3],vetor2[4],vetor2[5],vetor2[6]);

 
    return 0;
}