# Import the User and Post classes from the respective files
from user import User
from post import Post

# Define the SocialMediaPlatform class
class SocialMediaPlatform:
    def __init__(self):
        # Initialize dictionaries to store users by email and username, and a variable to keep track of the logged-in user
        self.users_by_email = {}
        self.users_by_username = {}
        self.logged_in_user = None

    def create_account(self, name, address, email, username):
        # Method to create a user account
        # Checks if the provided email or username is already used, if yes, returns None
        # If not, creates a new User object, adds it to the dictionaries, and returns the user object
        # This method ensures uniqueness of email and username for each user
        if email in self.users_by_email or username in self.users_by_username:
            return None

        user = User(name, address, email, username)
        self.users_by_email[email] = user
        self.users_by_username[username] = user
        return user

    def login(self, username):
        # Method to log in a user
        # Given a username, it retrieves the corresponding User object from the dictionaries
        # If the user exists, sets the logged_in_user variable to the User object and returns True
        # If the user doesn't exist, returns False
        user = self.users_by_username.get(username)
        if user:
            self.logged_in_user = user
            return True
        return False

# The main program with the text-based user interface
if __name__ == "__main__":
    # Create an instance of the SocialMediaPlatform class
    platform = SocialMediaPlatform()

    # Start an infinite loop for user interaction
    while True:
        print("\nWelcome to the Social Media Platform!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Account creation option
            # Prompt the user to input details for creating a new account
            # Call the create_account method to create the account and display success/failure message
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            email = input("Enter your email: ")
            username = input("Choose a username: ")

            user = platform.create_account(name, address, email, username)
            if user:
                print("Account created successfully!")
            else:
                print("Email or username already in use. Account creation failed.")

        elif choice == "2":
            # Login option
            # Prompt the user to enter their username for login
            # Call the login method to authenticate the user and display success/failure message
            username = input("Enter your username: ")
            if platform.login(username):
                print(f"Welcome, {platform.logged_in_user.name}!")
                # Start a nested loop for user options after successful login
                while True:
                    print("\nUser Options:")
                    print("1. Create a Post")
                    print("2. See Other Posts")
                    print("3. Follow a User")
                    print("4. See Friend Suggestions")
                    print("5. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        # Post creation option
                        # Prompt the user to enter the post content and call the post_message method
                        post_content = input("Enter your post: ")
                        platform.logged_in_user.post_message(post_content)
                        print("Post created successfully!")

                    elif user_choice == "2":
                        # View other posts option
                        # Iterate over all users and call the display_posts method for each user
                        print("\nAll Posts:")
                        for user in platform.users_by_username.values():
                            user.display_posts()

                    elif user_choice == "3":
                        # Follow a user option
                        # Prompt the user to enter the username of the user they want to follow
                        # Call the follow_user method for the logged-in user
                        follow_username = input("Enter the username of the user you want to follow: ")
                        user_to_follow = platform.users_by_username.get(follow_username)
                        if user_to_follow and user_to_follow != platform.logged_in_user:
                            platform.logged_in_user.follow_user(user_to_follow)
                            print(f"You are now following {follow_username}!")

                    elif user_choice == "4":
                        # Friend suggestions option
                        # Call the get_friend_suggestions method for the logged-in user
                        # Display the friend suggestions (usernames) to the user
                        print("Friend Suggestions:")
                        for suggested_friend in platform.logged_in_user.get_friend_suggestions():
                            print(suggested_friend.username)

                    elif user_choice == "5":
                        # Logout option
                        # Display a goodbye message, reset the logged-in user, and break out of the nested loop
                        print(f"Goodbye, {platform.logged_in_user.name}!")
                        platform.logged_in_user = None
                        break
                    else:
                        print("Invalid option. Please try again.")

            else:
                print("Login failed. Invalid username.")

        elif choice == "3":
            # Exit option
            # Display a goodbye message and break out of the main loop to terminate the program
            print("Exiting the Social Media Platform. Goodbye!")
            break

        else:
            # Invalid option handling
            print("Invalid option. Please try again.")