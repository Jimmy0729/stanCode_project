"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        headers = {'User-Agent':'headersMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        male = 0
        # The total amount of male
        female = 0
        # The total amount of female
        count = 0
        # The variable to count the total time of loop
        ans = ''
        # In order to get a new str since the number in website have comma
        td_tags = soup.find_all('td')
        for td in td_tags:
            '''
            Use debug mode to find when the number of baby appear
            and we can find some law to get the td.text we want.
            '''
            count += 1
            if count == 4 or (count-4) % 5 == 0:
                for i in range(len(td.text)):
                    # get a new str again so that we can plus it to male
                    if td.text[i].isdigit():
                        ans += td.text[i]
                male += int(ans)
                ans = ''

            elif count == 6 or (count-6) % 5 == 0 and count != 1:
                # get a new str again so that we can plus it to female
                for i in range(len(td.text)):
                    if td.text[i].isdigit():
                        ans += td.text[i]
                female += int(ans)
                ans = ''
        print(f'Male number:{male}')
        print(f'Female number:{female}')


if __name__ == '__main__':
    main()
