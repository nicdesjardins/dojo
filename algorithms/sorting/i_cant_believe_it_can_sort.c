#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

void cant_believe_it_can_sort(int arr[]);
//void printArr(int arr[]);
int len(int arr[]);

int main(int argc, char **argv) {

  int arr[] = { 1, 5, 4, 3, 2, 99 };

  printf("len %d\n", (int) (sizeof(arr) / sizeof(arr[0])));
  printf("len: %d\n", len(arr));
  
  /*
  printf("initial array:");
  printArr(arr);
  
  cant_believe_it_can_sort(arr);
  printf("sorted array:");
  printArr(arr);
  */
  return 0;
}

void cant_believe_it_can_sort(int arr[]) {
}

int len(int arr[]) {
  return (int) ( sizeof(arr) / sizeof(arr[0]));
}

/*
void printArr(int arr[]) {
  int i;
  int len = (int) ( sizeof(arr) / sizeof(arr[0]) );
  for(i = 0; i < len; i++) {
    if(i > 0)
      printf(", ");
    printf("%c", arr[i]);
  }
  printf("\n");
}

*/
