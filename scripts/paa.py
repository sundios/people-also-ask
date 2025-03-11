#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: konradburchardt
"""

import undetected_chromedriver as uc
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_stealth_driver():
    """Set up an undetected Chrome WebDriver to avoid Google bot detection."""

    options = uc.ChromeOptions()
    options.headless = False  # Set to True for headless mode
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
    options.add_argument("--disable-popup-blocking")

    driver = uc.Chrome(options=options)

    print("✅ Stealth Chrome Driver Ready")
    return driver

def search(query, clicks, lang):
    """
    Opens Google, enters a query, clicks PAA questions, and extracts answers.
    Parameters:
    query (str): The search query
    clicks (int): Number of PAA questions to click
    lang (str): Language code ('en' or 'es')
    """

    driver = get_stealth_driver()

    try:
        # Step 1: Open Google
        google_url = f"https://www.google.com?hl={lang}"
        print(f"🔎 Opening Google: {google_url}")
        driver.get(google_url)
        time.sleep(random.uniform(5, 8))  # Human-like delay

        # Step 2: Find search bar and enter query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(random.uniform(6, 10))

        # Click and extract PAA questions and answers
        extract_paa_questions(driver, clicks)

    except Exception as e:
        print(f"❌ Error: {str(e)}")

    finally:
        driver.quit()

def extract_paa_questions(driver, clicks):
    """
    Clicks 'People Also Ask' (PAA) questions in order (top-to-bottom)
    and extracts all expanded questions.
    Parameters:
    driver: Selenium WebDriver instance
    clicks (int): Number of PAA questions to click
    """
    try:
        paa_data = set()  # Store unique questions
        clicked_count = 0  # Track how many questions were clicked

        while clicked_count < clicks:
            # Get all PAA questions currently available
            paa_questions = driver.find_elements(By.XPATH, "//div[contains(@jsname,'N760b')]//div[contains(@jsname,'tJHJj')]")

            if clicked_count >= len(paa_questions):
                print("⚠️ No more new questions available to click.")
                break  # Stop if we run out of questions

            # Click the next available question (top-to-bottom)
            try:
                question = paa_questions[clicked_count]  # Select the question in order
                question_text = question.text.strip()

                if question_text and question_text not in paa_data:
                    print(f"🔹 Clicking question #{clicked_count+1}: {question_text}")
                    driver.execute_script("arguments[0].click();", question)
                    time.sleep(random.uniform(2, 3))  # Delay to simulate human behavior

                    paa_data.add(question_text)  # Store question to avoid duplicates
                    clicked_count += 1  # Increment click count

                    # Wait and refresh the list after clicking
                    time.sleep(2)

            except Exception as e:
                print(f"⚠️ Skipping question due to error: {str(e)}")
                break  # Stop clicking if an error occurs

        # Step 3: Extract all expanded questions (including new ones added)
        time.sleep(3)  # Allow new questions to load
        all_visible_questions = driver.find_elements(By.XPATH, "//div[contains(@jsname,'N760b')]//div[contains(@jsname,'tJHJj')]")

        for q in all_visible_questions:
            q_text = q.text.strip()
            if q_text:
                paa_data.add(q_text)

        # Convert to DataFrame and save results
        df = pd.DataFrame(sorted(paa_data), columns=["Questions"])
        df.to_csv("paa_results.csv", index=False, encoding="utf-8")
        print("\n✅ Saved results to 'paa_results.csv'")
        print(df)

    except Exception as e:
        print(f"❌ Error clicking PAA questions: {str(e)}")

# Get user input
query = input("Add your query: ")
clicks = int(input("How many questions do you want to click?: "))
lang = input("Please select your language (en/es): ")

# Run search
search(query, clicks, lang)
