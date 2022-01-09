#include <stdio.h>
#include <string.h>

#define SOMETHING_TO_SAY 0
#define IS_IT_TRUE 1
#define SAY_IT 2
#define KEEP_TO_YOURSELF 3

struct node {
  char *text;
  struct node *yes;
  struct node *no;
} nodes[] = {
  { "do you have something to say?" } // 0
  , { "is it true?" } // 1
  , { "say it" } // 2
  , { "keep it to yourself" } // 3
};

int main(void) {

  // do you have something to say?
  nodes[SOMETHING_TO_SAY].yes = &nodes[IS_IT_TRUE];
  nodes[SOMETHING_TO_SAY].no = &nodes[KEEP_TO_YOURSELF];

  // is it true?
  nodes[IS_IT_TRUE].yes = &nodes[SAY_IT];
  nodes[IS_IT_TRUE].no = &nodes[KEEP_TO_YOURSELF];

}
