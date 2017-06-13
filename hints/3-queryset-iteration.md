# Hint 3

The last challenging part of this project is handling the iteration inside the `BaseQuerySet` class. It's a simple iteration pattern, but we need to make sure to handle requests to next pages every time the data in current page is exhausted.

A pseudocode interpretation of the iteration process might look like:

```
if next elem position is not in retrieved elems:
    get next page of elems
    if error retrieving:
        raise StopIteration
    else:
        convert data to objects and store
get next elem
increase position of next elem
return elem
```

It may make things easier to put the logic for retrieving a page of results and subsuquently converting them to objects into a helper method.
