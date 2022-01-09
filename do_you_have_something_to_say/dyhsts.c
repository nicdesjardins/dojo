#include <stdio.h>
#include <stdlib.h>

struct node {
  char *text;
  struct node *yes;
  struct node *no;
} nodes[] = {
  { "Do you have something to say?" } // 0
  , { "Is it true?" } // 1
  , { "Is it nice?" } // 2
  , { "Is it necessary?" } // 3
  , { "S.T.F.U.", 0, 0 } // 4
  , { "Speak with L.O.V.E.", 0, 0 } // 5
};

void makeNodeConnections(void);

int main(void) {

  makeNodeConnections();
  system("clear");
  
  while(1) {  
    
    struct node *curr;
    curr = &nodes[0];

    int c = 0;
    while(1) {

      if (curr->yes == 0) {
	printf("\n%s\n\n", curr->text);
	//return 0;
	break;
      }

      if(c != '\n')
	printf("\n%s\n(y, n, or q for quit)\n\n", curr->text);

      c = getchar();
      if (c == 'y') {
	curr = curr->yes;
	continue;
      }

      else if (c == 'n') {
	curr = curr->no;
	continue;
      }

      else if (c == 'q') {
	printf("kthxbai!\n");
	return 0;
      }

      else if (c == '\n') {
	continue;
      }

      else {
	printf("invalid option: %c\n", c);
	continue;
      }  
    }
  }
  
  return 0;
  
}

void makeNodeConnections(void) {
  // do you have something to say?
  nodes[0].yes = &nodes[1]; // yes -> is it true?
  nodes[0].no = &nodes[4]; // no -> stfu

  // is it true?
  nodes[1].yes = &nodes[2]; // yes -> is it nice?
  nodes[1].no = &nodes[4]; // no -> stfu

  // is it nice?
  nodes[2].yes = &nodes[5]; // yes -> speak w/ love
  nodes[2].no = &nodes[3]; // no -> is it necessary?

  // is it necessary?
  nodes[3].yes = &nodes[5]; // yes -> speak w/ love
  nodes[3].no = &nodes[4]; // no -> stfu
}
