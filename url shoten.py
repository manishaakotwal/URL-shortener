import pyshorteners

url=input("Enter URL for shortener:")

def shortenurl(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenurl(url)