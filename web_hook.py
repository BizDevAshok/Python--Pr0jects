import requests

# Your webhook URL here
webhook_url = "https://socialmedia.com// your_webhook_token"

# The message you want to send
data = {
    "content": " Hello guys New post from following platform."
}

# Send the POST request to the webhook URL
response = requests.post(webhook_url, json=data)

# Check the response
if response.status_code == 204:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed: {response.status_code}, {response.text}")
