from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import os

#new top mix track and artist urls
top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

#create the selenium browser
browser = webdriver.Chrome('C:/Users/Lenovo/Desktop/webdriver/chromedriver.exe')
browser.get("https://soundcloud.com")

# main menu
print()
print(">>> Welcome to the Python Soundcloud Scraper")
print(">>> Explore the Top / New & Hot Charts for all Genres")
print(">>> Search Soundcloud for Tracks, Artist, and Mixes")
print()

# new or top menu
while True:
    print(">>> Menu")
    print(">>> 1 - Search for a track")
    print(">>> 2 - Search for an artist")
    print(">>> 3 - Search for a mix")
    print(">>> 4 - Top charts")
    print(">>> 5 - New & hot charts")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Your choice: "))
    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue

    # search for an artist
    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue

    #search for a mix
    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue

    #search for top Charts
    if choice == 4:
        request = requests.get(top_url)
        soup = bs4.BeautifulSoup(request.text, 'lxml')

        while True:
            print(">>> Genres Avalaible: ")
            print()

            genres = soup.select("a[href*=genre]")[2:]
            genre_links=[]

            #printout all of the avaiaible Genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> Your choice (x to re-select chart type): ")
            print()

            if choice == 'x': break
            else: choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            #print tracks
            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index+1) + ": " + track.text)
                print()
            #song selection loop
            while True:
                choice = input(">>> Your choice (x to re-select chart type): ")
                print()

                if choice == 'x':
                    break;
                else:
                    choice = int(choice) - 1

                print("Now Playing: "+ track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])
                button = browser.find_element_by_id('content')
                button.click()

    #search for new and hot Charts
    if choice == 5:
        request = requests.get(new_url)
        soup = bs4.BeautifulSoup(request.text, 'lxml')

        while True:
            print(">>> Genres Avalaible: ")
            print()

            genres = soup.select("a[href*=genre]")[2:]
            genre_links=[]

            #printout all of the avaiaible Genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> Your choice (x to re-select chart type): ")
            print()

            if choice == 'x': break
            else: choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            #print tracks
            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index+1) + ": " + track.text)
                print()
            #song selection loop
            while True:
                choice = input(">>> Your choice (x to re-select chart type): ")
                print()

                if choice == 'x':
                    break;
                else:
                    choice = int(choice) - 1

                print("Now Playing: "+ track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])
                button = browser.find_element_by_id('content')
                button.click()

                
print()
print("Good Bye!")
print()
