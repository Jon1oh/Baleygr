
# Project Name

Baleygr

# Project Description

The creation of a program that can proactively scan the World Wide Web (WWW) to identify
and take down phishing sites acting as authorities of the
Singapore Government. This will be done by efficiently and cost effectively crawling, scraping
and taking screenshots of URLs at scale to handle more than 1 million pages / day on a continuous basis.

# Installation

For the use of this program, the required modules include:

1. requests

2. bs4

```python
pip install requests

pip install bs4
```

# Usage

For the usage of this program, the main URL should be given in the first phrasing,
Then BeauitfulSoup will be used to retrieve the content of the given URL page.
The program will then scrape the content for any URL links, before depositing the links onto
the included .JSON file. 






