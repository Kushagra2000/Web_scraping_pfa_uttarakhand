# Web_scraping_pfa_uttarakhand
Web scraping script to scrape text articles from PFA-Uttarakhand's archived website

Link to target site: https://web.archive.org/web/20150102141104/http://pfauttarakhand.org/


I used the BeautifulSoup package in my Python script for scraping all text articles containing information regarding animal abuse and rescue operations. The site was hosted on archive.org's (https://archive.org/) Wayback Machine(https://archive.org/web/). I obtained all snapshots pertaining to the various time period's in the site's uptime using the wayback-machine-scraper command line utility by sangaline(https://github.com/sangaline/wayback-machine-scraper) and collected all hyperlinks from the snapshots while disregarding header data.  
