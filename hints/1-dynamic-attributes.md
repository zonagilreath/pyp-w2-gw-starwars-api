# Hint 1

One of the first challenges you will find, is assigning all the information you get from the API client as dynamic attributes to your models. Even though it seems complicated, it's just a matter of iterating through the JSON data, and use the `setattr()` built-in function to assign each value as an attribute of the model object.
This should be done at initialization time, in the `BaseModel.__init__()` method.

```python
def __init__(self, json_data):
    """
    Dynamically assign all attributes in `json_data` as instance
    attributes of the Model.
    """
    for key, value in json_data.items():
        setattr(self, key, value)
```

For better compatibility between Python 2 and 3 versions, you can use `six.iteritems()` function (check the documentation [here](https://pythonhosted.org/six/#six.iteritems)), like this:

```python
import six

def __init__(self, json_data):
    """
    Dynamically assign all attributes in `json_data` as instance
    attributes of the Model.
    """
    for key, value in six.iteritems(json_data):
        setattr(self, key, value)
```
