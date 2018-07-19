from starwars_api.client import SWAPIClient
from starwars_api.exceptions import SWAPIClientError
from six import iteritems

api_client = SWAPIClient()


class BaseModel(object):
    

    def __init__(self, json_data):
        """
        Dynamically assign all attributes in `json_data` as instance
        attributes of the Model.
        """
        for key, val in iteritems(json_data):
            setattr(self, key, val)

    @classmethod
    def get(cls, resource_id):
        """
        Returns an object of current Model requesting data to SWAPI using
        the api_client.
        """
        get_string = 'get_{}'.format(cls.RESOURCE_TYPE)
        get_fn = getattr(api_client, get_string)
        json_data = get_fn(resource_id)
        
        return cls(json_data)

    @classmethod
    def all(cls):
        """
        Returns an iterable QuerySet of current Model. The QuerySet will be
        later in charge of performing requests to SWAPI for each of the
        pages while looping.
        """
        qs_string = "{}QuerySet".format(cls.__name__)
        
        return globals()[qs_string]()


class People(BaseModel):
    """Representing a single person"""
    
    RESOURCE_TYPE = 'people'
    
    def __str__(self):
        return "Person: {}".format(self.name)


class Films(BaseModel):
    """Representing a single film"""
    
    RESOURCE_TYPE = 'films'
    
    def __str__(self):
        return "Film: {}".format(self.title)


class BaseQuerySet(object):

    def __init__(self, **params):
        
        get_string = 'get_{}'.format(self.RESOURCE_TYPE)
        get_fn = getattr(api_client, get_string)
        json_data = get_fn(**params)
        
        self.results = json_data['results']
        self.resource_count = json_data['count']
        

    def __iter__(self):
        self.idx = 0
        self.iter_count = 0
        self.results_page = 1
        return self

    def __next__(self):
        """
        Must handle requests to next pages in SWAPI when objects in the current
        page were all consumed.
        """
        
        if not hasattr(self, 'idx'):
            self.idx = 0
        
        if not hasattr(self, 'iter_count'):
            self.iter_count = 0
            
        if not hasattr(self, 'results_page'):
            self.results_page = 1
            
        
        if self.iter_count == self.count():
            raise StopIteration
        
        
        try:
            result = self.results[self.idx]
                
        except IndexError:
            self.results_page += 1
            next_page_qs = globals()[self.__class__.__name__](page=self.results_page)
            self.results = next_page_qs.results
            self.idx = 0
        
        self.iter_count +=1
        return self.MODEL(result)

    next = __next__

    def count(self):
        """
        Returns the total count of objects of current model.
        If the counter is not persisted as a QuerySet instance attr,
        a new request is performed to the API in order to get it.
        """
        return self.resource_count
        


class PeopleQuerySet(BaseQuerySet):
    RESOURCE_TYPE = 'people'
    MODEL = People


class FilmsQuerySet(BaseQuerySet):
    RESOURCE_TYPE = 'films'
    MODEL = Films
