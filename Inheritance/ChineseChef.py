# class ChineseChef:
#     def make_chicken(self):
#         print("the chef makes a chicken")
#
#
#     def make_salad(self):
#         print("the chef makes a salad")
#
#
#     def make_special_dish(self):
#         print("the chef makes orange chicken")
#
#     def make_fried_rice(self):
#         print("chef makes fried rice")

from Chef import Chef

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("chef makes fried rice")
    def make_special_dish(self):
        print("the chef makes orange chicken")

