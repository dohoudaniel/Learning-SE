# ChatGPT - Class VS Object Variables
-------------------------------------

- In object-oriented programming, a class is a blueprint or template for creating objects, while an object is an instance of a class. 
- A class variable is a variable that is shared among all instances of the class, while an object variable is a variable that is specific to an instance of the class. 
Here are some differences between class and object variables:

- Scope: A class variable is visible and accessible to all instances of the class, while an object variable is only visible and 
accessible within the instance of the class that it belongs to.

- Memory allocation: Class variables are allocated memory only once, whereas object variables are allocated memory for each instance of the class.

- Accessing the variable: Class variables are accessed using the class name, while object variables are accessed using the object name.

- Modification: Class variables can be modified by any instance of the class, and the modification will be reflected in all instances of the class. 
Object variables, on the other hand, can only be modified within the instance of the class that it belongs to, and the modification will not affect 
other instances of the class.

- Initialization: Class variables are initialized when the class is defined, while object variables are initialized when an instance of the class is created.

- Visibility: Class variables are often used to represent information that is common to all instances of the class, while object variables are often used to 
represent information that is specific to an individual instance of the class.

- In summary, class variables are shared by all instances of the class, while object variables are specific to each instance of the class. The choice of using 
a class variable or an object variable depends on the specific requirements of the program.
