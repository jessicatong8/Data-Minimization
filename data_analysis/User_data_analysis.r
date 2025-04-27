df <- read.csv("data_analysis/UserPurposeLimitation_Values_Cleaned.csv")

table(df$UserExp_AF)
table(df$UserExp_PP)
table(df$UserExp_AM)
table(df$UserExp_AL)



columns_to_plot <- c("UserExp_AF", "UserExp_PP", "UserExp_AM", "UserExp_AL")


par(mar = c(5, 10, 4, 2)) # margins bottom, left, top, right



# for (col in columns_to_plot) {
#     barplot(
#         table(df[[col]]),
#         horiz = TRUE, # rotate bars horizontally
#         las = 1, # make axis labels horizontal
#         xlab = "Count", # label the x-axis
#         main = paste("User Expectations of Data Collection for ", col)
#     )
# }

# Define the new labels
labels <- c("Definitely yes", "Probably yes", "Not sure", "Probably no", "Definitely not")

# Convert the numerical data to factor and assign the new labels
df$UserExp_AL <- factor(df$UserExp_AL, levels = 1:5, labels = labels)

barplot(
    table(df$UserExp_AL),
    horiz = TRUE, # rotate bars horizontally
    las = 1, # make axis labels horizontal
    xlab = "Count", # label the x-axis
    main = "User Expectations of Data Collection for Analytics"
)
split_values <- unlist(strsplit(df$Request_AF, ","))
table(split_values)
barplot(table(split_values))



# filtered_df <- df[df$col & df$ == "finance", ]
# filtered_df <- df[df$col & df$ == "food and drink", ]
# filtered_df <- df[df$col & df$ == "game", ]
# filtered_df <- df[df$col & df$ == "photo and video", ]
# filtered_df <- df[df$col & df$ == "shopping", ]
