class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    #
    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)



# company = Company(["tom", "bob", "jane"])


# company1= company[:2]
#
# print(len(company))
#
# for em in company1:
#     print(em)
class Myvector(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other_instance):
        re_vector = Myvector(self.x+other_instance.x,self.y+other_instance.y)
        return re_vector
    def __str__(self):
        return "x:{x},y:{y}".format(x=self.x,y=self.y)
first_vec = Myvector(1,2)
second_vec = Myvector(3,4)
print(first_vec+second_vec)