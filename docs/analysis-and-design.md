**NAME: Rhys Quilter: - K00241356**

# Name of project 

The name of my project is: Perfect Parking

# Description of business problem being solved/purpose of system:

The purpose of perfect parking is to try and solve the widespread
problem of traffic congestion and lack of parking especially in Limerick
City. Parking is one of the main issues that causes traffic congestion
especially in cities, people are selfish when they drive and begin to
rush other road users that might be new in the city and looking for
parking, when they are rushed and put under pressure, they can end up
parking illegally on the side of the road which can cause traffic to be
stopped. With my application perfect parking I'm hoping to ease the
stress and anxiety that road users face in finding appropriate parking
which gives them a price range that they might be looking for and a
location straight to the parking lot while also knowing if there is
parking available, this will eliminate traffic congestion, the waste of
petrol and diesel from driving around looking for parking and also
people's time.

# Numbered/Ordered List -- Detailed Specification 

-   **Type** Map API

Menu

Drilldown

Map API

-   **Location** Home page

> Login page
>
> Navigation bar
>
> Select parking
>
> View parking

1.  **User Functions**

```{=html}
<!-- -->
```
1.  Register

> **Type:** menu form item
>
> **Location**: Home page (not logged in/registered users)

**Action**: once a Guest user opens the application they will be greeted
with a log-in page, there will also be a **button** underneath the form
that states, "don't have a log in register now". If the guest attempts
to login and doesn't have a log-in, they will be prompted with an error
message stating them to register. Once the guest selects the
registration button, they will be brought to the register form, here
they will be asked to enter e-mail, password, confirm password. Once
registered their details will be sent and saved to the User Details
table in the DB. They will then be redirected to the Log-in page.

2.  Login

**Type:** menu form item

**Location**: Login page (not logged in users)

**Action**: the user will provide an e-mail and password to login. These
details will be verified by the DB by a lookup. If the details entered
is correct the user will be logged in and be brought to the select
parking/parking lookup page. If their information is incorrect, they
will be prompted to renter e-mail and password.

3.  Logout:

**Type:** menu item

**Location**: Navigation bar item (for logged in users)

**Action:** when selected in the navigation bar of a logged in user the
user will be logged out and sent back to the login page.

4.  Select Parking

**Type**: Menu item

**Location:** Select parking location (Accessed from navigation bar)

**Action:** once a user is logged in they can access the **select
parking** page, from here users can select parking in the city that they
would like to view. There will be a list of all the different parking
lots in the city.

5.  View Parking

**Type:** Parking Drilldown

**Location:** View parking page (Accessed through select parking)

**Action** this page will show all the information about the selected
parking, it will show the parking price per hour, and per day. There
will also be a map that can be viewed by the user and shows the location
of the parking.

6.  Get direction.

**Type:** Map API

**Location:** View parking page (Accessed from the map)

**Action:** when the user is viewing the map, if the user clicks the
map, it will show information such as the address and the name of the
parking, it will also prompt the user to get the directions from their
location to the parking lot, this is done through google maps.

1.  View prices

**Type:** button

**Location:** View parking page

**Action:** when the user is viewing the parking there will be a button
stating view prices, when the user presses this button, it will show the
parking rates for that parking lot.

**Administration functions**

1.  Login:

**Type:** menu form item

**Location**: Login page (not logged in users)

**Action**: the user will provide an e-mail and password to login. These
details will be verified by the DB by a lookup. If the details entered
is correct the user will be logged in and be brought to the select
parking/parking lookup page. If their information is incorrect, they
will be prompted to renter e-mail and password.

1.  Logout:

**Type:** menu item

**Location**: Navigation bar item (for logged in users)

**Action:** when selected in the navigation bar of a logged in user the
user will be logged out and sent back to the login page.

2.  View Registered Users:

**Type**: Menu Item

**Location**: view all users

**Action**: When selected this menu item will present a table of all
user's IDs and usernames

along with status (active).

3.  Edit Price:

**Type:** Button

**Location** Edit parking.

**Action:** when the admin presses the button it will allow him to
update the price of parking per hour/day/week, when this is done the
users will be greeted with a new price once it has been successfully
updated.

4.  view User

**Type:** Menu item/button

**Location:** view user

**Action:** when the admin is viewing all users, they can then select a
user which they wish the view the details for. When they press on the
user it will view that one users' details.

5.  Delete user.

**Type:** button

**Location:** view user

**Action:** when the admin is viewing the user details, they will also
have a button which they can use to delete user, this might have to be
done in certain circumstances such as user has violated the terms and
conditions, when the admin presses the delete user button it will delete
all the user details from the database.

# Database design

![Diagram Description automatically
generated](media/image1.png){width="5.395833333333333in"
height="5.15625in"}

This database design consists of three tables: \"User\",
\"ParkingLotMonitor\", and \"ParkingLot\".

-   The \"User\" table has three columns: \"Id\" (Primary Key),
    \"Username\", and \"Password\".

-   The \"ParkingLotMonitor\" table has six columns: \"Id\" (Primary
    Key), \"ParkingLotId\" (Foreign Key),
    \"ProbabilityParkingAvailable\", \"LastUpdated\", \"Status\", and
    \"DataTime\".

-   The \"ParkingLot\" table has seven columns: \"Id\" (Primary Key),
    \"Name\", \"Address\", \"Image\", \"Hours\", \"IsPaidParking\",
    \"Latitude\", and \"Longitude\".

the diagrams shows a relationship between the \"ParkingLotMonitor\" and
\"ParkingLot\" tables through the use of the \"has\" symbol. The
\"ParkingLotId\" column in the \"ParkingLotMonitor\" table acts as a
connection point, serving as a foreign key to link the two tables.

## User Parking Sequence diagram

![](media/image2.png){width="6.268055555555556in" height="2.0875in"}

this is the sequence diagram of the process where a user is searching
for parking near their location using the application. The user asks the
app if there is parking available near their GPS location on Henry
Street.

The app then queries multiple parking lot monitors,
HenryStParkingLotMonitor, LowerHartstongeParkingLotMonitor,
MallowStreetPart1ParkingLotMonitor, and
MallowStreetPart2ParkingLotMonitor, to check if parking is available in
each lot.

The HenryStParkingLotMonitor responds that parking is 97% available, the
LowerHartstongeParkingLotMonitor responds 87%,
MallowStreetPart1ParkingLotMonitor 65%, and
MallowStreetPart2ParkingLotMonitor 45%.

Finally, the application then sends a response to the user indicating
that there are 3 parking lots available near their location, with the
names HenrySt, LowerHartstonge, and MallowStreetPart1.

# Prototype design for the pages

When I was thinking about how I would structure and layout my Perfect
Parking web application I decided to draw up some diagrams to give me a
better insight into what the pages would look like after the diagrams
were hand drawn I was then able to make some HTML prototype pages so I
can get a better vision into what they would look like in a web browser.

## Drawn prototypes.

### Login/Parking page

![](media/image3.emf){width="3.563138670166229in" height="5.775in"}

Above is my Login page, this page is where the users will be brought to
when they first open the application. Once the users are logged in they
will be brought to the parking page this is where they will see a list
of all the parking spaces.

### View parking page

![](media/image4.emf){width="3.433333333333333in"
height="5.52930227471566in"}

This is the view parking page, this page is opened when the user either
searches or selects a parking lot from the parking page, here it will
show information such as pictures of the car park, a map showing a
pinned location of where the carpark is, this also allows you to get the
direction to the parking lot by using google maps, you can also add this
car park to your favourites and pay for your parking in advance if the
user would like.

### Book Parking/Payment page

![](media/image5.emf){width="3.2256944444444446in"
height="5.082889326334208in"}

Once the user selects book parking, they will be brought to the booking
page, here they can select the rate that they would like to park such as
per hour or per day. Once the confirm parking button is pressed they
will be brought to the payment page where they can input there card
information to finish off the payment.

### View users/view user (Admin)

![](media/image6.emf){width="3.375in" height="5.3513867016622925in"}

These two web application pages are for the admin, once the admin logs
in they have the ability to view users and select a user, once the
select a user has been selected the admin can do things such as suspend
a user and edit user information.

## HTML Prototypes

### Login Page

![](media/image7.png){width="6.268055555555556in"
height="2.717361111111111in"}

### Registration Page

![](media/image8.png){width="6.268055555555556in"
height="3.8756944444444446in"}
