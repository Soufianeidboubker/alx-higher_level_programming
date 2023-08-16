#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyOb list.
 */
void print_python_list_info(PyOb *p)
{
	int size, alloc, s;
	PyOb *ob;

	size = Py_SIZE(p);
	alloc = ((PyListOb *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (s = 0; s < size; s++)
	{
		printf("Element %d: ", s);

		ob = PyList_GetItem(p, s);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
