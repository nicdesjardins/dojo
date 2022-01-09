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

void displayNode(struct node *node, int level);
void tabs(int num, char *t);

int main(void) {
  int level = 0;
  displayNode(&nodes[0], level);
}

void displayNode(struct node *node, int level) {
  char t[16];
  tabs(level, t);
  printf("%s%s\n", t, node->text);

  if(node->yes != NULL){
    printf("\n%syes: \n", t);
    displayNode((node->yes), level+1);
  }
  
  if(node->no != NULL) {
    printf("\n%sno: \n", t);
    displayNode(node->no, level+1);
  }
}

void tabs(int num, char *t) {
  memset(t, ' ', num * 2);
  t[num*2] = '\0';
}
