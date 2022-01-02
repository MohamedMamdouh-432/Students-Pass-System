class Person :
    def __init__(self, nm, n_id, c_id, dep, isvac):
        self.name = nm
        self.nat_id = n_id
        self.cge_id = c_id
        self.depart = dep 
        self.isVac = isvac
    def show(self):
        print(f'Name : {self.name}')
        print(f'National Id : {self.nat_id}')
        print(f'College Id : {self.cge_id}')
        print(f'departement : {self.depart}')
        print(f'Vaccinated State : {self.isVac}')

class Student(Person) :
    def __init__(self, nm, n_id, c_id, dep, isvac, gd, gd_yr, catg):
        super().__init__(nm, n_id, c_id, dep, isvac)
        self.grade = gd
        self.grad_year = gd_yr
        self.category = catg
    def show(self):
        super().show()
        print(f'Grade : {self.grade}')
        print(f'Graduation Year : {self.grad_year}')
        print(f'category : {self.category}')

class Lecturer(Person):
    def __init__(self, nm, n_id, c_id, dep, isvac, spc, unv):
        super().__init__(nm, n_id, c_id, dep, isvac)
        self.speclt = spc
        self.org_unv = unv
    def show(self):
        super().show()
        print(f'Speciality : {self.speclt}')
        print(f'Origin University : {self.org_unv}')