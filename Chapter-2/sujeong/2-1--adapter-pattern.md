# 어뎁터 패턴

## 어뎁터 패턴의 활용
어뎁터 패턴은 기존에 만들어진 클래스가 있을 때 기존 클래스에 변형을 가하지 않고 새로운 인터페이스로 사용하기 원할 때 사용된다.

이를 테면 쉬운 예로는
~~~{.python}
class Shape(metaclass=abc.ABCMeta):
    @abstractmethod
    def draw(x1, y1, x1, y2):
~~~
위와 같이 좌상단, 우하단의 좌표를 각각 입력 받아 어떤 도형을 출력하는 인터페이스로 도형 출력 클래스를 만들었을 때

~~~{.python}
class LegacyRect:
    def draw(x, y, width, height):
        ...
~~~
위와 같이 기존에 만들어진 시작 좌표와 너비와 높이를 입력 받아 사각 도형을 그려주는 메서드를 가진 클래스가 있고 이를 재활용 하고 싶다고 하면

이를
~~~{.python}
class Rect:
    def __init__(self, legacyRect):
        self.legacyRectDrawer = legacyRect
    def draw(x1, y1, x1, y2):
        self.legacyRect.draw(x1, y1, x2 - x1, y2 - y1) 
        
~~~
이와 같은 형태로 어뎁터 클래스를 만들어 재활용 하는 것을 생각해 볼 수 있겠다.

## 조금더 실용적인 어뎁터 패턴의 활용

만약 과거에 만들어진 도형 객체가 다음과 같이 더 많다고 가정하자
~~~{.python}
class LegacyRect:
    def draw(x, y, width, height):
        ...

class LegacyCircle:
    def draw(x, y, radius):
        ...

class LegacyLine:
    def draw(leftTopX, leftTopY, rightBottomX, rightBottomY):
        ...

class LegacyPicture:
    def draw(x, y, width, height):
        ...
~~~
그리고 이 도형 객체들을 이용해서 무작위 좌표에 다양한 도형으로 폭죽이 터지는 장면을 그려주는 신출력기가 있다고 하자
이 때 어뎁터 패턴을 사용하지 않는다면 아마도 코드는 다음과 같을 것이다

~~~
class SceneDrawer:
    def drawFirework():
        leftTopCoord = rand.sample(xrange(1024), 2)
        rightBottomCoord = [point + xrange(50) for point in leftTopCoord]
        
        x1 = leftTopCoord[0]
        y1 = leftTopCoord[1]
        x1 = rightBottomCoord[0]
        y1 = rightBottomCoord[1]
        
        for shape in shapeList:
            if instanceof LegacyRect:
                shape.draw(x1, y1, x2 - x1, y2 - y1)
            elif instanceof LegacyCircle:
                shape.draw(x2 - (x1/2), y2 - (y1/2), ((x2 - x1)/2))
            elif instanceof LegacyLine:
                shape.draw(x1, y1, x1, y2)
            elif instanceof LegacyPicture:
                shape.draw(x1, y1, x2 - x1, y2 - y1)
            else:
                pass
~~~

아마 조금 더 지원하는 도형의 종류가 많아진다면 도형의 형태를 비교하는 상당히 길어 질 것이며, 실수의 위험도 높아질 것이다.
만약 도형객체가 모두 동일한 파라메터를 받는 형태로 코드가 수정된다면, 비교문을 사용하지 않고 가독성과 편의성을 동시에 만족하는 코드를 짤 수 있다.

~~~{.python}
class Rect:
    def __init__(self, legacyRect):
        self.legacyRect = legacyRect
    def draw(x1, y1, x1, y2):
        self.legacyRect.draw(x1, y1, x2 - x1, y2 - y1)
        
class Circle:
    def __init__(self, legacyCircle):
        self.legacyCircle = legacyCircle
    def draw(x1, y1, x1, y2):
        self.legacyCircle.draw(x2 - (x1/2), y2 - (y1/2), ((x2 - x1)/2))

class Line:
    def __init__(self, legacyLine):
        self.legacyLine = legacyLine
    def draw(x1, y1, x1, y2):
        self.legacyLine.draw(x1, y1, x1, y2)

class Picture:
    def __init__(self, legacyPicture):
        self.legacyPicture = legacyPicture
    def draw(x1, y1, x1, y2):
        self.legacyPicture.draw(x1, y1, x2 - x1, y2 - y1)
~~~

다음과 같이 Legacy 도형들에 대한 어뎁터를 작성해 보자.

그리고 

코드를 수정하고 난 뒤의 신출력기는 다음과 같은 모습일 것이다
~~~
class SceneDrawer:
    def drawFirework():
        leftTopCoord = rand.sample(xrange(1024), 2)
        rightBottomCoord = [point + xrange(50) for point in leftTopCoord]
        
        x1 = leftTopCoord[0]
        y1 = leftTopCoord[1]
        x1 = rightBottomCoord[0]
        y1 = rightBottomCoord[1]
    
        for shape in shapeList:
            shape.draw(x1, y1, x2, y2)
~~~

## 조금 더 많이 실용적인 어뎁터 패턴의 활용
