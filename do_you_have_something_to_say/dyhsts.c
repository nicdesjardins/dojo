#include <stdio.h>
#include <stdlib.h>

#include "nodes.h"

int main(void) {

  system("clear");

  struct node *curr;
  curr = &nodes[SOMETHING_TO_SAY];

  int c = 0;
  while(1) {

    if(c != '\n')
      printf("\n%s\n(y, n, or q for quit)\n\n", curr->text);

    c = getchar();
    
    if (c == 'y') {
      curr = curr->yes;
    }

    else if (c == 'n') {
      curr = curr->no;
    }

    else if (c == 'q') {
      printf("kthxbai!\n");
      return 0;
    }

    else {
      if(c != '\n')
	printf("invalid option: %c\n", c);
    }

    if (curr->yes == NULL) {
      printf("\n%s\n\n", curr->text);
      return 0;
    }
  }
  
  return 0;
  
}
