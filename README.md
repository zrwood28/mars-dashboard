# web-scraping-challenge
Scraping data from various sites in order to create a Mission to Mars webpage. 

## Summary
Various Mars-based websites with news and information about the planet were visited in order to create a singular page to hold a collection of data. In a jupyter
notebook, these four websites were parsed for specific attributes, such as news headlines and descriptions, images, and comparisons to Earth. The scraping delivered a
dictionary that was stored in a function to be called upon by a Flask site. This site displays all the elements from the four webpages and also has an interactive button
run the scrape function and populate the page with new Mars data if it had been updated on each respective source page. 
