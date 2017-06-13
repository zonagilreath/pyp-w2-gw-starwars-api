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

One way to do this is to use another of Python's methods for working with dynamic attributes: `getattr`

This is how `getattr` works:
```python
# These two lines are functionally the same
print(my_obj.my_attr)
print(getattr(my_obj, 'my_attr'))
```
Just like `setattr`, `getattr` takes the attribute name as a string. You can also give `getattr` a third parameter which becomes the default value if the attribute doesn't exist.

One useful way to use `getattr` is to use it to dynamically call an object's methods, since they are also attributes of the object:
```python
class MyObject(object):
    def my_method(self):
        pass

o = MyObject()

# These two are functionally the same
o.my_method()
getattr(o, 'my_method')()
```
