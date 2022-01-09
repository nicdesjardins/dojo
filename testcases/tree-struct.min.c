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
  [SOMETHING_TO_SAY] = {
    .text = "do you have something to say?"
    , .yes = &nodes[IS_IT_TRUE]
    , .no = &nodes[KEEP_TO_YOURSELF]
  }
  
  , [IS_IT_TRUE] =  {
    .text = "is it true?"
    , .yes = &nodes[SAY_IT]
    , .no = &nodes[KEEP_TO_YOURSELF]
  }
  
  , [SAY_IT] = { .text = "say it" }
  , [KEEP_TO_YOURSELF] = { .text = "keep it to yourself" }
};

int main(void) {


}
