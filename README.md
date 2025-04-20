<h1>TeslaCarFinder</h1>

<p><strong>TeslaCarFinder</strong> is a Python bot that checks the stock status of a user-specified vehicle on Tesla's Turkish website and sends a notification via Telegram when the stock status changes. This bot periodically checks Tesla's inventory page, searches for the specified vehicle, and sends a Telegram message if it is available. The vehicle you want to search for can be changed by modifying the <strong>target_text</strong> variable in the code.</p>

<h2>Features</h2>
<ul>
    <li>Checks the stock status of a user-specified vehicle on Tesla's Turkey site.</li>
    <li>If the vehicle is available, sends a notification to the user via Telegram bot.</li>
    <li>Updates stock status every 2 hours.</li>
    <li>Safely stores the necessary API information for the Telegram bot in a <strong>.env</strong> file.</li>
</ul>

<h2>Requirements</h2>
<p>To run this project, you'll need the following tools and libraries:</p>
<ul>
    <li>Python 3.7+</li>
    <li>Telegram Bot API Token (Create a bot and obtain the token)</li>
    <li>Telegram Chat ID (The ID of the user or channel that will use the bot)</li>
    <li>Python libraries:
        <ul>
            <li><strong>pyautogui</strong>: Used for screen control.</li>
            <li><strong>pyperclip</strong>: Used to get the text copied to the clipboard.</li>
            <li><strong>requests</strong>: Used for making HTTP requests.</li>
            <li><strong>python-dotenv</strong>: Used for reading environment variables from the <strong>.env</strong> file.</li>
        </ul>
    </li>
</ul>

<h2>Installation</h2>

<h3>1. Install Python</h3>
<p>If you don't have Python installed, download and install the latest version from the <a href="https://www.python.org/downloads/">official Python website</a>.</p>

<h3>2. Install Required Libraries</h3>
<p>Install the required Python libraries by running the following command in the terminal or command prompt:</p>
<pre><code>pip install pyautogui pyperclip requests python-dotenv</code></pre>

<h3>3. Create a Telegram Bot</h3>
<p>Create a bot using <a href="https://core.telegram.org/bots#botfather">Telegram BotFather</a>.</p>
<p>Get the API token for your bot.</p>
<p>Obtain the <strong>chat ID</strong> for the user or channel that will use the bot. You can do this by following these steps:</p>
<ul>
    <li>Search for the bot you created using BotFather in Telegram.</li>
</ul>

<h3>4. Create the .env File</h3>
<p>Create a <strong>.env</strong> file in the project directory and add the following information:</p>

<pre><code>
TELEGRAM_API_TOKEN=your_telegram_api_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
</code></pre>
<p>- Replace <strong>your_telegram_api_token</strong> with the API token of your Telegram bot,</p>
<p>- Replace <strong>your_telegram_chat_id</strong> with the chat ID where the bot will send messages.</p>

<h3>5. Run the Code</h3>
<p>To run the project, use the following command in the terminal or command prompt:</p>
<pre><code>python TeslaCarFinder.py</code></pre>
<p>This code will periodically check the Tesla Turkey website and check the stock status of the vehicle specified by <strong>target_text</strong> every 2 hours. If the vehicle is available, it will send a notification via Telegram.</p>

<h2>Understanding the Code</h2>

<p>The main steps in the <strong>TeslaCarFinder.py</strong> file are:</p>
<ul>
    <li><strong>Open the page and click the "Envanteri Keşfedin" button</strong>: <br> - The <code>webbrowser</code> library is used to open Tesla's Turkey site. <br> - The <code>pyautogui</code> library is used to click specific screen coordinates.</li>
    <li><strong>Copy the page content</strong>: <br> - The entire text of the page is copied using <code>pyautogui</code>'s <code>command + A</code> and <code>command + C</code> key combinations.</li>
    <li><strong>Search for the target vehicle</strong>: <br> - It checks if the <strong>target_text</strong> (e.g., "Model Y") exists in the copied text.</li>
    <li><strong>Send a notification via Telegram</strong>: <br> - If the target vehicle is found, a message is sent to Telegram using the <code>requests</code> library.</li>
    <li><strong>Check every 2 hours</strong>: <br> - The code runs in a loop and checks the Tesla site every 2 hours.</li>
</ul>

<h2>Securing the .env File</h2>
<h3>Hiding the .env File when Uploading to GitHub:</h3>
<p>If you plan to share this project on platforms like GitHub, you can ensure the privacy of your <strong>.env</strong> file by creating a <strong>.gitignore</strong> file in the root directory of the project and adding the following line:</p>
<pre><code>.env</code></pre>
<p>This will prevent the <strong>.env</strong> file from being uploaded to GitHub.</p>

</body>
