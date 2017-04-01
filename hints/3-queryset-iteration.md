# Hint 3

The last challenging part of this project is handling the iteration inside the `BaseQuerySet` class. It's a simple iteration pattern, but we need to make sure to handle requests to next pages every time the data in current page is exhausted.

As we will handle the iteration manually, we will need to set a few attributes in the `__init__` method to keep track of the current state of the iteration.

```python
def __init__(self):
    self.current_page = 0
    self.current_element = 0

    # this attribute will contain the concatenation of all elements we get
    # in the successive requests to next pages. Meaning that, if we have
    # 10 results per page, after requesting the second page we will
    # see 20 elements in `self.objects`
    self.objects = []
```

Once we set up the initial attributes, we will continue with a simple `__iter__` method, that returns a new instance of the QuerySet for every iteration structure:

```python
def __iter__(self):
    return self.__class__()
```

For each loop in the iteration, we will need to:
- Check if `self.objects` is not exhausted.
- In case it is, request the next page of results using the `APIClient` class.
- If next page is empty or does not exist, raise `StopIteration` exception.
- Else, return the element in the proper index for current loop.

As we don't certainly know how many elements we will have in all pages, we can loop using a `while` structure, and simply brake it with the `StopIteration` exception once we are done.

```python
def __next__(self):
    """
    Must handle requests to next pages in SWAPI when objects in the current
    page were all consumed.
    """
    while True:
        if self.current_element + 1 > len(self.objects):
            # need to request a new page
            try:
                self._request_next_page()
            except SWAPIClientError:
                raise StopIteration()
        elem = self.objects[self.current_element]
        self.current_element += 1
        return elem

def _request_next_page(self):
    """
    Requests next page of elements to the API based on the current state
    of the iteration.
    """
    # increate the page counter to request the following page
    self.current_page += 1

    # request next page in a generic way. Similar to what we did in BaseModel
    method_name = 'get_{}'.format(self.RESOURCE_NAME
    method = getattr(api_client, method_name)
    json_data = method(**{'page': self.current_page})

    # remember that each element in `self.objects` needs to be an instance
    # of the proper Model class. For that we will instantiate the Model class
    # (either People or Films) for each result in the new page.
    Model = eval(self.RESOURCE_NAME.title())
    for resource_data in json_data['results']:
        self.objects.append(Model(resource_data))
```


** NOTE: Using the `eval()` function could generate security issues. Use it under your own risk or try to find a way around to get the Model class name based on the `RESOURCE_NAME` variable.
