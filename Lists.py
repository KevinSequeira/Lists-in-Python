# Hello people! Good to have you back for another session on Python with the Programming Panda.
# In the last session, we had a quick look at the last Immutable Data Type: Tuples.
# From here on, we're going to explore Mutable Data Types. As explained before, Mutable Types
# in Python allow you to change the data they hold any time after they have been created.

# So, getting started, in this session, we're going to dive into Lists. Lists are pretty similar
# to Tuples, only that they can be altered any time after being assigned values, unlike Tuples.
# Also, they are considered as 'general sequences', and are ordered positionally. This means that
# you can pick up data objects from a list by calling on its position.

# As you go ahead, you'll notice that Lists closely represent Arrays in Java, C, or C++. And yet
# they differ by this: Lists can contain hetergenous data, i.e. data of different types.

# Consider this simple list that holds data about a Student:
List_Student001 = [1, 'Kevin', 'Sequeira', 'Electronics', 5.4];

# First, let's confirm that this is indeed a 'List':
List_Student001_DataType = type(List_Student001);
print('Data Type of Student001: ' + str(List_Student001_DataType));      # The output for this line is: Data Type of Student001: <class 'list'>

# Now consider this declaration:
Tuple_Student001 = (1, 'Kevin', 'Sequeira', 'Electronics', 5.4);
Tuple_Student001_DataType = type(Tuple_Student001);
print('Data Type of Student002: ' + str(Tuple_Student001_DataType));      # The output for this line is: Data Type of Student001: <class 'tuple'>
                                                                    # This is because of the difference in declaration. Be very careful when
# creating Lists - they are always created with [ ] brackets, while Tuples are created with ( ).

# del Student002, Student002_DataType;        # Here, I am deleting the Tuple variables, as we won't be using them in the future.

# Now, let's have a look at how Lists can be altered. You can add elements to a list:
print('\n' + 'Original Student001: ' + str(List_Student001));
print('Student001 ID: ' + str(id(List_Student001)));     # The output for this line is: Student001 ID: 17343192
List_Student001 += ['Mumbai'];       # Here, I have used 'Operator Overloading' for adding 'Mumbai' to the list 'Student001'. We'll explore this later.
print('\n' + 'New Student001: ' + str(List_Student001));
print('Student001 ID: ' + str(id(List_Student001)));     # The output for this line is: Student001 ID: 17343192

# In the above example you see, when we add the String 'Mumbai' to the List Student001, the resulting data is
# not stored as a new List. The data is stored back into the original List. This proves that the List is Mutable.
# Now what would happen if we were to do the same for the Tuple Student002?
print('\n' + 'Original Student002: ' + str(Tuple_Student001));
print('Student002 ID: ' + str(id(Tuple_Student001)));     # The output for this line is: Student002 ID: 9838880
Tuple_Student001 += 'Mumbai', ;
print('\n' + 'New Student002: ' + str(Tuple_Student001));
print('Student002 ID: ' + str(id(Tuple_Student001)));     # The output for this line is: Student002 ID: 21871280

# From the above example, it is proven that Tuples are Immutable Objects.
# Let's look at some more operations that can be carried out on Lists...

# Unlike simply adding data to Lists, you cannot delete or multiple data the same way. For these, you need
# to use Type Specific Operations / Functions.
# You can append data at the end of a List:
List_Student001.append('India');
print('\n' + 'Student001: ' + str(List_Student001));     # The output for this line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Electronics', 5.4, 'Mumbai', 'India']

# You can also delete specific data from the List:
List_Student001.remove(5.4);
print('\n' + 'Student001: ' + str(List_Student001));     # The output for this line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Electronics', 'Mumbai', 'India']

# You can use the .pop(index) function which removes and returns data from a specific position:
List_Student001.pop(3);
print('\n' + 'Student001: ' + str(List_Student001));     # The output for this line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Mumbai', 'India']

# Also you can 'pop' data from the last position by using the .pop() function:
List_Student001.pop();
print('\n' + 'Student001: ' + str(List_Student001));     # The output for this line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Mumbai']

# You can 'insert' values at specific positions by using the .insert(index, value) function:
List_Student001.insert(3, 'Electronics');
print('\n' + 'Student001: ' + str(List_Student001));     # The output for this line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Electronics', 'Mumbai']

List_Student001.insert(4, 5.4);
List_Student001.insert(6, 'India');
print('\n' + 'Student001: ' + str(List_Student001));

# Using the above type-specific functions, we are now back to the original List we had created.
# Once again, let's check the List Object ID:
print('\n' + 'Student001 ID: ' + str(id(List_Student001)));     # The output for this line is: Student001 ID: 17343192. This confirms that this is the same
                                                         # List we've been working on right from the start.
# Let's look at a couple of more Type Specific Functions:
print('\n' + 'Index of String "Sequeira": ' + str(List_Student001.index('Sequeira')));      # The .index(object) gives us the position of a specific object
                                                                                            # within the List.

# You can count the number of times and object appears within a List:
print('\n' + 'Total number of Objects in List Student001: ' + str(List_Student001.count('Kevin')));

# You can also extend the List by a sequence:
List_Student001.extend(['Xavier Institute of Engineering', 'University of Mumbai']);
print('\n' + 'Student001: ' + str(List_Student001));
# The output for the above line of code is: Student001: [1, 'Kevin', 'Sequeira', 'Electronics', 5.4, 'Mumbai', 'India', 'Xavier Institute of Engineering', 'University of Mumbai']

# Before we end, I'd like to also highlight a couple of other ways we can create Lists.
# Lists can be created from a Tuple:
List_Student002 = list((2, 'Annet', 'DSouza', 'Commerce', 5.8, 'Mumbai', 'India', 'HR College of Commerce', 'University of Mumbai'));
print('\n' + 'Student002: ' + str(List_Student002));
# The above code creates the list as follows: Student002: [2, 'Annet', 'DSouza', 'Commerce', 5.8, 'Mumbai', 'India', 'HR College of Commerce', 'University of Mumbai']

# Similarly, you can create a List from a String:
List_Student003 = list('3 Diana Sequeira Commerce 5.7 Mumbai India St. Andrews College University of Mumbai');
print('\n' + 'Student003: ' + str(List_Student003));
# You're going to love the output for this one:
# Student003: ['3', ' ', 'D', 'i', 'a', 'n', 'a', ' ', 'S', 'e', 'q', 'u', 'e', 'i', 'r', 'a', ' ', 'C', 'o', 'm', 'm', 'e', 'r', 'c', 'e', ' ', '5', '.', '7', ' ', 'M', 'u', 'm', 'b', 'a', 'i', ' ', 'I', 'n', 'd', 'i', 'a', ' ', 'S', 't', '.', ' ', 'A', 'n', 'd', 'r', 'e', 'w', 's', ' ', 'C', 'o', 'l', 'l', 'e', 'g', 'e', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y', ' ', 'o', 'f', ' ', 'M', 'u', 'm', 'b', 'a', 'i']
# Yes, please avoid coverting Strings to Lists!

# Also, you can access data within a List by using the index positions as in Strings and Tuples!
Student001_FirstName = List_Student001[1];
Student001_LastName = List_Student001[2];
Student001_FullName = Student001_FirstName + ' ' + Student001_LastName;
print('\n' + 'Student 001 Full Name: ' + Student001_FullName);
# The output for the above code is: Student 001 Full Name: Kevin Sequeira

# You can also multiply a list by a number:
List_Student001_Multiplied = List_Student001 * 2;
print('\n' + 'Student 001 x 2: ' + str(List_Student001_Multiplied));
# On multiplying by 2, we get a List that is twice as long:
# Student 001 x 2: [1, 'Kevin', 'Sequeira', 'Electronics', 5.4, 'Mumbai', 'India', 'Xavier Institute of Engineering', 'University of Mumbai', 1, 'Kevin', 'Sequeira', 'Electronics', 5.4, 'Mumbai', 'India', 'Xavier Institute of Engineering', 'University of Mumbai']

# Well, that's all we're going to look at, for now. There's a lot more that can be done with Lists. But don't worry.
# For now, this much is enough to get you started. We'll visit more examples and operations as we go ahead.

# Before we finish, let's have a look at 'Operation Overloading' as I'd mentioned earlier.
# You probably know how the basic operators work. You know Addition (+), Subtraction (-),
# Multiplication (*), Division (/), Power Operation (**), and Modulus (%).

# Now, many a time, while using Mutable Data Types (not just in Python), we would use these operators in the typical
# manner for manipulating data within an Object, and then storing the result within the same object:

print('\n' + 'Original Student001: ' + str(List_Student001));
print('Student001 ID: ' + str(id(List_Student001)));     # The output for this line is: Student001 ID: 17343192
List_Student001 = List_Student001 + [2014];              # Here, I have added 2014 to the List Student001, and tried to save the result back into the same
                                                         # List
print('\n' + 'New Student001: ' + str(List_Student001));
print('Student001 ID: ' + str(id(List_Student001)));     # The output for this line is: Student001 ID: 30202256

print('\n' + 'Original Student002: ' + str(List_Student002));
print('Student002 ID: ' + str(id(List_Student002)));     # The output for this line is: Student001 ID: 30560384
List_Student002 += [2014];                               # In this case, I have overloaded the operator. And you will see the resulting data is successfully
                                                         # stored back into the original List.
print('\n' + 'New Student002: ' + str(List_Student002));
print('Student002 ID: ' + str(id(List_Student002)));     # The output for this line is: Student001 ID: 30560384

# The above examples clearly show that using Operator Overloading when it comes to Mutable Data Types is the better
# approach.

# We won't dive deeper, but here's how you overload the other operators:
# a = a + b; becomes a += b;
# a = a - b; becomes a -= b;
# a = a * b; becomes a *= b;
# a = a / b; becomes a /= b;
# Similarly for other operators.

# I'll see you on our next session, where we'll dive into the next Mutable Type, and probably the most awesome one yet:
# Python Dictionaries! 
