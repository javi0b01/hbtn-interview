#include"binary_trees.h"
/**
 * heap_insert - function that inserts a value into a Max Binary Heap
 * @root: is a double pointer to the root node of the Heap
 * @value: is the value store in the node to be inserted
 *
 * Return: a pointer to the inserted node, or NULL on failure
 **/
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *node;

	if (!root)
		return (NULL);
	if (!*root)
		return (*root = binary_tree_node(NULL, value));
	return (NULL);
}
