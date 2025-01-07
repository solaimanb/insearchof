
# **Google Search Automation - #insearchof**

This project automates Google searches using Selenium WebDriver. It performs the following tasks:

- Opens Google.
- Executes a search query entered by the user.
- Navigates through multiple pages of search results.
- Extracts titles and URLs of search results.
- Saves the results to CSV files (one per page).
- Captures screenshots of each page.

---

## **Features**

1. **Automated Search**:
   - Allows the user to input a search query.
   - Handles navigation across multiple pages of search results.

2. **Data Extraction**:
   - Extracts search result titles and URLs.
   - Saves extracted data to CSV files.

3. **Screenshots**:
   - Captures and saves a screenshot of each search results page.

4. **Pagination**:
   - Supports navigating through a user-defined number of pages.

---

## **Project Structure**

```
.
├── main.py              # Main script to run the automation
├── screenshots/         # Folder for storing screenshots (auto-created)
├── csv_results/         # Folder for storing CSV results (auto-created)
├── requirements.txt     # List of required Python libraries
└── README.md            # Project documentation
```

---

## **Requirements**

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/solaimanb/insearchof.git
   cd insearchof
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download and configure ChromeDriver:
   - Ensure ChromeDriver matches your installed Chrome version.
   - Add the `chromedriver` executable to your system PATH or keep it in the project folder.

---

## **Usage**

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the search query when prompted:
   ```
   Enter your search query: Selenium Python
   ```

3. Specify the number of pages to scrape:
   ```
   Enter the maximum number of pages to scrape: 3
   ```

4. The script will:
   - Perform the search.
   - Extract results from each page.
   - Save the results to CSV files in the `csv_results/` folder.
   - Capture screenshots of each page in the `screenshots/` folder.

---

## **Output**

- **CSV Files**:
  Extracted data is saved as individual CSV files, named based on the query and page number:
  ```
  csv_results/Selenium_Python_page_1_YYYYMMDD_HHMMSS.csv
  ```

- **Screenshots**:
  Screenshots are saved for each page:
  ```
  screenshots/Selenium_Python_page_1_YYYYMMDD_HHMMSS.png
  ```

---

## **Customization**

- **Change Browser**: Replace `webdriver.Chrome()` with the desired WebDriver (e.g., `webdriver.Firefox()`).
- **Modify CSS Selectors**: Update the `extract_results` function if the structure of Google search results changes.

---

## **Known Issues**

- Google may trigger CAPTCHA if too many requests are sent. To avoid this:
  - Add a delay (`time.sleep`) between actions.
  - Use proxies or a VPN.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contributing**

Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

---

## **Author**

- **Your Name**
- Email: insearchof.us@gmail.com
- GitHub: [solaimanb](https://github.com/solaimanb)
