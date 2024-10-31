# Data Visualization Application using Streamlit and Snowflake

Your task is to develop a data visualization application using Streamlit that connects to Snowflake and displays key insights from the Customer Purchasing Behavior dataset, available on Kaggle: Customer Purchasing Behaviors (https://www.kaggle.com/datasets/hanaksoy/customer-purchasing-behaviors).
Dataset Overview
The dataset contains information about customer purchasing behaviors, including demographics, purchase amounts, and purchasing habits. You will load this data into Snowflake, process it, and build visualizations based on business insights.
Tasks
1. Data Preparation & Snowflake Setup

1. Download the dataset and create a table in Snowflake to store the customer purchasing data.

2. Use Snowflake's file staging and data loading options to upload the dataset.

3. Ensure that the table is properly structured for querying.


2. Data Processing in Snowflake

4. Perform data processing operations to clean the data (e.g., handling null values, filtering, etc.).

5. Extract meaningful subsets of data, such as:
6. Customer segmentation (based on age, location, purchase history).

7. Purchase patterns over time (e.g., monthly or yearly trends).





3. Streamlit App Development

8. Develop a Streamlit application that connects to Snowflake using the snowflake.connector library.

9. The application should allow users to:
10. Filter data by customer segments (e.g., age group, region).

11. Visualize purchase behavior over time using line charts or bar graphs.

12. Display summary statistics (e.g., total purchases, average purchase amount, customer count).





4. Visualizations

13. Include at least 3 visualizations using libraries such as matplotlib or plotly:
14. Purchasing Trends: A time-based line graph showing how purchases change over time.

15. Customer Segments: A bar chart showing purchase totals by customer age group or location.

16. Top Customers: A table or chart displaying the top 10 customers based on purchase amount.





5. Manage GitHub Repository

17. Upload the full codebase (including the Streamlit app and connection to Snowflake) to a public GitHub repository.

18. Repository should include:
19. A README.md file explaining the project and how to run the Streamlit app locally.

20. A CHANGELOG.md file containing changes during the application development process.

21. Released application using GitHub functionality.

22. Any necessary dependencies (list them in a requirements.txt file).

23. .gitignore file.






