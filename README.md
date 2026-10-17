# URLify

A feature-rich command-line interface (CLI) tool built in Python for shortening links using various URL shortener providers and services.

## Features

* Multi-Provider Support: Supports multiple link-shortening services including TinyURL, Is.gd, Da.gd, Clck.ru, Chilp.it, and Ttm.sh.
* Authentication Integration: Supports API keys and user credentials for premium/account-based shorteners such as Bit.ly, Cutt.ly, Adf.ly, Ow.ly, Short.cm, and Tiny.cc.
* Interactive Menu: Terminal interface for choosing shorteners and entering requirements.

## Prerequisites

Ensure you have Python installed along with the `pyshorteners` library:

* Python: 3.x
* pyshorteners Library: Install via pip:

  ```
  pip install pyshorteners
  ```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/musaddiq-sultan/URLify.git
   cd URLify
   ```

2. Install required dependencies:

   ```
   pip install pyshorteners
   ```

## How to Use

Run the script directly from your terminal:

```
python main.py
```

### Steps to Shorten a Link

1. Select a Shortener: Choose from the list of available shorteners by typing its corresponding number (1 to 16).
2. Provide Required Credentials (If Applicable):
   * For standard services (e.g., TinyURL, Is.gd), no additional key is required.
   * For account-based services (e.g., Bit.ly, Cutt.ly), input your API key or user credentials when prompted.
3. Input Target Link: Enter the full URL you wish to shorten.
4. Output Generation: The shortened URL will be generated and displayed in the terminal.