class Delegator(object):
    def __getattr__(self, called_method):
        def wrapper(*args, **kwargs):
            delegation_config = getattr(self, 'DELEGATED_METHODS', None)
            if not isinstance(delegation_config, dict):
                raise AttributeError("'%s' object has not defined any delegated methods" % (self.__class__.__name__))
            
            for delegate_object_str, delegated_methods in delegation_config.items():
                if called_method in delegated_methods:
                    break
            else:
                raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, called_method))
                
            delegate_object = getattr(self, delegate_object_str, None)
            return getattr(delegate_object, called_method)(*args, **kwargs)
        return wrapper


class Human():
    def speak(self): print("hello")

class Child(Human):
    def speak(self): print("heyy")
    def take_out_the_trash(self): print("Okayyyy I'll do it Mom and Dad!")
    def do_the_dishes(self): print("What??! Another chore?!")

class Spouse(Human):
    def speak(self): print("hi")
    def cook_dinner(self): print("Make your own dinner!")
    def do_the_dishes(self): print("It's your turn, ya lazy bum")

class Parent(Delegator, Human):
    DELEGATED_METHODS = {
        'child': [
            'take_out_the_trash',
            'do_the_dishes'
        ],
        'spouse': [
            'cook_dinner',
            'do_the_dishes'
        ]
    }
    
    def __init__(self):
        self.child = Child()
        self.spouse = Spouse()


parent = Parent()
parent.take_out_the_trash()  # Delegated to Child
parent.cook_dinner()         # Delegated to Spouse
try:
    parent.speak()  # This should raise an AttributeError
    parent.do_the_dishes()  # This should raise an AttributeError
except AttributeError as e:
    print(e)
