# 1. Create a vector containing the numbers from 10 to 20
vector_numbers <- c(10:20)

# Print the vector
print("Vector of numbers from 10 to 20:")
print(vector_numbers)

# 2. Build a 4x4 matrix with numbers from 1 to 16
matrix_numbers <- matrix(1:16, nrow = 4, ncol = 4)

# Print the matrix
print("4x4 Matrix with numbers from 1 to 16:")
print(matrix_numbers)

# 3. Make a list containing a numeric vector, a character vector, and a matrix
numeric_vector <- c(1, 2, 3, 4)
character_vector <- c("campo1", "campo2", "campo3")
list_matrix <- matrix(5:12, nrow = 2, ncol = 4)

my_list <- list(numeric_vector, character_vector, list_matrix)

# Print the list
print("List containing a numeric vector, a character vector, and a matrix:")
print(my_list)

# 4. Construct a data frame with three columns: studentID, name, degree, and year
student_data <- data.frame(
  studentID = c(1, 2, 3, 4),
  name = c("Marcos", "Maria", "Alvaro", "Daniel"),
  degree = c("Computer Science", "Physics", "Mathematics", "Chemistry"),
  year = c(2020, 2023, 2021, 2022)
)

# Print the data frame
print("Data frame with columns: studentID, name, degree, and year:")
print(student_data)
