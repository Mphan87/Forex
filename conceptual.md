### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?


<!-- answer -->
-Python is a better-designed language that makes it easy to maintain, whereas JavaScript is poor.
-Python is not good for mobile development, whereas Java-Script is good.
-Python is slow to run compared to JavaScript.
-Python provides a huge standard library, whereas JavaScript has a limited standard library.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

<!-- answer -->
use .get() and pass in a default value 
-get('c', doesn't exist)


- What is a unit test?

Test one "unit" of functionality or method at a time. 


- What is an integration test?


This test if components work together

“Does this URL path map to a route function?”
“Does this route return the right HTML?”
“Does this route return the correct status code?”
“After a POST to this route, are we redirected?”
“After this route, does the session contain expected info?”

- What is the role of web application framework, like Flask?


provides useful tools and featueres that make creating web applications easier


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?



The key difference between query parameters and route parameters is that route parameters are essential to determining route, 
whereas query parameters are optional. Query Parameter is often used with a form.


- How do you collect data from a URL placeholder parameter using Flask?

<!-- This is an example of placeholder parameter using flask  -->
@app.route('/user/<username>')
def show_user_profile(username):
    """Show user profile for user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"


- How do you collect data from the query string using Flask?


<!-- This is an example query string using Flask  -->

<!-- This is usually used with forms -->

@app.route("/search")
def search():
    <!-- """Handle GET requests like /search?term=fun""" -->

    term = request.args["term"]
    return f"<h1>Searching for {term}</h1>


- How do you collect data from the body of the request using Flask?

Use request.form to get data when submitting a form with the POST method. 
Use request.args to get data passed in the query string of the URL, like when submitting a form with the GET method.


- What is a cookie and what kinds of things are they commonly used for?


Cookies are name/string-value pair stored by the client (browser).
The server tells client to store these.
The client sends cookies to the server with each request.

cookies are most commonly used to track website activity. When you visit some sites, the server 
gives you a cookie that acts as your identification card. Upon each return visit to that site, 
your browser passes that cookie back to the server



- What is the session object in Flask?


Sessions
-Flask sessions are a “magic dictionary”
-Contain info for the current browser
-Preserve type (lists stay lists, etc)
-Are “signed”, so users can’t modify data


- What does Flask's `jsonify()` do?


jsonify() is a helper method provided by Flask to properly return JSON data.

