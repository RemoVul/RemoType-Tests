class A:
    def f(self,x,y=2):
        x = x / 2
        list_1 = [1.3,2.5, x]
        return list_1
    
    @staticmethod
    def get_name():
        return "RemoType Will Make Your Coding Exprerience Better"
    
class B(A):
    def generate_dict(self,lis):
        new_dict= {str(j): j * 2 for j in lis}
        return new_dict

a_obj = A()
a_obj.f(50.6)
new_dict = B().generate_dict([1,2,3])
access_static = A.get_name()