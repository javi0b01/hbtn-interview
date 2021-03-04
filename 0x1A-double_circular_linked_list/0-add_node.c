#include "list.h"

/**
 * add_node_end - Add a new node to the end of a double circular linked list
 * @list: the list to modify
 * @str: the string to copy into the new node
 * Return: Address of the new node, or NULL on failure
 */

List *add_node_end(List **list, char *str)
{
	List *tmp, *newNode;

	newNode = malloc(sizeof(List));
	if (!newNode)
		return (NULL);
	newNode->str = str;
	if (!(*list))
	{
		*list = newNode;
		newNode->next = newNode;
		newNode->prev = newNode;
	}
	else
	{
		tmp = *list;
		newNode->next = tmp;
		newNode->prev = tmp->prev;
		tmp->prev->next = newNode;
		tmp->prev = newNode;
	}
	return (newNode);
}

/**
 * add_node_begin - Add a new node to the beginning of a double circular l-list
 * @list: the list to modify
 * @str: the string to copy into the new node
 * Return: Address of the new node, or NULL on failure
 */

List *add_node_begin(List **list, char *str)
{
	List *tmp, *newNode;

	newNode = malloc(sizeof(List));
	if (!newNode)
		return (NULL);
	newNode->str = str;
	if (!*list)
	{
		*list = newNode;
		newNode->next = newNode;
		newNode->prev = newNode;
	}
	else
	{
		tmp = *list;
		newNode->next = tmp;
		newNode->prev = tmp->prev;
		tmp->prev->next = newNode;
		tmp->prev = newNode;
		*list = newNode;
	}
	return (newNode);
}
