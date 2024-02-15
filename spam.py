import requests
import time

# Function to log into Instagram account
def login_to_instagram(username, password):
    session = requests.Session()
    session.headers.update({'user-agent': 'Mozilla/5.0'})

    login_url = 'https://www.instagram.com/accounts/login/'
    login_data = {'username': username, 'password': password}

    try:
        response = session.post(login_url, data=login_data)
        response_json = response.json()
        if response_json.get('authenticated'):
            return session
        else:
            print("Failed to log in. Please check your credentials.")
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred during login:", e)
        return None

# Function to send message to group
def spam_group(session, group_id, message):
    send_message_url = f'https://www.instagram.com/direct_v2/web/threads/{group_id}/broadcast/text/'
    message_data = {'text': message}

    try:
        response = session.post(send_message_url, data=message_data)
        if response.status_code == 200:
            return True
        else:
            print("Failed to send message. Status code:", response.status_code)
            return False
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending message:", e)
        return False

# Main program
if __name__ == "__main__":
    # User input for Instagram credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # User input for group ID and spam text
    group_id = input("Enter the ID of the group you want to spam: ")
    spam_text = input("Enter the text you want to spam: ")

    # Logging into Instagram
    session = login_to_instagram(username, password)
    if session:
        print("Successfully logged in to Instagram.")
        time.sleep(2)

        # Spamming the group
        success = spam_group(session, group_id, spam_text)
        if success:
            print("Successfully spammed the group.")
        else:
            print("Failed to spam the group. Check your credentials or try again later.")
    else:
        print("Failed to log in to Instagram. Check your credentials and try again.")
