import pandas as pd

if __name__ == "__main__":
    # Define a dictionary 'x'

    x = {'Name': ['Rose', 'John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4],
         'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
         'Salary': [100000, 80000, 50000, 60000]}

    # casting the dictionary to a DataFrame
    df = pd.DataFrame(x)
    print(df)
    x = df[['ID']]
    print(x)
    print(type(x))
    z = df[['Department', 'Salary', 'ID']]
    print(z)

    s = {'Student': ['David', 'Samuel', 'Teny', 'Even'], 'Age': [27, 24, 22, 32],
         'Country': ['UK', 'Canada', 'China', 'USA'],
         'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
         'Marks': [85, 72, 80, 76]}
    df = pd.DataFrame(s)
    print(df)
    b = df[['Marks']]
    print(b)
    c = df[['Country', 'Course']]
    print(c)
