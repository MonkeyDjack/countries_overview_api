![](RackMultipart20210721-4-1klnj6x_html_944cbfafc4fdd58f.jpg)

# Countries overview Api

USAGE DOCUMENTATION

Mukhitdin Iakhiarov | Data processing | 15.01.2021

# Overview

Countries overview api provides users with various data about mostly all countries in the world.

The provided data consist of 3 different datasets

- Country population statistic
- Country happiness statistic
- Country obesity statistic

# Required libraries

The Api was build in python and in order to run it on another pc, the developer should install pip to install and manage additional packages that are not part of the Python standard library. If Python is not available on the system please follow these steps: 1) Open CMD and type get-pip.py and use the windows store to download the latest Python build. By selecting it and pressing &quot;Get&quot;. 2) Install Python.

![](RackMultipart20210721-4-1klnj6x_html_fd3ab0b8bdb4b791.png)

**To install all the libraries simply open shell in api folder and run**

pip install -r requirements.txt

# Start the api

**Open shell in api folder and type:**

python api.py

# Database

I decided to stick with sqlite due to its efficiency in reading big amounts of data. You can find the db file in the root folder. No need to install it anywhere.

# Routes

127.0.0.1:5000/happiness – World Happiness

127.0.0.1:5000/obesity – World Obesity

127.0.0.1:5000/population – world Population

The data comes in different types depending on headers: application/json, text/xml

# Consumer

To run the consumer, put the folder on localhost e.g Xampp