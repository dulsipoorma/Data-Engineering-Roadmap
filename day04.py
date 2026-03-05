import pandas as pd

movie_data={
    'Title':['  dark  ', 'inception', '  INTERSTELLAR', 'tenet'],
    'Rating':[8.8, 7.5, 9.2, 6.5]
}

df = pd.DataFrame(movie_data) #turning dictionary into DataFrame

#without using loops clean names- .str.strip() removes the spaces and .str.upper() turns to the capital
df['Title']=df['Title'].str.strip().str.upper() 

#filtering data
high_rated=df[df['Rating']>8.0]

print("Cleaned and Filtered movies")
print(high_rated)

high_rated.to_csv('cleaned_movies.csv',index=False)
