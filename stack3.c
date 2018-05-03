#include <stdio.h>
#include <stdlib.h>
int makeodd(int number){
    int odd = 1;
    if(number % 2 == 0){
        return number + odd;
    }
    return number;
}
int main(int argc, char* argv[]){
    int result = 0;
    /*
    printf("argc: %d\n", argc);
    for(int i=0; i < argc; i++){
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    if(argc != 2){
        printf("usage: %s number\n", argv[0]);
        exit(-1);
    }

    printf("number +1 = %d\n", atoi(argv[1]) + 1);
*/
    if(argc != 2){
        printf("usage: %s number\n", argv[0]);
        exit(-1);
    }
    result = makeodd(atoi(argv[1]));
    printf("makeodd :%d\n", result);
    return 0;
}