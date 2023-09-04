#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	/* Check if list is empty or has only one node */
	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list->next;      /* Initialize the tortoise pointer */
	hare = list->next->next;    /* Initialize the hare pointer */

	/* Traverse the list with tortoise and hare pointers */
	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)   /* If they meet, there's a cycle */
			return (1);

		tortoise = tortoise->next;      /* Move the tortoise by one step */
		hare = hare->next->next;        /* Move the hare by two steps */
	}

	return (0); /* If we reach the end, there's no cycle */
}
