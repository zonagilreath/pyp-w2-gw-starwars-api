# [pyp-w2] Star Wars API

![Star Wars](https://images.wondershare.es/images/ringtones/star-wars-episode-7-release-date2.jpg)

Today we will implement a client for the Star Wars API: `https://swapi.co/` (a.k.a. `swapi`).
See extra documentation about the API here: `https://swapi.co/documentation`

`swapi` is using a RESTful structure. It has well defined "groups" of data, also known as `resources` (ie: `people`, `planets`, `starships`, etc).
Each resource has its own URL path. There are URLs used for LISTing many objects of given resource (ie: `/api/people/`), and other for getting the details of one particular object of the resource (ie: `/api/people/1/`).

We will concentrate in two particular resources: `People` and `Films`.
For each of them, we will need to create a model class able to query and present the data. You must respect the following interface:

```python
>>> luke = People.get(1)
>>> str(luke)
"Person: Luke Skywalker"
>>> luke.name
"Luke Skywalker"
>>> luke.birth_year
"19 BBY"
```

Resources must also implement a way of iterating through all objects. To do that, we will use the `all()` classmethod, which will return a `QuerySet` iterable object:

```python
>>> qs = People.all()
>>> next(qs)
"Person: Luke Skywalker"
>>> next(qs)
"Person: C-3PO"
```

Iterative structures like `for`, `while` and list comprehensions must also be supported by `QuerySet`s:
```python
>>> len([person for person in People.all()])
87
>>> for person in People.all():
        print(person.name)
"Luke Skywalker"
"C-3PO"
...
```

`QuerySet`s must implement an easy way of returning the amount of objects it contains:

```python
>>> qs.count()
87
```

Feel free to expand the client behavior with extra functionality.
