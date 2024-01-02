#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list) {
    listint_t *slow = list, *fast = list;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return 1;  // Cycle detected
        }
    }

    return 0;  // No cycle
}
