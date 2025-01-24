# Currency and Commodity Price Inquiry

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
