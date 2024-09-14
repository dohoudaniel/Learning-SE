/* stack.h */

struct node_s {
	int data;
	struct node_s *next;
};

typedef struct node_s node;

node *create_stack(void);
void Push(int inputData, node *stack);
int Pop(node *stack);
int top(node *stack);
int is_empty(node *stack);
