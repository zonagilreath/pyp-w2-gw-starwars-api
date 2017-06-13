# Hint 1

One of the first challenges you will find, is assigning all the information you get from the API client as dynamic attributes to your models. Even though it seems complicated, it's just a matter of iterating through the JSON data, and use the `setattr()` built-in function to assign each value as an attribute of the model object.

`setattr()` works as follows:
```python
# These two lines are functionally the same
my_obj.my_attr = my_value
setattr(my_obj, 'my_attr', my_value)

```
Note that the actual attribute name needs to be a string when using `setattr`.


For better compatibility between Python 2 and 3 versions, you can use `six.iteritems()` function for iterating through dictionary values (check the documentation [here](https://pythonhosted.org/six/#six.iteritems)), like this:

```python
import six

for key, value in six.iteritems(my_dictionary):
    # do stuff
    pass
```
