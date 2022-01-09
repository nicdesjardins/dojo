#define SOMETHING_TO_SAY 0
#define IS_IT_TRUE 1
#define IS_IT_NICE 2
#define IS_IT_NECESSARY 3
#define STFU 4
#define SPEAK_W_LOVE 5

struct node {
  char *text;
  struct node *yes;
  struct node *no;
} nodes[] = {
  [SOMETHING_TO_SAY] = {
			.text = "Do you have something to say?"
			, .yes = &nodes[IS_IT_TRUE]
			, .no = &nodes[STFU]
  } 
  , [IS_IT_TRUE] =  {
		     .text = "is it true?"
		     , .yes = &nodes[IS_IT_NICE]
		     , .no = &nodes[STFU]
  }
  , [IS_IT_NICE] = {
		    .text = "Is it nice?"
		    , .yes = &nodes[SPEAK_W_LOVE]
		    , .no = &nodes[IS_IT_NECESSARY]
  }
  , [IS_IT_NECESSARY] = {
			 .text = "Is it necessary?"
			 , .yes = &nodes[SPEAK_W_LOVE]
			 , .no = &nodes[STFU]
  }
  , [SPEAK_W_LOVE] = { .text = "Speak w/ L.O.V.E." }
  , [STFU] = { .text = "S.T.F.U." }
};
