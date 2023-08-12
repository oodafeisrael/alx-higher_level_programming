#include "lists.h"
/**
* check_cycle - function to check if a linked list contains a cycle
* @list: linked list to be checked
* Return: 0 if the list has no cycle, otherwise 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
