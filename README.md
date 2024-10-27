# Automated Bot Scripts for Hack SoDA 2024

This repository contains three Python bot scripts developed as part of a hackathon project for Hack SoDA 2024 at Arizona State University. The bots are designed for various activities, including brute-force login attempts, cart abandonment simulation, and automated content scraping with review posting.

## Project Overview

These scripts demonstrate automation capabilities for different e-commerce scenarios and showcase the challenges and ethical considerations related to bot detection and prevention. Each bot serves a unique purpose within a simulated environment:

### 1. Brute Force Login Bot
This bot attempts multiple login combinations on a target login page, designed for testing authentication resilience. It showcases common bot behaviors in brute-force scenarios.

- **Technologies**: Selenium, Python
- **Functionality**: Repeated login attempts with varying credentials
- **Use Case**: Demonstrates the need for CAPTCHA, rate-limiting, and bot detection on login pages.

### 2. Cart Abandonment Bot
Simulates a user adding items to the cart without completing the purchase, mimicking typical cart-stuffing and abandonment behavior.

- **Technologies**: Selenium, Python
- **Functionality**: Adds items to the cart and simulates a user abandoning the session
- **Use Case**: Useful for studying cart-abandonment patterns and designing countermeasures.

### 3. Content Scraping and Review Bot
Automates the process of scraping content from a page and posting reviews on products, simulating scenarios where bots interact with page content.

- **Technologies**: Selenium, BeautifulSoup, Python
- **Functionality**: Extracts content data and posts reviews on specified product pages
- **Use Case**: Highlights bot detection and prevention strategies on content and review platforms.

## Prerequisites

- **Python 3.8+**
- **Selenium WebDriver** (ChromeDriver is recommended)
- **BeautifulSoup4** (for the content scraping bot)

## Usage

Run each script individually after configuring the target URLs and relevant parameters. Ensure the necessary credentials and access rights if testing on secure sites.

> **Disclaimer**: These scripts are for educational and research purposes only. Unauthorized use on live websites is strictly prohibited and may violate terms of service.

---

This project was created as part of a hackathon challenge to explore automation and bot behavior, focusing on ethical testing in a controlled environment.
