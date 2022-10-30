# Web Scrapper for Encircle
This is test app for Webscrapping website with various Tyres.

# App Design
<p align="center">
  <img src="https://github.com/mtmak9/Encircle-Python-Test/blob/Projects/App_design.png" alt="Banner"/>
</p>

![Github license](https://img.shields.io/github/license/mtmak9/Encircle-Python-Test)

## Description
Scrape at least one website from the list below using a set
of 3-part tyre inputs provided. Store the data in a database CSV or SQLite3.

Require the following information per tyre price:
- Name of Website Scraped (www.national.co.uk, www.blackcircles.com)
- Tyre brand (Bridgestone, Michelin)
- Tyre pattern (Turanza T001, Ecopia EP500)
- Tyre Size (205/55. 16 V (91), 225/50. 16 W (100) XL)
- Seasonality (if available) (Summer, Winter)
- Price

## Key Features
- Scrape website safely using BeautyfullSoup4, and parsle information to CSV file using designed columns
- App create file with website_name and datetime for easy recognise files
- App fetch data about counting Reviews if avaible in service
- App fetch name,size,speedrating of fetched Tyres
- Export to CSV file or Can activate Database in SQLite3 and export data to SQL Database

## Instruction
1. Select service to use
2. Type correct Tyre details: 1. Width, 2. Profile, 3. Size
3. Click Start button to Fetch data and export Output with result to CSV file in same folder application exist

*STOP button kill application or working script


