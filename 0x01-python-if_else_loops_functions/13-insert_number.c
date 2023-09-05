#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Description: This function inserts a new node with the specified number into
 * a sorted singly-linked list while maintaining the sorting order.
 *
 * Return: If function fails to allocate memory for new node, returns NULL.
 *         Otherwise, it returns a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	/* Allocate memory for the new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	/* Set the value of the new node to the specified number */
	new->n = number;

	/* Handle where list is empty or new node inserted at the beginning */
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	/* Traverse the list to find the appropriate position for insertion */
	while (node && node->next && node->next->n < number)
		node = node->next;

	/* Insert the new node into the list */
	new->next = node->next;
	node->next = new;

	return (new);
}
