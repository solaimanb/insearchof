import os
from datetime import datetime
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def setup_driver():
    driver = webdriver.Chrome()
    return driver


def open_google(driver):
    driver.get("https://www.google.com")
    print("Google opened!")


def perform_search(driver, query):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    print(f"Search performed for: {query}")


def capture_screenshot(driver, query, folder="screenshots"):
    os.makedirs(folder, exist_ok=True)

    page_width = driver.execute_script("return document.body.scrollWidth")
    page_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(page_width, page_height)

    sanitized_query = query.replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = os.path.join(folder, f"{sanitized_query}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot captured and saved as: {screenshot_path}")
    return screenshot_path


def extract_results(driver):
    time.sleep(5)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    print(f"Found {len(results)} results!")

    extracted_data = []
    for result in results:
        try:
            title = result.text
            link = result.find_element(By.XPATH, "..").get_attribute("href")
            extracted_data.append((title, link))
            print(f"Extracted: {title} - {link}")
        except Exception as e:
            print(f"Error extracting result: {e}")

    return extracted_data


def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.ID, "pnnext")
        next_button.click()
        print("Navigated to the next page.")
        return True
    except NoSuchElementException:
        print("No more pages to navigate.")
        return False


def save_results_to_csv(results, query, page_number, folder="csv_results"):
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    sanitized_query = query.replace(" ", "_")
    filename = os.path.join(folder, f"{sanitized_query}_{timestamp}.csv")

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(results)
    print(f"Results saved to {filename}")
    return filename


def main():
    query = input("Enter your search query: ")
    max_pages = int(input("Enter the maximum number of pages to scrape: "))
    driver = setup_driver()

    try:
        open_google(driver)
        perform_search(driver, query)

        page_number = 1
        all_results = []

        while page_number <= max_pages:
            print(f"Scraping page {page_number}...")
            capture_screenshot(driver, f"{query}_page_{page_number}")
            results = extract_results(driver)
            all_results.extend(results)
            save_results_to_csv(results, query, page_number)

            if not go_to_next_page(driver):
                break
            page_number += 1
            time.sleep(2)

            print(f"Scraped {len(all_results)} results across {page_number - 1} pages.")

    finally:
        driver.quit()
        print("Browser closed!")


if __name__ == "__main__":
    main()
