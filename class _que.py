# class Vector2d:
#     def __init__(self, i, j) -> None:
#         self.i = i
#         self.j = j


#         def printVector:
#             print("f{self.i}i + {self.j}j")

#         class Vector3d: 

#             def __init__(self, i, j, k):
#                 super().__init__(i, j)
#                 self.k = k


#         def printVector(self):
#             print("f{self.i}i + {self.j}j + {self.k}k")

# V2 = Vector2d(1, 5)
# # V3 = Vector3d(11, 5, 9)  

#Question number ---

# st = "The name of the student is {}, his marks are {} and phone number is {}"
# a = st.format("Prayas",97, 7505645990)
# print(a)

#Question number----

# a = [i*2 for i in range(1, 11)]
# st = ""
# for item in a:
#     st += str(item) + '\n'

#     print(st)

#Question number --

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am the best Developer in my own world'
 
app.run()


