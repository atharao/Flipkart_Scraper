# Flipkart Mobile Product Scraper

This is a Python script that scrapes mobile product data from Flipkart's search results and displays it in both CSV format and a PrettyTable.

## Features

* Scrapes product name, price, offer percentage, and specifications from Flipkart.
* Writes data to a CSV file for further analysis.
* Displays the data in a well-organized PrettyTable for easy reading.

## Tools and Technologies

* Python 3.x
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): A library for web scraping HTML and XML documents.
* [PrettyTable](https://github.com/jazzband/prettytable): A library for creating neat tables in the terminal.
* [argparse](https://docs.python.org/3/library/argparse.html): A library for parsing command-line arguments.


## Installation

Ensure you have Python 3.x installed along with the following libraries:

* beautifulsoup4
* prettytable

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 

```
```bash
pip install prettytable 

```

## How to Use

Run the script from the command line with a page number as an argument. The script will scrape the mobile products from the specified Flipkart page and generate a CSV file named "products.csv" in the current directory.

```bash
python flipkart_scraper.py 1
 
```
The above command will scrape the first page of Flipkart's search results for mobile products.If you want Scrape the Second Page repace 1 with 2 and so on....

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.