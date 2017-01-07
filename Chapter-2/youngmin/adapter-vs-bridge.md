## Adapter pattern
~~~{.python}
class Target:
    @staticmethod
    def meth1(p1, p2):
        print (p1 + ", " + p2)
 
 
class Adapter:
    @staticmethod
    def meth2(p1, p2, p3):
        Target.meth1(p1, p2 + " and " + p3)

if __name__ == '__main__':
    Adapter.meth2('here', 'there', 'everywhere')
~~~

## Bridge pattern
~~~{.python}
class Implementation(object):
    def interface1(self, p1, p2):
        print (p1 + ", " + p2)
 
 
class Bridge(object):
    def __init__(self):
        self.impl = Implementation()
 
    def interface2(self, p1, p2, p3):
        self.impl.interface1(p1, p2 + " and " + p3)

if __name__ == '__main__':
    Bridge().interface2('here', 'there', 'everywhere')
~~~