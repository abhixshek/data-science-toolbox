def function_name_with_googlestyle_docstring(arg_1, arg_2=97):
    """Description of what the function does.


    Args:
      arg_1 (str): Description of argument that can break onto the next line
        if needed.
      arg_2 (int, optional): Write optional when an argument has a default
        value.

 
    Returns:
      bool: Optional description of the return value. But often the name of the function and the description will make this clear anyway.
      Extra lines are not indented.


    Raises:
      ValueError: Include any error types that the function intentionally
        raises.


    Notes:
      See https://www.google.com
      for more info
    """
#In Google style, the docstring starts with a concise description of what the function does. This should be in imperative language.
#For instance: "Split the data frame and stack the columns" instead of "This function will split the data frame and stack the columns".
#You can also include any additional notes or examples of usage in free form text at the end.

def function_name_with_numpydoc_docstring(arg_1, arg_2=97):
    """

    Description of what the function does.


    Parameters
    ----------
    arg_1: expected data type of arg_1
      Description of arg_1.
    arg_2: int, optional
      Write optional when an argument has a default value.
      Default=97.


    Returns
    -------
    answer : The type of the return value
      Can include a description of the return value.
      Replace "Returns" with "Yields" if this function is a generator.
    """
    answer=50
    return answer

#To get a version, with those leading spaces removed, you can use the getdoc() function from the inspect module.
#import inspect; print(inspect.getdoc(function_name))
#The inspect module contains a lot of useful methods for gathering information about functions.

#NOTE: Notice how the print(function.__doc__) version of the docstring had strange whitespace at the beginning of all but the first line.
#That's because the docstring is indented to line up visually when reading the code.
#But when we want to print the docstring, removing those leading spaces with inspect.getdoc() will look much better.
