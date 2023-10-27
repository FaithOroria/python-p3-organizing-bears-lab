# SQL queries for the bear database

# Task 1: Select names and ages of all female bears
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

# Task 2: Select names of all bears in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name;
"""

# Task 3: Select names and ages of all alive bears, ordered from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age;
"""

# Task 4: Select the name and age of the oldest bear
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# Task 5: Select the name and age of the youngest bear
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age
LIMIT 1;
"""
