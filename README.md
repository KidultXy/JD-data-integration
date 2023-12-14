# JD Computer Information Collection and Integration

Final Project for the 2022 Data Collection and Integration Course

1. Python
2. Flask Framework
3. Pandas
4. Beautiful Soup
5. HTML + CSS + JS
6. jQuery
7. Bootstrap Framework
8. Echarts + Pyecharts

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

