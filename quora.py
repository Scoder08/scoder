import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
 
 
url = input("Ask Question : ")

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = url+" quora"
  
for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
    url=j 


print("\nLoading Data..\n")
result = requests.get(url)
 
#to check whether successfully connected to the page or not..
success = result.status_code
if success==200:
	print("Connection to the webpage was successful..!\n")
 
#get the source code of the page..
src = result.content
 
#creating object
soup = BeautifulSoup(src, 'lxml')
 
#getting the question..
question = soup.find("a", attrs={'class': 'question_link'})
print("Question:"+question.text)
 

 
#getting the answer..
print("\n")
answer = soup.find("div", attrs={'class':'u-serif-font-main--regular'})
print("Answer:"+answer.text)