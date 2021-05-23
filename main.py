import os
import sys
import praw
import json
from bs4 import BeautifulSoup
from ebooklib import epub

class epub_handler:

    def __init__(self, path, name, data):
        self.book = epub.EpubBook()
        self.add_defaults(self.book, data)

    def add_defaults(self, book,data):
        # set metadata
        book.set_identifier('id123456')
        book.set_title(data[0])
        book.set_language(data[1])
        book.add_author(data[3])


class reddit_scrape:
    #Defining varibles
    user_agent="Reddit-2-EPUBs"

    def __init__(self, url):
        self.pull_reddit_login()

    def pull_reddit_login(self):

        if not os.path.exists("./logininfo.json"):
            data={}
            data["login"] = []
            data["login"].append({
                "user-agent": self.user_agent,
                "client-id": "ID GOES HERE",
                "secret": "CLIENT SECRET GOES HERE"
            })
            with open('./logininfo.json', 'w') as outfile:
                json.dump(data, outfile)

        else:
            with open('./logininfo.json') as json_file:
                data = json.load(json_file)
            print(data)


#Calling reddit scrape to gather data.
reddit = reddit_scrape("Blanke")
