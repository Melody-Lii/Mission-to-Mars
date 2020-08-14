# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headles driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # set news variables
    news_title, news_paragraph = mars_news(browser)
    
    # set hemi variables
    cerberus_img, cerberus_title, schiaparelli_img, schiaparelli_title, syrtis_img, syrtis_title, valles_img, valles_title = mars_hemis(browser) 

    # run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "cerberus_img": cerberus_img,
        "cerberus_title": cerberus_title,
        "schiaparelli_img": schiaparelli_img,
        "schiaparelli_title": schiaparelli_title,
        "syrtis_img": syrtis_img,
        "syrtis_title": syrtis_title,
        "valles_img": valles_img,
        "valles_title": valles_title
    }
    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # convert browser html to a soup object
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # slide_elem.find("div", class_='content_title')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# ### Featured Images

def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url

# ### Mars Facts

def mars_facts():

    try:
        # Read web scrape to Dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    df.columns=['description', 'value']
    df.set_index('description', inplace=True)

    # Return df to html, add bootstrap
    return df.to_html(classes="table table-dark")

# ### Hemispheres
marsHemis = []

def mars_hemis(browser):

    # list for saved scrapes
    #marsHemis = []

    try:

        ## Cerberus
        
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # locate link to more details, click
        cerberus_elem = browser.find_by_tag('h3')[0]
        cerberus_elem.click()

        # parse html w/ soup
        html = browser.html
        cerberus_soup = BeautifulSoup(html, 'html.parser')

        # get img url
        cerberus_img = cerberus_soup.select_one('div.downloads ul li a').get("href")
        # get hemi title
        cerberus_title = cerberus_soup.select_one('div.content h2').get_text()

        # append img_url & title in marsHemi list
        marsHemis.append({'img_url': cerberus_img, 'title': cerberus_title})



        ## Schiaparelli

        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # locate link to more details, click
        schiaparelli_elem = browser.find_by_tag('h3')[1]
        schiaparelli_elem.click()

        # parse html w/ soup
        html = browser.html
        schiaparelli_soup = BeautifulSoup(html, 'html.parser')

        # get img url
        schiaparelli_img = schiaparelli_soup.select_one('div.downloads ul li a').get("href")
        # get hemi title
        schiaparelli_title = schiaparelli_soup.select_one('div.content h2').get_text()

        # append img_url & title in marsHemi list
        marsHemis.append({'img_url': schiaparelli_img, 'title': schiaparelli_title})



        ## Syrtis

        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # locate link to more details, click
        syrtis_elem = browser.find_by_tag('h3')[2]
        syrtis_elem.click()

        # parse html w/ soup
        html = browser.html
        syrtis_soup = BeautifulSoup(html, 'html.parser')

        # get img url
        syrtis_img = syrtis_soup.select_one('div.downloads ul li a').get("href")
        # get hemi title
        syrtis_title = syrtis_soup.select_one('div.content h2').get_text()

        # append img_url & title in marsHemi list
        marsHemis.append({'img_url': syrtis_img, 'title': syrtis_title})



        ## Valles

        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # locate link to more details, click
        valles_elem = browser.find_by_tag('h3')[3]
        valles_elem.click()

        # parse html w/ soup
        html = browser.html
        valles_soup = BeautifulSoup(html, 'html.parser')

        # get img url
        valles_img = valles_soup.select_one('div.downloads ul li a').get("href")
        # get hemi title
        valles_title = valles_soup.select_one('div.content h2').get_text()

        # append img_url & title in marsHemi list
        marsHemis.append({'img_url': valles_img, 'title': valles_title})

    except BaseException:
        return None
    
    return cerberus_img, cerberus_title, schiaparelli_img, schiaparelli_title, syrtis_img, syrtis_title, valles_img, valles_title

if __name__ == "__main__":

    print(scrape_all())