# Hint 2

As we mentioned during the presentation of this project, we must write a generic implementation that contains most of the logic in the `BaseModel` abstract class and only relies in a few class attributes to determine which is the actual Model that the use is instantiating. In this particular case, the important class attribute is `RESOURCE_NAME`.

All content in the `BaseModel` class must be generic, meaning that **we must avoid** things like these:

```python
def get(cls, resource_id):
    # ...
    if cls.RESOURCE_NAME == 'people':
        # do something
    elif cls.RESOURCE_NAME == 'films':
        # do something else
    elif ...
```

Imagine that we want to add a third Model in the future. If we hardcode all the different `RESOURCE_NAME` values in the method, we must come back to this point and add the new model we created. Not very scalable.

Instead, we must find the way to implement it in a way that allows future Models additions without further changes in the `BaseModel` class.

This could be a valid approach:

```python
@classmethod
def get(cls, resource_id):
    """
    Returns an object of current Model requesting data to SWAPI using
    the api_client.
    """

    # let's generate the method name dynamically based
    # on the RESOURCE_NAME class variable
    method_name = 'get_{}'.format(cls.RESOURCE_NAME)  # this will be either `get_people` or `get_films`

    # now that we have the name, let's pick the actual method function
    # from the `api_client` object using the built-in `getattr()`
    method = getattr(api_client, method_name)

    # and finally let's execute the method sending the proper parameters
    # and return the result
    json_data = method(resource_id)

    # remember that the result of the `get()` method must be an instance
    # of the model. That's why we need to instantiate `cls`, which
    # represents the current Model class (either People or Films)
    return cls(json_data)
```
