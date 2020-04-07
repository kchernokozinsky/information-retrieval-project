from models.PhraseSearchUtil import find_phrase_by_biwords, find_phrase_by_words
from models.SingleWordIndex import SingleWordIndex

from models.TwoWordIndex import TwoWordIndex

if __name__ == "__main__":
    # Find phrases by biwords
    twi = TwoWordIndex("D:/information-retrieval-project/res");
    print("He exchanged dark looks lol : ",
          find_phrase_by_biwords("He exchanged dark looks lol", twi.mat_incidence, twi.directory))
    print("He exchanged dark looks : ",
          find_phrase_by_biwords("He exchanged dark looks", twi.mat_incidence, twi.directory))

    # Find phrases by words and distances between them
    swi = SingleWordIndex("D:/information-retrieval-project/res");
    print("номинальным /1 Японии /3 ограничена : ",
          find_phrase_by_words("номинальным /1 Японии /3 ограничена", swi.mat_incidence, swi.inverted_indexes,
                               swi.directory))
    print("номинальным /1 Японии /4 ограничена : ",
          find_phrase_by_words("номинальным /1 Японии /4 ограничена", swi.mat_incidence, swi.inverted_indexes,
                               swi.directory))
