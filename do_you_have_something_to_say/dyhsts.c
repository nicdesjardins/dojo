#include <stdio.h>
#include <stdlib.h>

#include "nodes.h"

int main(void) {

  struct node *curr;
  curr = &nodes[SOMETHING_TO_SAY];

  int c = 0;
  while(1) {
    
    if(c != '\n')
      printf("\n%s\n(y, n, or q for quit)\n\n", curr->text);

    c = getchar();

    switch(c) {
    case 'y':
      curr = curr->yes;
      break;
    case 'n':
      curr = curr->no;
      break;
    case 'q':
      printf("kthxbai!\n");
      return 0;
    case '\n':
      break;
    default:
	printf("invalid option: %c\n", c);
	break;
    }

    if (isOutcome(curr)) {
      printf("\n%s\n\n", curr->text);
      return 0;
    }
  }
  
  return 0;
  
}
