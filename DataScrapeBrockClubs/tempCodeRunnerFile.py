from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

def scrap():
  url = f'https://www.brockbusu.ca/clubs/browse/'
  driver = Chrome()
  driver.get(url)

  html_content = driver.page_source
  soup = BeautifulSoup(html_content, 'lxml')
  #find all of the links in the website
  club_links = soup.find_all('a', class_ = "msl-gl-link")

  #create a loop for each link  
  for links in club_links:
    #add links together 
    club_url = 'https://www.brockbusu.ca' + links['href']
    #open up website link to clubs and find urls
    driver2 = Chrome()
    driver2.get(club_url)

    html_content2 = driver2.page_source
    soup2 = BeautifulSoup(html_content2, 'lxml')
    nameOfClub = soup2.find('h1', class_='purple').text
    print('Name:', nameOfClub)
    try:
      email = soup2.find('a', class_='socemail')['href'].removeprefix('mailto:')
      print('Email:', email)
    except:
      print('Email: N/A')
scrap()