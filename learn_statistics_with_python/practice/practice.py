import numpy as np
import pandas as pd
from scipy import stats

books_data = pd.read_csv("books.csv") 
books_height = books_data['Height']

book_height_mean   = int(np.mean(books_height))
book_height_median = int(np.median(books_height))
book_height_mode   = stats.mode(books_height)


print("The mean pages in dataset is " + str(book_height_mean))
print("The median pages in dataset is " + str(book_height_median))
print("The mode pages in dataset is " + str(book_height_mode[0][0]) + " and it appears " + str(book_height_mode[1][0]) + " times out of " + str(len(books_height)))

data = np.array([10,13,7,10,5,15])
print(np.mean(data))
print(np.median(data))
print(stats.mode(data))


