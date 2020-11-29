#include <stdio.h>
#include <stdlib.h>


struct Stack {
  int val;
  struct Stack *next;
};

struct Stack *s = NULL;

/*Doing insertion from start and deletion from Start*/

void display() {
  /*
   *   Return value : void
   *   Input        : Pointer to the stack "s"
   */
  struct Stack *ptr = s;

  if (ptr == NULL) {
    printf("Empty\n");
  }

  while (ptr != NULL) {
    printf("%d ", ptr->val);
    ptr = ptr->next;
  }
}
void push(int data) {
  /*
   *   Return value : void
   *   Input        : Pointer to the stack "s",Integer to be inserted "data"
   */

  struct Stack *n = (struct Stack *)malloc(sizeof(struct Stack));
  n->val = data;
  n->next = s;
  s = n;
  /*printf("pushed %d\n", data);
  display(s);*/
}

void pop() {
  /*
   *   Return value : void
   *   Input        : Pointer to the stack "s"
   */
  // save reference to first link

  s = s->next;
}

int main() {
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  while (1) {
    int choice;
    int data;
    scanf("%d", &choice);
    // printf("%d\n",choice);
    switch (choice) {
    case 1: {
      scanf("%d", &data);
      // printf("%d\n",data);
      push(data);
    } break;

    case 2: {
      pop();
    } break;

    case 3: {
      display();
      printf("\n");
    } break;

    case 4: {
      return 0;
    } break;
    }
  }
  return 0;
}
