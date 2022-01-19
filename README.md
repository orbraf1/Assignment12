# Assignment 12
### Hey, my name is Or Braf. Those are the main things I did in this assignment:
* I created a new route called '/assignment12/restapi_users' and added it to the menu of my website. In case no user_id was provided this route returns the data of a default user (id_user = 6) from the table 'users' in JSON format.
* I also created another new route called '/assignment12/restapi_users/< int:user_id >'. This route returns a user's data in JSON format and if there is no user with such user_id - the route will return an error message in JSON format. As you can see, I used int validation for the type of user_id inside this route.
