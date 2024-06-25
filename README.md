# Calculator

### Dependencies:

`1. Python3
`
`2. Tkinter`
(`pip install tkinter`)
### to run the code type👇:
`python calculator.py`
# grade_tracker.py
A simple Python program to track and manage student grades. The program allows the user to input grades for different subjects or assignments, calculate the average grade, and display the overall grade along with the letter grade and GPA.

## Features

- **Add Grade:** Input grades for different subjects or assignments.
- **Display Grades:** View all entered grades, the calculated average grade, corresponding letter grade, and GPA.
- **Calculate Average:** Computes the average of all entered grades.
- **Get Letter Grade:** Converts the average grade to a letter grade based on a standard scale.
- **Get GPA:** Converts the average grade to a GPA based on a standard scale.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/brithvik1/grade_tracker.py.git
    cd grade_tracker
    ```

2. Ensure Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/).

## Usage

1. Open the project in your preferred code editor (e.g., Visual Studio Code).

2. Run the program:

    ```sh
    python grade_tracker.py
    ```

3. Interact with the program through the terminal:

    ```
    1. Add Grade
    2. Display Grades
    3. Exit
    Choose an option:
    ```

    - **Add Grade:** Choose option `1`, then enter the subject and grade when prompted.
    - **Display Grades:** Choose option `2` to view all entered grades, the average grade, letter grade, and GPA.
    - **Exit:** Choose option `3` to exit the program.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

# Social Media Platform - README

## Overview

This project is a simple text-based social media platform that allows users to create accounts, post messages, comment on posts, follow other users, and receive friend suggestions based on their followed accounts. The platform is built using Object-Oriented Programming (OOP) concepts and includes the use of Data Structures and Algorithms (DSA) to efficiently manage user data and perform various operations.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
4. [Data Structures and Algorithms (DSA)](#data-structures-and-algorithms-dsa)
5. [Time and Space Complexity](#time-and-space-complexity)
6. [Functions and Descriptions](#functions-and-descriptions)
7. [Usage](#usage)
8. [Conclusion](#conclusion)

## Introduction

The Social Media Platform is a command-line application developed in Python. Its primary purpose is to simulate a basic social media experience where users can interact by posting messages, following each other, and receiving friend suggestions.

## Features

1. Account Creation: Users can create new accounts with unique usernames and emails.
2. Login: Users can log in with their usernames to access their accounts.
3. Post Messages: Logged-in users can post messages to share with their followers.
4. Comment on Posts: Users can comment on posts made by other users.
5. Follow Users: Users can follow other users to see their posts in their feed.
6. Friend Suggestions: The platform suggests friends based on the accounts the user is following.
7. Post Likes: Users can like posts made by others.

## Object-Oriented Programming (OOP)

This project extensively utilizes OOP principles to create well-organized and modular code. The main classes used in the project are:

1. `User`: Represents a user account with attributes like name, address, email, and username. It contains methods for posting messages, commenting on posts, following users, and getting friend suggestions.

2. `Post`: Represents a user's post with attributes like the user who created the post, content, and the number of likes. It has a method to add likes to a post.

3. `SocialMediaPlatform`: This class is the core of the social media platform. It handles account creation, login, and user interactions. It maintains dictionaries to store users by email and username for quick access.

## Data Structures and Algorithms (DSA)

The project uses the following DSA concepts:

1. **Dictionaries**: Dictionaries are used to efficiently store user data and retrieve users by their email and username.

2. **Sets**: Sets are used to store the friends of a user. Sets allow efficient membership checks and eliminate duplicate entries.

## Time and Space Complexity

- The time complexity of account creation and login methods is O(1) as they involve constant-time operations like dictionary lookups and insertions.

- The time complexity of posting messages, commenting on posts, and following users is also O(1) as they involve simple data structure operations like appending to lists and adding to sets.

- The time complexity of getting friend suggestions is O(N*M) in the worst case, where N is the number of friends of the user and M is the average number of friends of the user's friends.

- The space complexity of the project is linear, O(N), where N is the number of users. Each user's data is stored in the dictionaries, and the number of users directly impacts the space consumption.

## Functions and Descriptions

1. `create_account(name, address, email, username)`: Creates a new user account with the provided details. Returns the created user object or None if the email or username is already in use.

2. `login(username)`: Logs in the user with the given username. Returns True if the user exists, False otherwise.

3. `post_message(message)`: Allows the logged-in user to post a message on their account.

4. `comment_on_post(post, comment)`: Adds a comment to the specified post.

5. `follow_user(user)`: Allows the logged-in user to follow another user.

6. `get_friend_suggestions()`: Returns a set of friend suggestions based on the accounts the user is following.

7. `like_post(post)`: Increments the number of likes for the specified post.

8. `display_posts()`: Displays all posts of the user along with their username.

9. `display_friends()`: Displays the usernames of all friends of the user.

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the `social_media_platform.py` file with a compatible Python interpreter (e.g., Python 3.8+).
3. Follow the on-screen instructions to create an account, login, and interact with the social media platform.

## Conclusion

The Social Media Platform project demonstrates the application of OOP principles and DSA concepts to build a basic social media simulation. Users can create accounts, post messages, follow other users, and receive friend suggestions. This project serves as a foundation for further enhancements and more sophisticated social media
