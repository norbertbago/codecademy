# https://content.codecademy.com/courses/beautifulsoup/cacao/index.html

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(webpage.content, 'html.parser')

ratings_data = soup.find_all("td", "Rating")

ratings = []
for rating in ratings_data[1:]:
  ratings.append(float(rating.string))

plt.hist(ratings)
plt.show()

company_data = soup.find_all("td", "Company")
company_names = []

for company in company_data[1:]:
  company_names.append(company.get_text())

df = pd.DataFrame.from_dict({"Company": company_names, "Rating": ratings})

average_group_rating = df.groupby("Company").Rating.mean()

ten_best = average_group_rating.nlargest(10)
print(ten_best)


