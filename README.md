# webscraping-web
scraping data and analysis
# What do we call web scraping?

Web scraping is an automated process of gathering public data. Web scrapers automatically extract large amounts of public data from target websites in seconds. 

# What Will You Need for Your Scraper?

To start building your own web scraper, you will first need to have Python installed on your machine. Ubuntu 20.04 and other versions of Linux come with Python 3 pre-installed.

To check if you already have Python installed on your device, run the following command:

    python3 -v

If you have Python installed, you should receive an output like this:

    Python 3.8.2

Also, for our web scraper, we will use the Python packages BeautifulSoup (for selecting specific data) and Selenium (for rendering dynamically loaded content). To install them, just run these commands:

    pip3 install beautifulsoup4 && pip3 install selenium

The final step it’s to make sure you install Google Chrome and Chrome Driver on your machine. These will be necessary if we want to use Selenium to scrape dynamically loaded content.

![image](https://user-images.githubusercontent.com/6348271/138045048-0b872ae3-0124-4456-ae6e-b3a01d3f9506.png)

One of the Python advantages is a large selection of libraries for web scraping. These web scraping libraries are part of thousands of Python projects in existence  on PyPI alone, there are over 300,000 projects today. Notably, there are several types of Python web scraping libraries from which you can choose:

    Requests
    Beautiful Soup
    lxml
    Selenium
    
# Web scraping Python libraries compared

![Untitled 1](https://user-images.githubusercontent.com/6348271/138046857-eda93fe4-da7d-43c2-a02b-13788cc051cc.jpg)


For this Python web scraping tutorial, we’ll be using three important libraries – BeautifulSoup v4, Pandas, and Selenium. Further steps in this guide assume a successful installation of these libraries. If you receive a “NameError: name * is not defined” it is likely that one of these installations has failed.
