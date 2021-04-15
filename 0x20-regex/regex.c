#include "regex.h"
/**
* regex_match - checks whether a given pattern matches a given string.
* @str: given string
* @pattern: given pattern
* Return: 1 if the pattern matches the string, or 0 if it doesn’t.
*/

int regex_match(char const *str, char const *pattern)
{
	if (!*pattern)
	{
		return (!*pattern);
	}
	if (*(pattern + 1) == '*')
	{
		if (regex_match(str, pattern + 2))
			return (1);
		while (*str && (*pattern == *(str++) || *pattern == '.'))
		{
			if (regex_match(str, pattern + 2))
				return (1);
		}
	}
	else if (*pattern == *str || (*pattern == '.' && *str))
		return (regex_match(++str, ++pattern));
	return (0);
}
