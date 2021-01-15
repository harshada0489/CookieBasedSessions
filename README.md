# CookieBasedSessions
Name: Harshada Prabhakar Bhangale
CWID: 887414969
Email id: harshada.bhangale@csu.fullerton.edu
Project Name::: Project 3- Server-Side Sessions
PROJECT IMPLEMENTATION
Cookie-based sessions
POINT 1
When USE_SESSION_STORE ​ in ​ counter.cfg​ is set to ​ False​ , Flask uses the default ​ session
implementation, storing the session variable ​ count​ in a signed cookie on the client side.
POINT 2
When the app is started and tries to load the page in two different browsers (e.g. Firefox and Chrome).
Refreshing the page a few times in each browser,noticed that they maintain separate counts. Screenshots of
a few different count values.
1. Run following commands in command prompt (cmd) when we are in counter project:
$ foreman start
Screenshots of Google chrome and Mozilla Firefox maintaining different counts.
1.
Chrome screenshot 1:2.
3.
Chrome screenshot 2:
FireFox screenshot 1:
4. FireFox screenshot 2POINT 3
When browser’s ​ developer​ ​ tools​ to examine the ​ Set-Cookie:​ response header, and noticed that it changes
each time the page is refreshed. Below are a few screenshots showing the change.
1.
Chrome screenshot 1:2.
Chrome screenshot 2 :Key-value store service
The file ​ kv.py​ implements a simple ​ key-value store​ service accessible via HTTP. The service exposes the following
methods:
POST /​ - sets a new value for a key
GET /<key>​ - retrieves a value of a key
DELETE /<key>​ - removes a key
GET /?prefix=PREFIX​ - returns a list of all keys matching PREFIX
POINT 4
Experimenting with these methods in ​ kv.py​ for the ​ set_key()​ , ​ get_key()​ , ​ delete_key()​ , and ​ match()
methods include example API calls using HTTPie.
Run below commands:
$ FLASK_APP=kv flask run
$ export DB_URL=localhost:5000
1. Experiment with POST method for set_key()
$ http localhost:5000 foo=bar2. Experiment with GET method for get_key()
$ http localhost:5000/foo
3. Experiment with GET method matching prefix for match()
$ http localhost:5000?prefix=f
4. Experiment with DELETE method for delete_key()
$ http DELETE localhost:5000/fooPOINT 5
Using Requests to write a Python script ​ dump.py​ to connect to the ​ kv.py​ service and display all of its keys
and values.
$ http localhost:5000 twitter=https://twitter.com/ProfAvery
$ http localhost:5000 github=https://github.com/ProfAvery
$ http localhost:5000 cpsc449=​ https://sites.google.com/view/cpsc4​ 49
Screenshot for the command run below:
So when we run the below command:
$ python3 ./dump.py ​ http://localhost:5000Server-side sessions
POINT 6
Modify ​ counter.cfg​ to set ​ USE_SESSION_STORE​ to ​ True​ , then start the counter app and the
key-value store service with ​ foreman start​ . Load the counter page, and notice that the methods
of ​ KeyValueSessionStore​ have not yet been implemented. Take a screenshot showing the failure.
● Screenshot showing failure(when USE_SESSION_STORE= TRUE and
KeyValueSessionStore is not been implemented )
●POINT 7
Now override the ​ set_key()​ , ​ get_key()​ , and ​ delete_key()​ methods in ​ KeyValueSessionStore​ to use
the Requests library to store keys and values in the ​ kv.py​ service.
●
●
Screenshot for methods in ​ KeyValueSessionStore in​ sessions.py
In sessions.py a variable is set to take url from KV_URL in counter.cfg
○ kv_url = app.config['KV_URL']TESTING
POINT 8
Now after implementation of ​ KeyValueSessionStore​ we can repeat step ​ (2) ​ from ​ Cookie-based Flask
sessions ​ and see the correct session behavior in both browsers.
Screenshot for both browser behaving correctly with different counterPOINT 9
Now Repeat step ​ (3) ​ from ​ Cookie-based Flask sessions ​ and notice that the ​ Set-Cookie:​ response header
only contains a session id, and that the session id does not change when the page is refreshed and the
counter is incremented. Take screenshots showing the same session key with different counter values.
●
Screenshot (when USE_SESSION_STORE= TRUE and KeyValueSessionStore is been
implemented)
○
showing the same session key with different counter values​ .(when page is ​ refreshed​ )
On Firefox
When count=6 :
Set-Cookie: ​ session=6cea3f31-60be-422c-9ae0-a281d9cdd0d6
On Firefox
When count=12 :
Set-Cookie: ​ session=6cea3f31-60be-422c-9ae0-a281d9cdd0d6On Google Chrome​ ​ When count=5 ​ :
Set-Cookie: session=4c4a9080-3934-4360-b913-3919abaeb1e1On Google Chrome​ ​ When count=11 :
Set-Cookie: session=4c4a9080-3934-4360-b913-3919abaeb1e1
POINT 10
After clicking the ​ Reset ​ button, the ​ POST​ request clears the session cookie and new session id is
generated once refreshed.
On Firefox
When Reset button is clicked(session id gets cleared)
Set-Cookie: ​ session=On Firefox​ New session id is created after refreshing the browser
Set-Cookie: ​ session= 9dff32c5-ff3f-4b28-85d4-3ec72c28f443On Google Chrome
When Reset button is clicked(session id gets cleared)
Set-Cookie: ​ session=
On Google Chrome
New session id is created after refreshing the browser
Set-Cookie: ​ session= 5c8e37df-0200-432b-b362-30c130994257POINT 11
Use your ​ dump.py​ script to list the active sessions in the key-value store.​ dump.py​ script to list the active sessions
in the key-value store for 2 different browsers:
Run the below command:
$ FLASK_APP=kv flask run
$ python3 ./dump.py ​ http://localhost:5000
