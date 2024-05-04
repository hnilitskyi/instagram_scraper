Instagram scraper
Is a Python application designed to collect data on the followers of a specified Instagram account. It utilizes the instagpy library for interacting with the Instagram API to fetch follower data. The scraper allows users to input their Instagram login credentials and add multiple accounts for scraping, providing flexibility in data collection. Upon specifying a target username, the scraper retrieves the followers for that account, handling pagination to ensure all followers are captured.

The application provides real-time feedback on the scraping process, displaying the scraped follower data for each account in a text area. Additionally, the scraper saves the scraped follower data to JSON files, facilitating further analysis or storage of the collected data. Overall, the Instagram scraper offers a convenient solution for gathering follower information from Instagram accounts for various purposes, such as social media analysis, marketing research, or audience engagement strategies.

     Features
Login Functionality: Users can input their Instagram username and password to log in to the Instagram account for scraping data.
Adding Multiple Accounts: Users can add multiple Instagram accounts for scraping data, allowing for flexibility and scalability in data collection.
Scraping Followers: The scraper collects data on followers for a specified target username by leveraging the instagpy library. It handles pagination to gather all followers.
Output Display: The application provides a text area to display the scraped follower data for each account, allowing users to monitor the scraping process and view results in real-time.
Output to JSON: The scraped follower data is saved to JSON files, with each file named after the target username for easy identification and retrieval of data.
    
     How to Use
Make sure to install:
PyQt5 and InstaGPy

Login Credentials:
Enter your Instagram username in the "Username for login" field.
Enter your Instagram password in the "Password for login" field.
Click the "Add User for Login" button to add the account for scraping.
Specify Target Username:
Enter the username for which you want to scrape followers in the "Target username" field.
Start Scraping:
Click the "Scrap!" button to initiate the scraping process.
The application will log in to each added account sequentially and scrape followers for the specified target username.
The scraped follower data will be displayed in the text area, and JSON files will be saved with the follower data for each account.
View Results:
Monitor the output text area to view the progress and results of the scraping process.
JSON files containing the scraped follower data will be saved in the same directory as the script, with filenames based on the target username.
Note: Ensure you have installed the required dependencies, including PyQt5, instagpy, and any other necessary libraries, before running the script.
