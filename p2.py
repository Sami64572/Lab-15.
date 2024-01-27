class Parent1:
    def common_method(self):
        print("Method from Parent1")

class Parent2:
    def common_method(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def specific_method(self):
        print("Specific method in Child")


child_instance = Child()


child_instance.common_method() 


class ChildReverse(Parent2, Parent1):
    def specific_method(self):
        print("Specific method in ChildReverse")

child_reverse_instance = ChildReverse()
child_reverse_instance.common_method()


class ChildOverride(Parent1, Parent2):
    def common_method(self):
        print("Overridden method in ChildOverride")

child_override_instance = ChildOverride()
child_override_instance.common_method()  


class ChildSuper(Parent1, Parent2):
    def common_method(self):
        super().common_method()
        print("Additional method in ChildSuper")

child_super_instance = ChildSuper()
child_super_instance.common_method()