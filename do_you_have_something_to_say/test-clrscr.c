#include <stdio.h>
#include <stdlib.h>

int main(void) {

  printf("test\n");

  int c;
  c = getchar();
  system("clear");
  //printf("\033[2J");
  //fputs("\x1b[2J", stdout);
  //fflush(stdout);

  printf("test 2\n");

  return 0;
  
}
