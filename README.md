Reddit Task script instructions

This script uses the Reddit API to authenticate the user via OAuth2 and fetch the latest 5 posts from a specific subreddit. The script displays the title, author, and upvote count for each post.

How to Run the Script:

1. Clone or copy the files into one folder. You should have the following files:
   - `pp.py` (main Python script)
   - `.env` file with your API credentials

2. Install dependencies:
   Open a terminal and run: 
   pip install requests
   pip install python-dotenv

3. Set your API credentials in the `.env` file:
   In the `.env` file, add the following:

   Example of `.env` file 

   CLIENT_ID=1234
   CLIENT_SECRET=1234
   USER_AGENT=1234

   Replace `your_client_id`, `your_client_secret`, and `your_user_agent` with your actual Reddit API credentials.

4. Run the script:
   In the terminal, run:

The script will automatically authenticate and fetch the latest 5 posts from the `python` subreddit. If you want to change the subreddit, simply modify the subreddit name in the script.

5. Expected output:
    If everything is set up correctly, the script will display the title, author, and upvote count for each post:
