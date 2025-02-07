movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def highrated(movie):
    return movie['imdb'] > 5.5

movie_example = {
  "name": "Ringing Crime",
  "imdb": 4.0,
  "category": "Crime"
}

print(highrated(movie_example))

def highfilter(movies):
    filtered_movies = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            filtered_movies.append(movie)
    return filtered_movies

movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    }
]

print(highfilter(movies))

def filter(movies, category):
    return [movie for movie in movies if movie['category'].lower() == category.lower()]

movies = [
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    },
    {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
    },
    {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
    }
]

print(filter(movies, "Drama"))
print(filter(movies, "Thriller"))
print(filter(movies, "Adventure"))

def average(movies):
    return sum(movie['imdb'] for movie in movies) / len(movies)

movies = [
    {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
    },
    {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
    },
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    }
]

print(average(movies))

def averagebycat(movies, category):
    total_score = 0
    count = 0

    for movie in movies:
        if movie['category'].lower() == category.lower():
            total_score += movie['imdb']
            count += 1

    if count > 0:
        return total_score / count
    else:
        return 0
    
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

print(averagebycat(movies, "Drama"))