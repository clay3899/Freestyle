# Freestyle: Champions are Coming

## Instalation

Fork this repository and then use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

Navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/Freestyle
```

## Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n game-env Pytho=3.7 #first time only
conda activate game-env #after creation
```

Install the requirements.txt file in the environment:

```sh
pip install -r requirements.txt
```

### Setup Environment Variable

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key).

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

```sh
ALPHAVANTAGE_API_KEY = "xxx"
```

In order to receive SMS updates, you must [sign up for a Twilio account](https://www.twilio.com/try-twilio). Click the link in the confiration email to verify your account and confirm the code sent to your phone. 

Then, create a new project with "Programmable SMS" capabilities. From the console you can view the project's Account SID and Auth Token. Make sure to update the contents of the ".env" file to specify these values as environment variables.

```sh
TWILIO_ACCOUNT_SID = "xxx"
TWILIO_AUTH_TOKEN = "xxx"
```

To receive a Twilio phone number to send the messages from click [here](https://www.twilio.com/console/sms/getting-started/build). Then update the contents of the ".env" variable.

```sh
SENDER_SMS= "xxx"
```

Lastly, set an environent variable to specify the intended recipient's phone number (including the plus sign at the beginning).

```sh
RECIPIENT_SMS= "xxx"
```

## Playing the Game

From within the virtual environment, use the following command to run the Python script from the command-line:

```sh
python game/main.py
```
