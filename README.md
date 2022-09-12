# Scrape Asta

This README is intended to help new developers, attempting to do web scraping for
the first time, to understand how to build something similar to this web
scraper.

- [Getting Started](#getting-started)
- [Project Background](#project-background)
- [Challenge](#challenge)
- [Choice of Technologies](#choice-of-technologies)
- [Minimizing Web Scraping](#minimizing-web-scraping)
- [Extracting Button Click Handler](#extracting-button-click-handler)

## Getting Started

```sh
# Set up virtual environment:
python -m venv .venv
# Activate virtual environment (this step is repeated for every new shell):
source ./.venv/bin/activate
# Install dependencies
pip install bs4 requests
# Try running it:
python -m scrape doFileDownload
```

## Project Background

Student enrollment statistics are public information in Sweden. A friend of mine
was interested in performing data analysis on the data. Without knowing what the
purpose was I wanted to help him extract the data that he needed, using their
API if possible.

## Challenge

My friend explained to me that he wanted to automate the following flow:

1. Navigate to https://www.uhr.se/statistik
2. Choose time period.
3. Perform empty search.
4. Click a button on the resulting page with the text "Spara som CSV-fil" (Save
   as CSV-file)

## Choice of Technologies

My friend wants to learn Python, so that directed my choice of technologies. In
order to guide him towards stable packages I recommended and used the
most commonly libraries for doing scraping in Python,
[requests](https://pypi.org/project/requests/) and
[beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

## Minimizing Web Scraping

The amount of web scraping used to solve any problem should be minimized. This is because most other approaches are faster, less brittle and are less dependent on the design of any given web page. Accordingly, I first explored the site to discover whether the steps in
[Challenge](#challenge) could somehow be reduced.

I discovered that the result of the selected time period is sent as a [search parameter](https://developer.mozilla.org/en-US/docs/Web/API/URL/search) to the second, meaning that the first three steps can be replaced by a request to the second page with [interpolated values for the search string and the time period](https://github.com/jrasmusbm/scrape/blob/6bc3358a944d4010b971a195828f88ece196af9b/scrape.py#L12-L13).

## Extracting Button Click Handler

Upon page load event listeners are registered, that respond to actions on the
page, like clicking a given button. As a next step in my investigation I decided
to use web scraping to determine the source code for the button. This could just
as easily have been done in a browser, but it's a good use case for
demonstrating how you can use code to parse a web page.

I wrote a helper that takes a function name and tries to locate that function
in the website code. If it is able to find it, it prints the function and its
body. This allows for quick exploration of the behavior of the button. As
a result I discovered that it uses some logic to build a URL which it then uses
to query for the CSV.

The next step would be to reproduce that logic in python. Who knows, maybe we
can hit the API directly and do not have to do web scraping at all? 🤔
