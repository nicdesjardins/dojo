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

void displayNode(struct node *node, int level);
void tabs(int num, char *t);

int main(void) {

  // do you have something to say?
  nodes[SOMETHING_TO_SAY].yes = &nodes[IS_IT_TRUE];
  nodes[SOMETHING_TO_SAY].no = &nodes[KEEP_TO_YOURSELF];

  // is it true?
  nodes[IS_IT_TRUE].yes = &nodes[SAY_IT];
  nodes[IS_IT_TRUE].no = &nodes[KEEP_TO_YOURSELF];
 
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
