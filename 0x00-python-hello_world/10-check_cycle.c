#include "lists.h"
/**
* check_cycle - function to check if a linked list contains a cycle
* @list: linked list to be checked
* Return: 0 if the list has no cycle, otherwise 1
*/
int check_cycle(listint_t *list)
{
	listint_t *pre = list;
	listint_t *new = list;

	if (!list)
		return (0);
	while (pre != NULL && new != NULL && new->next != NULL)
	{
		pre = pre->next;
		new = new->next->next;

		if (pre == new)
		{
			return (1);
		}

	}
	return (0);
}
