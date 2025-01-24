# Currency and commodity price inquiry using bs4 library

This Python script fetches and displays the current price of selected commodities and currencies from the **TGJU** website. The program scrapes real-time price data for various commodities, such as the dollar, gold, quarter, and emami coin.

## Features

- Fetches real-time price data for different commodities.
- Scrapes information from the TGJU website.
- Displays the current price in a user-friendly format.

## Requirements

To run the script, make sure you have the following Python libraries installed:

- `requests` — for making HTTP requests to the website.
- `beautifulsoup4` — for parsing HTML and extracting required information.

You can install the required libraries using `pip`:

```bash
**************************************************
pip install requests beautifulsoup4
**************************************************
```
## How to Use
1. Clone or download this repository.
2. Ensure that the required libraries are installed (as shown in the requirements section).
3. Run the script to retrieve and display the price for different commodities.
## Running the Script
The script is designed to fetch price data for the following commodities:
- Dollar: Fetches the price of the US dollar.
- Gold: Fetches the price of 18K gold.
- Quarter: Fetches the price of the Iranian quarter
- A Emami Coin: Fetches the price of the Emami coin.

To get the price for a particular commodity, use the inquiry() function and provide the symbol of the commodity as a parameter. Example:

```bash
**************************************************
inquiry("dollar")
**************************************************
```
This will print the current price of the dollar by scraping the corresponding TGJU page.
## Example Output

```bash
**************************************************
https://www.tgju.org/profile/price_dollar_rl price : 500,000
**************************************************
```
## How It Works
1. URL Dictionary: A dictionary (URLS) is defined at the start of the script, mapping each commodity symbol (e.g., "dollar", "gold") to its corresponding URL on the TGJU website.
2. inquiry() Function:
- Accepts a symbol (commodity) as a parameter.
- Makes an HTTP request to the URL associated with that symbol.
- Parses the response HTML using BeautifulSoup to extract the price value.
- Extracts and displays the price from the page content.
3. Display Output: The script prints the URL and the corresponding price with clear separation for better readability.

## Currency and commodity price inquiry using Selenium library
This Python script uses Selenium to scrape the real-time prices of popular cryptocurrencies (BTC, ETH, and USDT) from the [Nobitex](https://nobitex.ir/) website.

## Prerequisites

Before running the script, you need to install the following dependencies:

- **Python** 3.x
- **Selenium** library
- **Chrome WebDriver** (or a WebDriver for your browser of choice)

### Installation

1. Install Python if you haven't already from the [official website](https://www.python.org/).
2. Install Selenium using pip:

   ```bash
   **************************************************
   pip install selenium
   **************************************************
    ```
3. Download and install the appropriate Chrome WebDriver for your version of Google Chrome, or use a different WebDriver for browsers like Firefox, Safari, etc.
4. Place the chromedriver executable in your system's PATH or specify its location when initializing the webdriver.Chrome() instance in the code.
## How It Works
This script will:
1. open the Nobitex website: https://nobitex.ir/
2. Scrape the price of a specified cryptocurrency (BTC, ETH, USDT) by extracting the data from the table on the page.
3. Print the current price of the selected cryptocurrency to the console.
4. Close the browser after retrieving the information.
   ## Usage
   The function Digital_currency(symbol) accepts a symbol of the cryptocurrency you want to check. Available symbols are:
- BTC - Bitcoin
- ETH - Ethereum
- USDT - Tether (USDT)
  ## Example
   ```bash
   **************************************************
    Digital_currency("USDT")
   **************************************************
    ```
This will scrape and print the current price of USDT from the Nobitex website.
## Code Explanation
1. URLS Dictionary:
- This dictionary contains the XPaths of the elements on the website where the cryptocurrency prices are located.
- Each key corresponds to a symbol (e.g., BTC, USDT, ETH), and the value is the XPath pointing to the price on the website.
2. Digital_currency Function:
- Accepts a symbol (such as USDT) and uses the corresponding XPath to scrape the price from the website.
- Opens the website in Chrome using Selenium's webdriver.
- Waits for the page to load (sleep(5)).
- Locates the price element using the XPath and prints its text value (the price).
- Finally, it quits the browser instance.
