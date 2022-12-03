To run my program, first run the csv_to_sqlite.py program to set up the database with the information from the csv files.
The run the app.py file with  "flask --app app run"
You will find the login information so you can login in the original_info.csv file so that you can login to an account
with permissions to access different things. 

An owner can access everything, which is order from manufacturer, enter time, schedule repair, add user, and charge customer.
Employees can only access enter time, schedule repair, and charge customer, while customers can only access schedule repair. 
User is the default access level that new users get added with. User is not able to access anything, it is just
a record keeping thing. 

After the username and password have been entered, the user can access the different options. The most important and only
one actually implemented is the add user funciton. The user can leave the password field blank to have a password generated
for them. If they chose an already taken username, don't put a username, or don't choose a password that fits requirements, 
then the site will reprompt them to enter the information again. Once the user has been added, they will be directed to a page
that tells the user their password and username (like if they generate a password they would need to know what it was).
The add user function will also sanitize input and remove problematic characteristics aka "'%. 

So login with my username and password:
anja
IBr]q)9I#2

and then make your own user and login with that!

* I parameterized my queries when inserting into the database using the question mark method shown in the example
* I sanitized out common problem special characters that would allow SQL injection from input boxes. 
* protect from XXS: no loading of remote scripts, so I don't need to protect them, cannot make an SRI hash for my files
hosted on flask
* my generate password function does not include characters that I filter out later
* I have handled my exceptions to make sure that my program won't crash if people type certain things in the text boxes
or nothing and crash the program. I also drop the table if it already exists with loading the csv into a SQLite database. 



sources:
1) https://www.geeksforgeeks.org/how-to-hide-password-in-html/
2) https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread
3) https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/


