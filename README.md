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
  - Secure login for returning users to access their personalized skincare dashboard
  - Includes error handling for incorrect login attempts
![Loginpage gif](https://private-user-images.githubusercontent.com/156049642/435482286-aff6bcd2-61ae-42a4-8806-28c8eacadf18.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk1MDcsIm5iZiI6MTc0OTAwOTIwNywicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDgyMjg2LWFmZjZiY2QyLTYxYWUtNDJhNC04ODA2LTI4YzhlYWNhZGYxOC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzUzMjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00MWYxYzRlYzA2ZWY4MzA1MmE1YjAyYzNlMjdkYTlmMzk1MmJlZWIyOTgyMjQyNTE2NjQ1MzU1ZTkzOTUxYTc3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.V89ZfFtJeXXATCvaC0yVWAMf9fLMXdAk6pdC3QK__uY)

# Register Page:
   - Allows new users to create an account
   - Collects basic information like email, age, skin type and password
   - Info gets added to the database and then user must login with new credentials
![Register Page](https://private-user-images.githubusercontent.com/156049642/435485963-ccb4a3d9-cae2-406a-b369-3b241bb30ec5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk1NTAsIm5iZiI6MTc0OTAwOTI1MCwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg1OTYzLWNjYjRhM2Q5LWNhZTItNDA2YS1iMzY5LTNiMjQxYmIzMGVjNS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzU0MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NjU1MWRkNDM2ZmNkOGUzZTM3MTQyZGVkYTA0ZWYyZWI4MWY3YTM3ZGNmODNjMTU3N2IyNTU2YjU2NzRkN2Y1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LJfGf4qokQWrI23XkXIY4xI6blQzDaWt6sY6aKZt1J4)

# Home Page:
   - Central hub after login showing navigation to all major features
   - Includes sidebar access to collections, diaries, reminders, reviews, all products
   - Displays a rotating slideshow of featured popular skincare product visuals for an engaging UI
![Home Page](https://private-user-images.githubusercontent.com/156049642/451188741-10ee7574-083c-413f-aac5-7bbeaabde15c.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTIzNDEsIm5iZiI6MTc0OTAxMjA0MSwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMTg4NzQxLTEwZWU3NTc0LTA4M2MtNDEzZi1hYWM1LTdiYmVhYWJkZTE1Yy5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNDQwNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZTA4N2JlNjY3ZmQyNGI3N2FlZDY5MTVhNWFiNTMwMGRiMDhjOTI0NDMwZTIwY2FhYWVmZDM2YjVjMDA1MGQ2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.YMOWGh0651PZ-0G2asYO6NfyeGxtzozTHUxREtIfLa4)

# Add Product Page: 
     - APIAutofill integration via API to suggest product type, shelf life, and ingredients
     - Users can manually add skincare products to their collection
     - Supports uploading an image for each product
![Add product Demo](https://private-user-images.githubusercontent.com/156049642/451190638-99542aca-f302-4761-ad89-8a8fba91fc0c.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTI2ODIsIm5iZiI6MTc0OTAxMjM4MiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMTkwNjM4LTk5NTQyYWNhLWYzMDItNDc2MS1hZDg5LThhOGZiYTkxZmMwYy5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNDQ2MjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04YzQ3YjQzNGQ4NjUxM2U4YjYyZjVkOGYwMjc3ZDg1Yzk2MTIyZDZiMjYzN2FkMmZlNjhmOTkwN2ZmZWEzOTE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.OVvvjzbt4ArOKJu1tls4vHOSNYP69CCxR1l9yU6anh0)

# My Collection Page: 
   - Displays a user’s personal product collection
   - Includes options to view, edit, or delete individual products
   - Allows users to track products they’re actively using and there is a Ai feature that recommends skincare products based on their collection
![My Collection Demo](https://private-user-images.githubusercontent.com/156049642/451199628-a4bfeb17-b3e8-46a6-bd38-edfb166d6299.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTQxNDYsIm5iZiI6MTc0OTAxMzg0NiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMTk5NjI4LWE0YmZlYjE3LWIzZTgtNDZhNi1iZDM4LWVkZmIxNjZkNjI5OS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTEwNDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMjYwMzk2ZjFhMWZiOGUzYWMyYjg4MjFjNjc3MTYwNjFhYmM5NTFiNTg2Mzk4ZDRiNmM1NjQ0MjgwM2M2NGZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.jutnmWdJJZAGc_G8beJMO1IcnE5O81dAaD8YsFZjQnM)

# All Product List Page: 
    - Lists all shared products across users
    - Users can browse community-added products
    - Features “Add to Collection” button for easy saving
![ Product list Demo](https://private-user-images.githubusercontent.com/156049642/451193754-3d80c893-c715-4276-864c-fbc3bbdf15bb.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTMyMDAsIm5iZiI6MTc0OTAxMjkwMCwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMTkzNzU0LTNkODBjODkzLWM3MTUtNDI3Ni04NjRjLWZiYzNiYmRmMTViYi5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNDU1MDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MTU5YjBkZTZkNTM0NmU5NmZjMGFhNjkzMDQyN2RhZjVlOWEwMjI2MTViY2UyMTMwMWJjMGUyYTAyOGRhZWY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.qnO4UxiIWWvM6385E-D43koW2hQXXUxNC4PmuXHbvFY)

# Profile/Edit Profile Pages: 
   -Displays user info like name, age, skin type, and profile photo
   -Lets users update their information and upload a new photo
   - Accessible through a floating icon for quick changes
![Profile](https://private-user-images.githubusercontent.com/156049642/435488038-361b6522-01bd-48e1-8cef-aafc75dfc0e9.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMDk2OTQsIm5iZiI6MTc0OTAwOTM5NCwicGF0aCI6Ii8xNTYwNDk2NDIvNDM1NDg4MDM4LTM2MWI2NTIyLTAxYmQtNDhlMS04Y2VmLWFhZmM3NWRmYzBlOS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwMzU2MzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTdhZmZjNGQ2YzJkMzMwNTA2ZDgzYTc4MGFkYzZkM2Q3OTgzZjYyNzVlZjY3ZmE3M2UzNWM0ZjMyMDIyMDJmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HxEKOEnZh7J1RyBc3s36jlxrrRyJk03j1ahYdk3_6fM)

# Diary Entries Page w/ Skincare Summary and Skincare Tip Ai Integration:
  - Users log daily skin updates, notes, and photos
  - Entries are processed by GPT to generate:
      * A skincare summary based on behavior and routines
      * A personalized skincare tip
  - Supports edit/delete and photo upload for each entry
![Diary Entries Demo](https://private-user-images.githubusercontent.com/156049642/451198658-c91829f0-0072-4ccc-a2ff-1a806f17f686.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTM5ODIsIm5iZiI6MTc0OTAxMzY4MiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMTk4NjU4LWM5MTgyOWYwLTAwNzItNGNjYy1hMmZmLTFhODA2ZjE3ZjY4Ni5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTA4MDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMzdhZDE4MWY2YzA5MTA1Y2FmNDZkZmVjMjRjYTVmMzIwZjE0ZWZhZWJkNWJkOGVkZDdlNzJkYTU1MmY2YmRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BhWFVmw5d1b6dlTySxYxjZl2DyuzvCufjjmZjcIRHgY)

# Review Page:
  - Users can leave one review per product
  - Shared reviews appear on the product’s info page
  - Helps the "community" by offering other users opinions
![Reviews Demo](https://private-user-images.githubusercontent.com/156049642/451202889-734f6a85-4610-4041-b8f4-e7a5dbad7120.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTQ2ODMsIm5iZiI6MTc0OTAxNDM4MywicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMjAyODg5LTczNGY2YTg1LTQ2MTAtNDA0MS1iOGY0LWU3YTVkYmFkNzEyMC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTE5NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00N2IwODI0MTAxMzhkZDVmNWNlMjFmYjEwNWQ4NWQzOTRkYzNiMjE4NjZiNGRhNmI5Njk3YTQyYjZlOTYxMWM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Q62A6aCt-bq575Qay_hXaL7n56E0S1-e1Mom-C0Z6II)

# Rating Page with Ai generated product usage instruction:
  - When viewing any product, AI generates a usage guide so it helps beginners understand how to properly apply products
  - Users can submit a review by clicking on Write Review button under the Product information
![Ratings Demo](https://private-user-images.githubusercontent.com/156049642/451205910-e77305b5-5b62-426c-9582-8681960bb909.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTUyMTYsIm5iZiI6MTc0OTAxNDkxNiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMjA1OTEwLWU3NzMwNWI1LTViNjItNDI2Yy05NTgyLTg2ODE5NjBiYjkwOS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTI4MzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZDJiMTE3NDk0ZTY3YTQxMzNjZjBhY2FmYzYwOWQ0YzBhY2UzNzZlY2FjMWRhNTdlZjBjZmNhYjBlYjhmZGJlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Z0QzyVQL96gGCxuNy65PXsw9xLIpCQ0VPMU_4c6_LCA)

# Reminder System
  - Lets users set reminders for skincare routines
  - Supports time/date settings and recurrence
  - Sends alerts for product expiration and routine tasks
![Reminders Demo](https://private-user-images.githubusercontent.com/156049642/451201668-98ecab56-b34c-400f-a33f-47d7e690486a.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTQ0ODYsIm5iZiI6MTc0OTAxNDE4NiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMjAxNjY4LTk4ZWNhYjU2LWIzNGMtNDAwZi1hMzNmLTQ3ZDdlNjkwNDg2YS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTE2MjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjQ4YWZiYTRiYzkwOGFhMWFmYjRkMGFlMmQwNWM2OTdmNDY5NzM0ZDRiOTU3NGJlNmI0ZWZiMmY4Yjg2NDkwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.JWyY7SrViYnWovtofHfD73i8V6Nbeo286r9juy5bHdE)

# Add to Collection Feature
  - Users can click one button to save a product from the shared “All Products” list
  - Prevents duplicate data entry
  - Automatically syncs the item into the user’s personal collection 
![Add to Collection Demo](https://private-user-images.githubusercontent.com/156049642/451207516-20b9d95d-e302-4b68-bf06-aebebd4b775a.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkwMTU0ODIsIm5iZiI6MTc0OTAxNTE4MiwicGF0aCI6Ii8xNTYwNDk2NDIvNDUxMjA3NTE2LTIwYjlkOTVkLWUzMDItNGI2OC1iZjA2LWFlYmViZDRiNzc1YS5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYwNFQwNTMzMDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00YzE0N2NiZjAyMjVjZDQ3Mzg3MjRiM2IxMmJkZjFjODM4MjBhYTYzMTI4Njk5NDk5MThlZGI1ZjUxNGNmMDBiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.khyyC_6lmPPawqWK40qzBIRFGur0fbcHtf_ddKCpc4o)

# References:
[1] Flask, Quickstart.Flask Documentation. https://flask.palletsprojects.com/en/stable/quickstart/. [accessed June 3, 2025]

[2] OSU CS340, Flask Starter App - GitHub Repository. Oregon State University. https://github.com/osu-cs340-ecampus/flask-starter-app. [accessed June 3, 2025]  
