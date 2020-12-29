import requests
from bs4 import BeautifulSoup
def get_over(code):
    for i in range (len(code)):
        if code[i]=="/":
            return(code[i+1:i+3])

def get_matches(Type):
    URL = 'https://www.espncricinfo.com/scores'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()
    spans = soup.find_all('div', {'class': 'match-score-block'})
    T20 = {}
    ODI = {}
    for i in spans:
        if (i.find_all("span", string="Live")):
            teams = i.find_all('p', {'class': 'name'})
            team = ' '
            for t in teams:
                tname = t.get_text() + " Vs "
                team += tname
            team = team[0:len(team) - 4]
            choose = i.find_all('span', {'class': 'extra-score'})

            for j in choose:
                if (get_over(str(j)) == '20'):
                    link = str(i.find('a', href=True))
                    T20[team]=link
                    #print(link)
                if (get_over(str(j)) == '50'):
                    link = str(i.find('a', href=True))
                    ODI[team] = link

    if Type=="t20":
        return T20
    if Type=="odi":
        return ODI

