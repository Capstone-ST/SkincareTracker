# About the SkincareTracker website
Skincare Tracker is a full-stack web application developed as part of our CS 467 capstone project. The goal was to build a helpful, user-friendly, and visually pleasing app that supports people in managing their skincare routines. The app allows users to log skincare products, review products, create daily diary entries, receive timely reminders, and benefit from AI-generated skincare summaries/tips, product recommendation, and product usage guidance. The idea was to mix utility with thoughtful design making skincare tracking not only organized, but also engaging and personalized. It’s built to be both functional and beautiful, designed to make skincare easy, smart, and a little more fun.

# Setup Instructions

To host and run the Skincare Tracker web application on your local machine, follow the steps below:

1. Clone the GitHub Repository: Open your terminal or command prompt and run:  
git clone https://github.com/Capstone-ST/
	SkincareTracker.git

2. Navigate into the Project Directory: Once cloned, change into the project directory:  
cd SkincareTracker

3. Install Required Packages: Ensure you have Python installed, then install the project dependencies:  
    	pip install -r requirements.txt

4. Run the Web Application: Launch the Flask application using:  
python app.py

5. You can now access the locally hosted version of the site by visiting:  
    		http://127.0.0.1:5000 

# Accessing Website
- Users must be connected to the OSU VPN in order to view the running website. 
- The website is hosted on the OSU server and can be accessed here: 
http://flip4.engr.oregonstate.edu:41102/user/login 
- Here is a set of testing credentials to log in to the website:
    * Username: admin
    * Password: 123
- Users can also create a new profile by clicking Register here. After logging in, the user will be taken to the homepage
  and can experiment around with the website.

  
# Screenshots of the Website

# Login Page:
![Loginpage gif](https://private-user-images.githubusercontent.com/156049642/435482286-aff6bcd2-61ae-42a4-8806-28c8eacadf18.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk1MDcsIm5iZiI6MTc0OTAwOTIwNywicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDgyMjg2LWFmZjZiY2QyLTYxYWUtNDJhNC04ODA2LTI4YzhlYWNhZGYxOC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzUzMjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00MWYxYzRlYzA2ZWY4MzA1MmE1YjAyYzNlMjdkYTlmMzk1MmJlZWIyOTgyMjQyNTE2NjQ1MzU1ZTkzOTUxYTc3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.V89ZfFtJeXXATCvaC0yVWAMf9fLMXdAk6pdC3QK__uY)

# Register Page:
![Register Page](https://private-user-images.githubusercontent.com/156049642/435485963-ccb4a3d9-cae2-406a-b369-3b241bb30ec5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk1NTAsIm5iZiI6MTc0OTAwOTI1MCwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg1OTYzLWNjYjRhM2Q5LWNhZTItNDA2YS1iMzY5LTNiMjQxYmIzMGVjNS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzU0MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NjU1MWRkNDM2ZmNkOGUzZTM3MTQyZGVkYTA0ZWYyZWI4MWY3YTM3ZGNmODNjMTU3N2IyNTU2YjU2NzRkN2Y1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LJfGf4qokQWrI23XkXIY4xI6blQzDaWt6sY6aKZt1J4)

# Home Page:
![Home Page](https://private-user-images.githubusercontent.com/156049642/435483820-3b7d139f-d5e2-480b-8ba5-9e40a03cc2b0.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDUxNjgyMTQsIm5iZiI6MTc0NTE2NzkxNCwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDgzODIwLTNiN2QxMzlmLWQ1ZTItNDgwYi04YmE1LTllNDBhMDNjYzJiMC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQyMFQxNjUxNTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MmEzMTM1YjczMDMwYjdlYTNhMjk2NmZlODkxNjZmZWNhODFhMmE0Mzc0ZTFlZWYxYmIxYTcwNTUxZjE1M2JiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.a64R6DSGJXED-IVXw_UTFyDROvsXWzxGwFrEspVbDT0)

# Add Product Page: 
     - API automatically fills in remaining data once typing in product name 
![Add product Demo](https://private-user-images.githubusercontent.com/156049642/435484391-e5472415-145c-4727-89b3-2a867f579eb3.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDUxNjg3MjksIm5iZiI6MTc0NTE2ODQyOSwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg0MzkxLWU1NDcyNDE1LTE0NWMtNDcyNy04OWIzLTJhODY3ZjU3OWViMy5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQyMFQxNzAwMjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MDdlOGY2MmNkYTE2NzZmZDkyODlmOGE1NDE2NDM5YjRjM2U5ZmMxYmUyNTVmMjYwMzhlNGU5NTdiYmYxNjAwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.andLY5teRqpLkFOccBNQ-gbbqflXqdd0AzogBo3cQQc)

# My Collection Page: 

# All Product List Page: 
![ Product list Demo](https://private-user-images.githubusercontent.com/156049642/435485368-26e413be-f6f6-4f53-be85-7b48444acac6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDUxNjk2MTIsIm5iZiI6MTc0NTE2OTMxMiwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg1MzY4LTI2ZTQxM2JlLWY2ZjYtNGY1My1iZTg1LTdiNDg0NDRhY2FjNi5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQyMFQxNzE1MTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NjY1ZDk2YjA4MmMyNmU2Yjc4OWYyMGNkOTliNTBmNzZiMjAzZWRmMjQ3MGE0NGQ1YjE3MGMxNGFmYWRhYjY3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.00YsaoeG2-KiseU_XJ0yczxKDPZ342GF8NmG9LHEpw8)

# Profile/Edit Profile Pages: 
![Profile](https://private-user-images.githubusercontent.com/156049642/435488038-361b6522-01bd-48e1-8cef-aafc75dfc0e9.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk2OTQsIm5iZiI6MTc0OTAwOTM5NCwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg4MDM4LTM2MWI2NTIyLTAxYmQtNDhlMS04Y2VmLWFhZmM3NWRmYzBlOS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzU2MzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTdhZmZjNGQ2YzJkMzMwNTA2ZDgzYTc4MGFkYzZkM2Q3OTgzZjYyNzVlZjY3ZmE3M2UzNWM0ZjMyMDIyMDJmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HxEKOEnZh7J1RyBc3s36jlxrrRyJk03j1ahYdk3_6fM)

# Diary Entries Page:

# Review Page:

# AI Integrations in Website:

# References:
[1] Flask, Quickstart.Flask Documentation. https://flask.palletsprojects.com/en/stable/quickstart/. [accessed June 3, 2025]
[2] OSU CS340, Flask Starter App - GitHub Repository. Oregon State University. https://github.com/osu-cs340-ecampus/flask-starter-app. [accessed June 3, 2025]  
