///////////////////////////////////////
/*									 */
/*  CS124 Programming Assignment 3   */
/*     Curren Iyer & Paul Lisker     */
/*			 April 25, 2016			 */
/*	   								 */
///////////////////////////////////////


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <time.h>

int ARRAY_SIZE = 100;

//Compare function for qsort to sort descending
int cmp(const void* a, const void* b){
	long long int* x = (long long int*) a;
	long long int* y = (long long int*) b;

	if (*y > *x){
		return 1;
	}
	if (*x > *y){
		return -1;
	}
	else{
		return 0;
	}
}

// Karmarkar-Karp
int kk(long long int* A){
	qsort(A, ARRAY_SIZE, sizeof(long long int), cmp);
	while(A[1] != 0){
		A[0] = A[0]-A[1];
		A[1] = 0;
		qsort(A, ARRAY_SIZE, sizeof(long long int), cmp);
	}
	return A[0];
}

int main(int argc, char *argv[]){
    if(argc != 2){
        printf("Wrong number of arguments!\n");
        return 1;
    }
    
    long long int* A;
    A = (long long int*) malloc(ARRAY_SIZE*sizeof(long long int));
    
    int i = 0;
    
    const char* filename = argv[1];
    
    FILE* file = fopen(filename, "r");
    
    long long int number;
    while(fscanf(file, "%lld", &number) > 0) {
        A[i]=number;
        i++;
    }
    fclose(file);

    int residue = kk(A);
    printf("%i\n", residue);
    return 0;
}