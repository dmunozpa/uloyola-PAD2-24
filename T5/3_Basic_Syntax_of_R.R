# 1. Create variables of different data types
num_var <- 5.3
char_var <- "Hello , R!"
logical_var <- TRUE
integer_var <- as.integer(3)
integer_var <- 3L

# Print the variables
print(paste("Numeric:", num_var))
print(paste("Character:", char_var))
print(paste("Logical:", logical_var))
print(paste("Integer:", integer_var))

# 2. Write a for-loop to print numbers from 1 to 10
print("Numbers from 1 to 10:")
for (i in 1:10) {
  print(i)
}

# 3. Define and call a function that takes two numbers as arguments and returns their product
multiply_numbers <- function(num1, num2) {
  return(num1 * num2)
}

# Call the function
result <- multiply_numbers(5, 7)
print(paste("Result of multiplying 5 and 7:", result))
