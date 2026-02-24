def analyze_movies(movies):
    """
    This function takes a list of movies.
    Each movie is represented as a tuple:
    (title, release_year, list_of_ratings)

    It calculates the average rating for each movie,
    filters out movies with average rating lower than 6.0,
    then prints the remaining movies formatted with:
    title, release year, and average rating.
    """

    filtered_movies = []

    for movie in movies:
        title = movie[0]
        year = movie[1]
        ratings = movie[2]

        average_rating = sum(ratings) / len(ratings)

        if average_rating >= 6.0:
            filtered_movies.append((title, year, average_rating))

    # ترتيب تنازلي حسب التقييم
    filtered_movies.sort(key=lambda x: x[2], reverse=True)

    for index, movie in enumerate(filtered_movies, start=1):
        print(f"{index}. {movie[0]} ({movie[1]}) - Average rating: {movie[2]:.2f} ★")