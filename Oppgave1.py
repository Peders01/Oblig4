
class filmer:
    def __init__(self, filmtittel, utgivelsesår, score):
        self.filmtittel = filmtittel
        self.utgivelsesår = utgivelsesår
        self.score = score

    def nice_print(self):
        return f"{self.filmtittel} was released in {self.utgivelsesår} and currently has a score of {self.score}"

film_1 =filmer("Inception", 2010, 8.8)
film_2 =filmer("The Martian", 2015, 8.0)
film_3 =filmer("Joker", 2019, 8.4)

print(f"{film_1.filmtittel} was released in {film_1.utgivelsesår} and currently has a score of {film_1.score}")
print(f"{film_2.filmtittel} was released in {film_2.utgivelsesår} and currently has a score of {film_2.score}")
print(f"{film_3.filmtittel} was released in {film_3.utgivelsesår} and currently has a score of {film_3.score}")
print()
print(film_1.nice_print())
print(film_2.nice_print())
print(film_3.nice_print())
