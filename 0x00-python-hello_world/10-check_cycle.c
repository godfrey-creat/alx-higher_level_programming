#include "lists.h"
/**
 * check_cycle - checks if there is a loop in the linked list
 * @list: head node
 * Return: 1 if there is loop, 0 if there is no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (!list || !list->next)
		return (0);
	slow = list;
	fast = list->next;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
