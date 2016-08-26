# TwitterScraper
A web scraper that takes a twitter hashtag on input and outputs a list of names that tweeted about it to a file

Because twitter dynamically loads its pages, I had to use Selenium to open it up in browser and scroll down automatically. This program will load as many pages as you ask it to and then analyze the page with Beautiful Soup, adding every username it finds. It then saves the names (no duplicates) to a text file.

Here's a demo:

![demo gif](scraper-demo.gif)
