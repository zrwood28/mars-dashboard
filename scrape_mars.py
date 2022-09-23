from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape():
    # Mars News
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless = False)

    url = "https://redplanetscience.com/"

    browser.visit(url)

    html = browser.html

    soup = bs(html, "html.parser")

    news_title = soup.find("div", class_ = "content_title").get_text()

    news_p = soup.find("div", class_ = "article_teaser_body").get_text()

    # Mars Image
    url = "https://spaceimages-mars.com/"

    browser.visit(url)

    html = browser.html

    soup = bs(html, "html.parser")

    img_class = soup.find("a", class_ = "showimg fancybox-thumbs")
    href = img_class["href"]

    featured_image_url = ("https://spaceimages-mars.com/" + href)

    # Mars Table
    url = "https://galaxyfacts-mars.com/"

    browser.visit(url)

    comp_table = pd.read_html(url)

    comp_df = comp_table[0]

    comp_df.columns = comp_df.iloc[0]

    renamed_df = comp_df.rename(columns = {"Mars - Earth Comparison": "Description"})

    clean_df = renamed_df.set_index("Description")

    mars_html_table = clean_df.to_html(buf = None)

    # Mars Hemispheres
    url = "https://marshemispheres.com/"

    browser.visit(url)

    html = browser.html

    soup = bs(html, "html.parser")

    hemisphere_links = []

    hemispheres = soup.find_all("div", class_ = "item")

    for x in hemispheres:
        hem_class = x.find("a", class_ = "itemLink product-item")
        hem_url = hem_class["href"]
        hemisphere_links.append(hem_url)

    link_list = []

    for y in hemisphere_links:
        link = (f"https://marshemispheres.com/{y}")
        browser.visit(link)
        html = browser.html
        soup = bs(html, "html.parser")
        hem_class = soup.find("li")
        hem_sample = hem_class.find("a")["href"]
        full_photo_link = (f"https://marshemispheres.com/{hem_sample}")
        link_list.append(full_photo_link)
        time.sleep(1)

    browser.quit()

    hemisphere_info = [
        {"title": "Cerberus Hemisphere", "img_url": link_list[0]},
        {"title": "Schiaparelli Hemisphere", "img_url": link_list[1]},
        {"title": "Syrtis Major Hemisphere", "img_url": link_list[2]},
        {"title": "Valles Marineris Hemisphere", "img_url": link_list[3]}
    ]

    mars_dict = {
        "mars_title": news_title,
        "mars_paragraph": news_p,
        "mars_image": featured_image_url,
        "mars_table": mars_html_table,
        "mars_hemispheres": hemisphere_info
    }

    return mars_dict



