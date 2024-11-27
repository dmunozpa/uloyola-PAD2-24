install.packages("readxl")
library(readxl)
library(stingr)

menu <- file.choose()
exce <- read_excel(menu)
