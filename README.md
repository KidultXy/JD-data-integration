# JD Computer Information Collection and Integration

## Background

With the development of the times and the widespread use of electronic information, computers have become a necessity in the lives of most people. However, the purchase of computers has often made consumers hesitate due to factors such as price and availability. In response to this demand, we came up with the idea of integrating computer information from e-commerce platforms. This involves collecting and integrating basic product information such as brand, price, and specifications, as well as analyzing user reviews and information about sellers and platforms.

To analyze consumer habits, we chose JD.com as our crawling platform. JD.com is the most popular choice for purchasing computers in China in the 21st century. It provides excellent logistics, consultation, after-sales support, and feedback platforms. By crawling data from JD.com, we can provide clearer information integration and analysis based on the information provided by the platform. This is greatly beneficial in guiding consumers to choose the computer that best suits their needs.

## Brief Introduction

We focused on digital product information on JD.com ([https://www.jd.com](https://www.jd.com/)) and crawled a total of 398 product pages. The architecture of the crawler, storage of web information, data cleaning, and visualization were implemented using the knowledge we acquired in the Data Collection and Integration course, with some additional enhancements. Our goal was to create a relatively comprehensive, clear, and user-friendly platform.

**The features of this project are as follows:**

- Includes hundreds of computer product information from JD.com.
- Supports keyword search.
- Supports login and registration functionality.
- Completed word cloud generation for reviews.
- Supports visualization of big data dashboard.
- The above features can be expanded to other categories on JD.com.

**The languages and technology stack used in the project are as follows:**

* Data cleaning
  * Python

* Web scraping framework
  * Beautiful Soup & Selenium
* Frontend framework
  * Flask 

* Frontend page beautification
  * HTML + CSS + JS
  * jQuery
  * Bootstrap 
  * Echarts + Pyecharts

## File Description

1. `preview-pics`: Contains overview images of our website information.

2. `jd_crawler`: JD data crawler.

3. `static`: Contains CSS, images, JS, and other files used for frontend visualization, making it easier for Flask framework rendering.

4. `templates`: HTML files for frontend interface rendering using the Flask framework.

   > 1. `index`: Login page.
   > 2. `register`: Registration page.
   > 3. `view`: Homepage.
   > 4. `search`: Display and search for all products.
   > 5. `details`: Display specific product information and visualization.
   > 6. `result`: Dashboard for displaying all product information.
   > 7. `team`: Basic webpage information and division of work page (intended to be improved as a user information interface in the future).

5. `visualize`: Data processing using Pandas and data visualization.

6. `wordcloud`: Word cloud generation.

7. `app.py`: Main file for Flask port integration. Run the program by configuring the environment and executing app.py directly.

8. `sql`/`jd.sql`: Stores the database structure and some data. You can directly import it into the local database by using "source" command. 

   > Note that the sql file does not contain repeated records for `products_details_info`/`products_basic_info`/`products_comment_info`. For those, you can import the corresponding product comment information from the `jd_crawler`'s `jd_computer` and `comment` folders in batch.

