#write your code here
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import csv
import re
string = open('book6.txt', encoding="utf8").read()
new_str = re.sub(r'[^a-zA-Z0-9\n]', ' ', string)
#print(new_str)

tokens = word_tokenize(new_str)
#print(tokens)

# Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()

#lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in tokens])
lemmatized_output = [lemmatizer.lemmatize(w) for w in tokens]

#print(lemmatizer.lemmatize("feet"))

#print(lemmatized_output)

#outputs = re.sub(r'[^a-zA-Z0-9\n]', ' ', lemmatized_output)
#print(outputs)

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

output = list(divide_chunks(lemmatized_output, 1))

# writing to csv file  
with open('data.csv', 'w', newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)   
        
    # writing the data  
    csvwriter.writerows(output) 

