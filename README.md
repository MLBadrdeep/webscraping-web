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

    pip3 install beautifulsoup4

and

    pip3 install selenium

The final step it’s to make sure you install Google Chrome and Chrome Driver on your machine. These will be necessary if we want to use Selenium to scrape dynamically loaded content.

## How to Inspect the Page

Now that you have everything installed, it’s time to start our scraping project in earnest.

You should choose the website you want to scrape based on your needs. Keep in mind that each website structures its content differently, so you’ll need to adjust what you learn here when you start scraping on your own. Each website will require minor changes to the code.

For this article, I decided to scrape information about the first ten movies from the top 250 movies list from IMDb: https://www.imdb.com/chart/top/.

First, we will get the titles, then we will dive in further by extracting information from each movie’s page. Some of the data will require JavaScript rendering.

To start understanding the content’s structure, you should right-click on the first title from the list and then choose “Inspect Element”.

By pressing CTRL+F and searching in the HTML code structure, you will see that there is only one <table> tag on the page. This is useful as it gives us information about how we can access the data.

An HTML selector that will give us all of the titles from the page is table tbody tr td.titleColumn a. That’s because all titles are in an anchor inside a table cell with the class “titleColumn”.

Using this CSS selector and getting the innerText of each anchor will give us the titles that we need. You can simulate that in the browser console from the new window you just opened and by using the JavaScript line:

    document.querySelectorAll("table tbody tr td.titleColumn a")[0].innerText

You will see something like this:

Now that we have this selector, we can start writing our Python code and extracting the information we need.
How to Use BeautifulSoup to Extract Statically Loaded Content

The movie titles from our list are static content. That’s because if you look into the page source (CTRL+U on the page or right-click and then choose View Page Source), you will see that the titles are already there.

Static content is usually easier to scrape as it doesn’t require JavaScript rendering. To extract the first ten titles on the list, we will use BeautifulSoup to get the content and then print it in the output of our scraper.

        import requests
        from bs4 import BeautifulSoup

        page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
        soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

        links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
        first10 = links[:10] # Keep only the first 10 anchors
        for anchor in first10:
            print(anchor.text) # Display the innerText of each anchor

The code above uses the selector we saw in the first step to extract the movie title anchors from the page. It then loops through the first ten and displays the innerText of each.

The output should look like this:
How to Extract Dynamically Loaded Content

As technology advanced, websites started to load their content dynamically. This improves the page’s performance, the user's experience, and even removes an extra barrier for scrapers.

This complicates things, though, as the HTML retrieved from a simple request will not contain the dynamic content. Fortunately, with Selenium, we can simulate a request in the browser and wait for the dynamic content to be displayed.
How to Use Selenium for Requests

You will need to know the location of your chromedriver. The following code is identical to the one presented in the second step, but this time we are using Selenium to make the request. We will still parse the page’s content using BeautifulSoup, as we did before.

        from bs4 import BeautifulSoup
        from selenium import webdriver

        option = webdriver.ChromeOptions()
        # I use the following options as my machine is a window subsystem linux. 
        # I recommend to use the headless option at least, out of the 3
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-sh-usage')
        # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
        driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor

Don’t forget to replace “YOUR-PATH-TO-CHROMEDRIVER” with the location where you extracted the chromedriver. Also, you should notice that instead of page.content, when we are creating the BeautifulSoup object, we are now using driver.page_source, which provides the HTML content of the page.
How to Extract Statically Loaded Content Using Selenium

Using the code from above, we can now access each movie page by calling the click method on each of the anchors.

    first_link = driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
    first_link.click()

This will simulate a click on the first movie’s link. However, in this case, I recommend that you continue using driver.get instead. This is because you will no longer be able to use the click() method after you go on a different page since the new page doesn't have links to the other nine movies.

As a result, after clicking on the first title from the list, you’d need to go back to the first page, then click on the second, and so on. This is a waste of performance and time. Instead, we will just use the extracted links and access them one by one.

For “The Shawshank Redemption”, the movie page will be https://www.imdb.com/title/tt0111161/. We will extract the movie’s year and duration from the page, but this time we will use Selenium’s functions instead of BeautifulSoup as an example. In practice, you can use either one, so pick your favorite.

To retrieve the movie’s year and duration, you should repeat the first step we went through here on the movie’s page.

You will notice that you can find all of the information in the first element with the class ipc-inline-list (".ipc-inline-list" selector) and that all of the elements of the list contain the attribute role with the value presentation (the [role=’presentation’] selector).

        from bs4 import BeautifulSoup
        from selenium import webdriver

        option = webdriver.ChromeOptions()
        # I use the following options as my machine is a window subsystem linux. 
        # I recommend to use the headless option at least, out of the 3
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-sh-usage')
        # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
        driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)

        page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
        soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup

        totalScrapedInfo = [] # In this list we will save all the information we scrape
        links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
        first10 = links[:10] # Keep only the first 10 anchors
        for anchor in first10:
            driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page
            infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
            informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
            scrapedInfo = {
                "title": anchor.text,
                "year": informations[0].text,
                "duration": informations[2].text,
            } # Save all the scraped information in a dictionary
            totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list

        print(totalScrapedInfo) # Display the list with all the information we scraped

## How to Extract Dynamically Loaded Content Using Selenium

The next big step in web scraping is extracting content that is loaded dynamically. You can find such content on each of the movie’s pages (such as https://www.imdb.com/title/tt0111161/) in the Editorial Lists section.

If you look using inspect on the page, you'll see that you can find the section as an element with the attribute data-testid set as firstListCardGroup-editorial. But if you look in the page source, you will not find this attribute value anywhere. That’s because the Editorial Lists section is loaded by IMDB dynamically.

In the following example, we will scrape the editorial list of each movie and add it to our current results of the total scraped information.

To do that, we will import a few more packages that make it possible to wait for our dynamic content to load.

          from bs4 import BeautifulSoup
          from selenium import webdriver
          from selenium.webdriver.common.by import By
          from selenium.webdriver.support.ui import WebDriverWait
          from selenium.webdriver.support import expected_conditions as EC

          option = webdriver.ChromeOptions()
          # I use the following options as my machine is a window subsystem linux. 
          # I recommend to use the headless option at least, out of the 3
          option.add_argument('--headless')
          option.add_argument('--no-sandbox')
          option.add_argument('--disable-dev-sh-usage')
          # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
          driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)

          page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
          soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup

          totalScrapedInfo = [] # In this list we will save all the information we scrape
          links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
          first10 = links[:10] # Keep only the first 10 anchors
          for anchor in first10:
              driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page 
              infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
              informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
              scrapedInfo = {
                  "title": anchor.text,
                  "year": informations[0].text,
                  "duration": informations[2].text,
              } # Save all the scraped information in a dictionary
              WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial']")))  # We are waiting for 5 seconds for our element with the attribute data-testid set as `firstListCardGroup-editorial`
              listElements = driver.find_elements_by_css_selector("[data-testid='firstListCardGroup-editorial'] .listName") # Extracting the editorial lists elements
              listNames = [] # Creating an empty list and then appending only the elements texts
              for el in listElements:
                  listNames.append(el.text)
              scrapedInfo['editorial-list'] = listNames # Adding the editorial list names to our scrapedInfo dictionary
              totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list

          print(totalScrapedInfo) # Display the list with all the information we scraped

For the previous example, you should get the following output:
How to Save the Scraped Content

Now that we have all the data we want, we can save it as a .json or a .csv file for easier readability.

To do that, we will just use the JSON and CVS packages from Python and write our content to new files:

          import csv
          import json

          ...

          file = open('movies.json', mode='w', encoding='utf-8')
          file.write(json.dumps(totalScrapedInfo))

          writer = csv.writer(open("movies.csv", 'w'))
          for movie in totalScrapedInfo:
              writer.writerow(movie.values())

Scraping Tips and Tricks

While our guide so far is already advanced enough to take care of JavaScript rendering scenarios, there are still many things to explore in Selenium.

In this section, I will share some tips and tricks that may come in handy.
1. Time your requests

If you spam a server with hundreds of requests in a short time, it’s very probable that at some point, a captcha code will appear, or your IP might even get blocked. Unfortunately, there is no workaround in Python to avoid that.

Therefore, you should put some timeout breaks between each request so that the traffic will look more natural.

          import time
          import requests

          page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
          time.sleep(30) # Wait 30 seconds
          page = requests.get('https://www.imdb.com/') # Getting page HTML through request

2. Error handling

Since websites are dynamic and they can change structure at any moment, error handling might come in handy if you use the same web scraper frequently.

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "your selector")))
        break
    except TimeoutException:
        # If the loading took too long, print message and try again
        print("Loading took too much time!")

The try and error syntax can be useful when you’re waiting for an element, extracting it, or even when you’re just making the request.
3. Take Screenshots

If you need to obtain a screenshot of the web page you are scraping at any moment, you can use:

driver.save_screenshot(‘screenshot-file-name.png’)

This can help debug when you’re working with dynamically loaded content.
4. Read the documentation

Last but not least, don’t forget to read the documentation from Selenium. This library contains information about how to do most of the actions you can do in a browser.

Using Selenium, you can fill out forms, press buttons, answer popup messages, and do many other cool things.

If you’re facing a new problem, their documentation can be your best friend.
Final Thoughts

This article’s purpose is to give you an advanced introduction to web scraping using Python with Selenium and BeautifulSoup. While there are still many features from both technologies to explore, you now have a solid base on how to start scraping.

Sometimes web scraping can be very difficult, as websites start to put more and more obstacles in the developer’s way. Some of these obstacles can be Captcha codes, IP blocks, or dynamic content. Overcoming them just with Python and Selenium might be difficult or even impossible.

So, I’ll give you an alternative as well. Try using a web scraping API that solves all those challenges for you. It also uses rotating proxies so that you don’t have to worry about adding timeouts between requests. Just remember to always check if the data you want can be lawfully extracted and used.
