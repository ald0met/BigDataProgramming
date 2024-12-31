from person import Person
class Student(Person):
    def __init__(self,num,name,gender,age,kor,eng,math):
        super().__init__(num,name,gender,age)
        self._kor=kor
        self._eng=eng
        self._math=math
        self._total=self._calculate_total()
        self._avg=self._calculate_avg()
        self._order=None

    @property
    def num(self):
        return self._num

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def age(self):
        return self._age

    @property
    def kor(self):
        return self._kor

    @property
    def eng(self):
        return self._eng

    @property
    def math(self):
        return self._math

    @property
    def total(self):
        return self._total

    @property
    def avg(self):
        return self._avg

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self,value):
        self._order=value

    def _calculate_total(self):
        return self._kor+self._eng+self._math

    def _calculate_avg(self):
        return round(self._total/3,2)
