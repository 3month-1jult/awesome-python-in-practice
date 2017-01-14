#composite pattern
#in graphic program, useful to composite object's grouping and de-grouping

import abc
import sys

#metaclass : http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
#class of class
class AbstractItem(metaclass=abc.ABCMeta):
  @abc.abstractproperty
  def composite(self):
    pass
  def __iter__(self):
    return iter([])

class SimpleItem(AbstractItem):
  def __init__(self, name, price = 0.00):
    self.name = name
    self.price = price
  
  #make getter, setter decorator
  @property
  def composite(self):
    return False
    
  def print(self, indent="", file=sys.stdout):
    print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)
    
class AbstractCompositeItem(AbstractItem):
  def __init__(self, *items):
    self.children = []
    if items:
      self.add(*items)
    
  def add(self, first, *items):
    self.children.append(first)
    if items:
      self.children.extend(items)
      
  def remove(self, item):
    self.children.remove(item)
    
  def __iter__(self):
    return iter(self.children)
    
class CompositeItem(AbstractCompositeItem):
  def __init__(self, name, *items):
    super().__init__(*items)
    self.name = name
    
  @property 
  def composite(self):
    return True
  @property
  def price(self):
    return sum(item.price for item in self)
    
  def print(self, indent="", file =sys.stdout):
    print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)
    for child in self:
      child.print(indent + "       ")
      
      
def main():
  pencil = SimpleItem("Pencli", 0.40)
  ruler = SimpleItem("ruler", 1.60)
  eraser = SimpleItem("eraser", 0.30)
  pencilSet = CompositeItem("Pencil Set", pencil, ruler, eraser)
  
  box = SimpleItem("Box", 1.00)
  boxedPencilSet = CompositeItem("Boxed pencil set", box, pencilSet)
  boxedPencilSet.add(pencil)
  for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
    item.print()
    
#if __name__ == "__main__":
main()
  
    
    
    
    
    
    
    
    
    
    
    
    
