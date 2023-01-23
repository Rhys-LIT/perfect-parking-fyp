![Technological University of the Shannon (TUS)
Opens](media/image1.png){width="6.0in" height="2.75625in"}

Perfect Parking A map API parking application: A Literature Review from
a Technological Perspective

Rhys Quilter: K00241356 \| Final Year Project \| 14/10/2022

# Table of Contents {#table-of-contents .TOC-Heading .unnumbered}

[1.0 Abstract [2](#abstract)](#abstract)

[2.0 Introduction [2](#introduction)](#introduction)

[3.0 Application Programming Interface (Api)
[4](#application-programming-interface-api)](#application-programming-interface-api)

[What Is An API? [4](#what-is-an-api)](#what-is-an-api)

[The History Of API's [4](#the-history-of-apis)](#the-history-of-apis)

[What Is A Mapping API.
[5](#what-is-a-mapping-api.)](#what-is-a-mapping-api.)

[What Is Directions API
[5](#what-is-directions-api)](#what-is-directions-api)

[How Can I Use Directions API
[5](#how-can-i-use-directions-api)](#how-can-i-use-directions-api)

[4.0 Big Data And Realtime Data
[6](#big-data-and-realtime-data)](#big-data-and-realtime-data)

[What Is Big Data [6](#what-is-big-data)](#what-is-big-data)

[Why Is Big Data Important
[6](#why-is-big-data-important)](#why-is-big-data-important)

[What Is Real Time Data
[7](#what-is-real-time-data)](#what-is-real-time-data)

[What Is The Importance Of Real Time Data
[7](#what-is-the-importance-of-real-time-data)](#what-is-the-importance-of-real-time-data)

[The Problems I Face With Gathering Data
[8](#the-problems-i-face-with-gathering-data)](#the-problems-i-face-with-gathering-data)

[5.0 Web Service Frameworks
[8](#web-service-frameworks)](#web-service-frameworks)

[Java Spring Framework
[9](#java-spring-framework)](#java-spring-framework)

[Why Use Java Spring. [9](#why-use-java-spring.)](#why-use-java-spring.)

[Advantages And Disadvantages Of Spring Framework
[10](#advantages-and-disadvantages-of-spring-framework)](#advantages-and-disadvantages-of-spring-framework)

[Conclusion [11](#conclusion)](#conclusion)

[C# Asp.Net [12](#c-asp.net)](#c-asp.net)

[Why Use Asp.Net [12](#why-use-asp.net)](#why-use-asp.net)

[Main Advantages Of Asp.Net
[13](#main-advantages-of-asp.net)](#main-advantages-of-asp.net)

[Conclusion [13](#conclusion-1)](#conclusion-1)

[6.0 Problem Statement [14](#problem-statement)](#problem-statement)

[7.0 Review Description [15](#review-description)](#review-description)

[8.0 Conclusion [17](#conclusion-2)](#conclusion-2)

[References [18](#_Toc118669900)](#_Toc118669900)

# Abstract 

This project is a Parking application for academic purpose. The aim of
my project is to create a parking system that will replace the outdated
systems and to help stop the widespread problem that is parking in our
cities. The applications that are used in Limerick City are simply not
good enough. So, my goal in this project is to improve the effectiveness
of finding parking spaces and to also relieve the stress of the users
looking for parking by implementing new and innovative features. I will
do this by using an MVC structure and by implementing methods such as
map API's that will show the user exactly where the parking is and by
providing locations for them to follow straight to the location. By
doing this I feel like it will also help with traffic congestion in the
city as people won't need to keep driving around the block to find a
convenient parking space.

# Introduction 

Due to an increase in in the number of cars being used in limerick city
and other cities in Ireland, finding a solution to car parks has now
become vital. The old-fashioned way of parking was that everyone would
just leave their cars parked in the streets until they were needed
again, this however caused major traffic congestions in towns and
cities. Shop owners also got hugely impacted as there wouldn't be enough
room for staff to park no mind the customers looking to go into their
shops which was damaging for their business, it is undeniable that car
parks are a very important factor in society, by having parking spaces
it reduced illegal parking which would have increased congestions on the
road and increasing travel time.

It is fair to say that parking back in the 1980s -- 1990s wasn't such a
big issue as there wasn't very many cars on the road as people couldn't
afford to have a car unless they were wealthy, nowadays however it is
very hard to find available parking spaces in places such as cities, and
of course universities especially during rush hour. Since limerick City
is a big city for students to come and study in with there being over
16,000 students attending university of limerick and just under 2000
students in TUS and Mary I, this brings so much more motor vehicles into
limerick city which is a city already struggling with car parking.
(UL.ie, 2022)

My goal is to try and reduce this issue by building a new innovative
parking app and to try to help motorists stop stressing about this
parking crisis.

# Application Programming Interface (API)

## What is an API? {#what-is-an-api .unnumbered}

An API are a mechanism that allow two software components to communicate
with each other using different definitions and protocols. An example of
an API would be the bureaus software system which contains the daily
weather data, the weather app on your phone would talk to this system
using APIs and shows you the daily weather updates on your phone. (What
is an API, 2022).

## The History of APIs  {#the-history-of-apis .unnumbered}

Between the years of 2000 and 2002, online commerce and information
sharing was just starting to become huge. Companies began to see an
opportunity to expand their impact by making their information more
accessible and shareable than ever before, these companies being Amazon,
eBay, and Salesforce.

In the year 2000 Salesforce finalized and released their first modern
API. Within this time eBay and alongside them Amazon also developed
their own API which allowed developers access. What this meant was that
for the first-time data-sharing was openly accessible for a wide range
of customizable uses.

As the years went on many companies started to explore APIs, as this
went on the APIs began to grow and software companies realized that APIs
were a convenient way to share resources with their developers and to
expand their footprint, spark ideas and to accelerate their development.

One of these software companies was Google, with their Google Maps.
Google launched its API in 2006 they done this to share the massive
amounts of geographical data that they have collected. This being the
Google Maps that we know today, being Google Street View, and the Map
application on our mobile phone which we use for navigation. (Hawkins,
2020)

## What is a mapping API. {#what-is-a-mapping-api. .unnumbered}

A map API also known as mapping API provides location intelligence for
software developers that are developing location-based products or
services. It is the base building blocks for location-aware
infographics.

A typical Map API have features including geocoding, reverse geocoding,
geolocation, directions, and navigation. There are other features such
as different types of maps such as terrain or satellite.

Map APIs are a great way for developers to retrieve location data such
as proximity details about places, travelling distances and the time it
will take between different endpoints. We saw map APIs being used in the
pandemic to identify areas that had big spikes in covid cases which
would be marked in red on the Covid app. (What is a Mapping API, n.d.)

## What is Directions API {#what-is-directions-api .unnumbered}

Directions API is a geolocation service that software developers can use
to plot routes between different places on a map. The Directions API
make it easier for developers to create interactive location-based
applications. (Google Maps Platform, n.d.)

## How can I use Directions API {#how-can-i-use-directions-api .unnumbered}

Directions API can play a big part in my application, the reason that I
am saying this is because if road users are new or visiting the city and
they would need to figure out how to get to this parking lot. Using
google Directions API would be a great way of doing this, when the user
finds a parking lot, they would like to use they would simply press the
parking icon and they would get a prompt to get the directions to the
parking and when clicking this it would open up there google maps and
show them the fastest way of getting to their location and the time it
will take. This will eliminate the road users worry from getting from
their location to the parking lot.

# Big Data and Realtime Data

## What is big data  {#what-is-big-data .unnumbered}

Big data is a combination of structured, semi structured, and
unstructured data that is collected by organizations, this data can be
mined for information to be used in many projects such as machine
learning, predictive modeling, and other analytics applications. Big
data is often characterized by the three Vs.

-   The large **Volume** of data in many environments.

-   The wide **Variety** of data types frequently stored in big data
    systems

-   The **velocity** at which much of the data is generated, collected,
    and processed

These characteristics were first identified in 2001 by Doug Laney, they
were then further popularized in 2005 by an analyst at a consulting firm
called Meta Group.

Big data doesn't equate to any specific amount of data, big data
deployments often involve terabytes, petabytes or even in some cases
exabytes of data that is created and collected over time. (Botelho,
n.d.).

## Why is big data important {#why-is-big-data-important .unnumbered}

Big data importance lies in the fact of how a company utilizes the
gathered data. Every company uses its gathered data in its own way, the
more a company can gather its data the more the company can grow.

Big data provides valuable insights into customers that companies can
use to refine their marketing, advertising, and promotions by doing this
they can increase customer engagement and conversion rates. (TechVidvan,
n.d.)

Big data is huge in the medical industry, medical researchers can
identify disease signs and risk factors, this can help the doctors
diagnose illnesses and medical conditions in patients. A combination of
data from electronic health records and the web can give healthcare
organizations and government agencies up to date information on
infectious diseases threats or outbreaks, we have seen this in the past
with the pandemic and how the HSE in Ireland were able to monitor the
amount of covid -- 19 infections per county, and how they were able to
create the Covid App with this data. (Botelho, n.d.)

## What is Real Time data {#what-is-real-time-data .unnumbered}

Real time data us data that is available as soon as its created and
acquired. Rather than being stored, data us forwarded to users as soon
as its collected and is immediately available without and delay, this is
crucial for supporting live, in the moment decision making. This real
time data is a big part of our everyday lives, it powers everything from
bank transactions and GPS this was also seen in the many Covid-19 maps
that emerged during the pandemic. (splunk.com, 2021)

We see a lot more of real time data then we think, Google collects
endless amounts of real time data and the way they do it is actually
very smart, they use a device that 6.6 billion people in the world have
and that being smart phones. (bankmycell.com, 2022) if people have smart
phones, then nearly everyone has the google map application and GPS in
their phones. When people sign into google on their phone Google starts
creating real time data through the GPS and other apps, for example,
when your using Google Maps on your phone it shows loads of data such as
the estimated time of arrival to your destination and also if there is
any traffic on your route, Google knows this by using real time data
from other people that are taking that route and that might be stuck in
traffic and this is all taken from the GPS location on smart phones.
(Ashish, 2022)

## What is the importance of Real Time data {#what-is-the-importance-of-real-time-data .unnumbered}

Real-Time data is a necessity to stay relevant for today's business and
it needs to be delivered by sophisticated electronic communications
tools such as digital signage and data dashboards, to remain appealing
to today's tech savvy workforce from call centers to retailers.
(Barnett, 2017)

Real time data is important in many parking applications, these
applications use real-time data to show users if there is parking spaces
in the carpark which they have selected, this data can be gathered by
the carpark having a barrier that counts the amount of cars that go in
or the amount of cars that exit, some carparks also have sensors on each
of the parking spaces this allows users to see what actual spaces are
available, this is the most ideal as it allows people that need disabled
parking to see if that type of parking space is available.

## The problems I face with gathering data {#the-problems-i-face-with-gathering-data .unnumbered}

When tech companies are building applications such as parking
applications, they are given a budget by the parking company, and this
enables them to put in these parking sensors or put in barriers to
gather the real-time data for the users. This is where I face a big
problem with gathering this data, since TUS carpark and other car parks
in the city is monitored by another parking company called APCOA I am
very limited to what data I can gather. Since I'm building this
application on a very small scale gathering real-time data is going to
be nearly impossible. One solution that I did think of would be to build
my own parking space sensor using a raspberry pi and putting this down
in a parking space in either my college or in the city, with doing this
brings even more problems, these problems being:

-   I would have to get permission from APCAO to allow me to place this
    sensor on their parking premises.

-   If I do get permission since the sensor would only be built on a
    raspberry pi it could easily get damaged or stolen.

-   I would only be able to build one sensor for one single parking spot
    which wouldn't gather much real-time data for the users.

# Web Service Frameworks

When I decided to create a web application, I started to do some
research on different web Service frameworks to decide what framework I
feel would work the best for my application, the frameworks that I
carried out research on were:

-   Java Spring

-   C# asp.NET

## Java Spring Framework {#java-spring-framework .unnumbered}

The Spring framework is a great application framework and inversion of
control container for the Java platform. It is a great example of
high-quality software. Spring provides everything required beyond the
java programming language for creating enterprise applications for a
wide range of scenarios and architectures. It has been developed for
over 17 years (George, 2021).

###  Why use Java Spring. {#why-use-java-spring. .unnumbered}

Spring framework helps develop various types of applications using the
Java platforms. It provides an extensive level of infrastructure
support. Spring also provides the Plain Old Java Objects also known as
POJOs mechanisms which developers can easily create the Java SE
programming model with the full and partial JAVA EE.

Spring Strives to facilitate the complex and unmanageable enterprise
Java application development revolution by offering a framework that
incorporates technologies, such as:

-   Aspect-oriented Programming

-   Dependency Injection

-   Plain Old Java Object

The Spring framework also provides plenty of features. It helps the
developers to perform the following functions.

-   Create a Java method that runs in a database transaction with no
    help from transaction APIs.

-   Create a local Java method that defines a remote procedure with no
    help from remote APIs.

-   Create a local Java method for a management operation with no help
    from JMX APIs.

-   Create a local Java method for a message handler with no help from
    LMS APIs

> (Simplilearn, 2022)

### Advantages and Disadvantages of Spring Framework {#advantages-and-disadvantages-of-spring-framework .unnumbered}

Java spring consists of multiple tools to get numerous web app
development benefits. When using spring it allows us to not write
lengthy code. It is beneficial because it saves developers time and
energy. I will now discuss the advantages and disadvantages of the Java
Spring framework.

**Advantages**

-   **Flexibility:** it offers flexible libraries to assist developers.
    Users can choose between XML and Java-based annotations regarding
    configuration. IoC and DI features are also present to provide
    extensive functionality and features.

-   **Consistent configuration:** It helps in providing a consistent way
    of configuration. It offers a separate configuration for the
    facilitation of developers.

-   **Secure:** the framework offers frequent updates to make our data
    an apps more secure.

-   **Simpler testing:** Developers can perform testing with ease due to
    this framework. It is possible die to the usage of dependency
    injection.

**Disadvantages**

-   **Complexity:** it is complex to work with Spring. Developers must
    have more relevant skills and expertise to use this framework.

-   **Hard to learn:** if you have little or no experience regarding
    development, it will be difficult to learn Spring. This is due to
    the incorporation of the latest programming techniques in this
    framework.

-   **Uses XML:** lots of XML is needed while developing a Spring app.
    It can also be problematic for developers.

-   **Parallel mechanism:** while using Spring developers can get
    multiple options. It can be very helpful in some cases, but it can
    also be confusing. Developers can run into problems when it comes to
    selecting the right mechanism and can result in wrong decision
    making. If these mistakes are made it can cause delays in the
    development of the applications. (Bashir, n.d.).

### Conclusion {#conclusion .unnumbered}

From the research that I undertook on the Java Spring Framework it
stands as a strong contender for a framework that I will possibly use, I
also have experience in this framework which will also be a huge help
when it comes to the design stage of the project.

## C# ASP.net {#c-asp.net .unnumbered}

ASP.NET is an open-sourced web framework for building web applications.
It is created by Microsoft, version 1.0 was released in 2002 to allow
developers to build dynamic web apps. Services and sites. The framework
is built to work with the standard HTTP protocol, which is the standard
protocol used across all web applications. (Tyler, 2022)

### Why use ASP.NET {#why-use-asp.net .unnumbered}

There are many reasons why developers should choose to use ASP.NET when
developing a website or application. High speed, low cos, and vast
language support are among the most significant benefits. ASP.NET is
built into the familiar Windows server environment, requiring less setup
and configuration than other web development platforms that must be
installed and configured separately. The popularity of ASP.NET makes
online resources and skilled developers easy to find.

Applications built using ASP.NET can be faster and more efficient than a
website that is built using PHP, for example ASP.NET applications are
compiled, which means the code is translated into object code, which is
then executed. This compilation process takes a small amount of time but
happens only once. After compilation, the code can be executed
repeatedly by the .NET platform very quickly.

The database type that you would like to use is an important decision
that has to be made when developing a web application, when using
ASP.NET you have a choice of different databases such as Microsoft SQL
server, MySQL, MariaDB to name a few. However MySQL and MariaDB are free
and open source but Microsoft SQL Server can require expensive software
licenses, there is a free express version which is suitable for a
majority of websites.

ASP.NET is written using OOP also known as Object Oriented Programming
languages such as C#. OOP provides a framework and patterns for code
organization and reuse. C# is a first-class programming language and
consistently ranks among the world's most in demand and most use
programming languages.

ASP.NET is developed by the world's largest software company, Microsoft.
Microsoft is heavily invested in their development platforms. Their
development community and supporting the software companies use to run
these applications. What this means is that there is no need for you to
worry about your software becoming obsolete any time soon. (Wiseley,
2018)

### Main advantages of ASP.NET {#main-advantages-of-asp.net .unnumbered}

-   The ASP.NET is a web framework is facilitated by a powerful toolkit
    and designer in the integrated development environment of visual
    studio. The Drag and Drop sever controls and auto deployment are
    only a couple of the features this versatile tool offers.

-   Lesser code encourages the application to easily manage and
    effectively maintain.

-   These applications have windows authentication which makes the
    applications more secure.

-   In ASP.NET applications, source code and HTML files are together so
    ASP.NET pages are easy to manage and write. The source code is now
    being run on the computer. This gives the website a lot od strength
    and versatility.

-   ASP.NET helps in developing robust web applications7

> (geeksforgeeks.org, 2021)

### Conclusion {#conclusion-1 .unnumbered}

From the research that I undertook for ASP.NET I learned that this
framework is very dominant over other frameworks such as the Java
Spring. I feel like ASP.NET would be a great framework for building
prototype screens for my application because of the drag and drop
feature that ASP.NET has within the Visual Studio IDE. This gives me a
lot to think about in terms of what framework I should use for
developing my application since I have researched two really good
frameworks.

# Problem Statement

**Ineffective ways of finding an available parking space which is a
waste of time, very fuel consuming and causes traffic jams.**

when road users are looking to find an available parking space they end
up wasting time and using a lot of fuel from them driving around the car
park or the block multiple times hopping to find a space, on average
people spend 17 hours per year driving around looking for parking spaces
(Quellmalz, 2021). By developing my app Perfect Parking I'm hoping to
make the parking process in college campus and in the city easy and
stress free, by doing this I'm hoping to eliminate the time and fuel
waste road users encounter while looking for parking.

**Lack of visual parking space availability.**

When road users are driving the visuals of the eye are limited, the
vision is blocked by many obstacles such as the cars frame causing blind
spots, other cars, trees and much more. With this in mind it can be
understood that the road users can find it difficult to spot an
available parking space if its in the distance or behind other cars.
This has turned into an important problem with road users and as a
result they waist time and fuel trying to spot an available space.

**Lack of knowledge of towns or cities.**

Limerick is a city where people migrate to for education or tourism, and
with this brings more road users. When people first come to Limerick
City, they have to learn the road routes and with this where the parking
is. A lot of road users that drive in a new place start to panic and get
anxious when they try and find parking. This can cause them to be in the
wrong lanes and cause traffic congestion. But with my app it will allow
users to plan their route to the parking of their choice and follow
directions on the phone to the car park. By doing this that it will keep
new road users in the city calm so they can enjoy there holiday or for
students teach them the road routes and the best places to park.

# Review Description

From doing research into parking systems, I have realized that there is
a lot of existing parking systems that use different strategies and
approaches to reach their goals and solve the problems of parking
systems.

In this section I will review a few systems that I feel are unique and
that have good strengths but that also have some weaknesses.

![Graphical user interface, application Description automatically
generated](media/image2.png){width="6.0in" height="3.036111111111111in"}

*Figure 1.0: web parking application to find parking in your area*
(APCOA, 2022)

**Brief**

APCOA is a parking application that supports Android mobile, iPhone, and
windows OS. APCOA is smart parking application, we use this company in
our TUS Moylish campus as of today. The application is very user
friendly it allows the user to see how much the parking is per hour and
as seen in figure 1.0 above shows in blue there is parking facilities
available to cater for disability parking, motor bikes and that the
location is secure and safe to park in with controlled gates and
surveillance cameras. This changes for different locations that you're
looking to park in. In this application it allows multiple ways to pay,
you can prepay by using your debit or credit card, if you're on Android
or IOS you can pay using Google Pay or Apple Pay respectfully. There are
also options to pay in cash when you arrive. APCOA claim that they can
help you find and pay for parking in seconds.

**Strengths**

From looking at figure 1.0 above we can see that the application uses a
Google Map API to equip the user with a map so they can see the exact
location of the car park that they would wish to book. With them also
showing the parking facilities in the car park this can allow users to
plan which car park they can park in depending on if they need disabled
parking or motorbike parking and so on.

**Weaknesses**

one of the weaknesses of this application is that it doesn't show the
user if there is parking available in that certain carpark, what this
means is that if a user does pre book their parking they are not
guaranteed a parking spot on their arrival. This could lead to the user
being frustrated on arrival.

**Recommendations**

The limitation mentioned above can be sorted by developing a simple
interface that will reduce the number of spaces available when somebody
pre books on the app or pays on arrival, by doing this it will limit the
number of frustrated users. Another recommendation that I will make
about this application would be that the user could get the location of
the parking lot and use their Apple or Google maps to take them to that
location.

# Conclusion

Since starting my FYP on Perfect Parking and the research that I have
undertaken I have learned how important Data and real-time data is,
without using this data the application wouldn't be as user-friendly and
would lack information that the users would find useful. Real-time data
isn't the be all and end all of my application, I must be realistic to
myself and I know its not possible to create a full-blown scale parking
application by myself and have loads of data with loads of information.
However, I can try my best by using tools such as Google APIs to supply
information for example estimated times of arrivals for user and traffic
data. When it comes to building a sensor, it is a brilliant idea but
when I weighed up the pros and cons of building the parking sensor there
was more disadvantages than advantages as described in heading 4.0
paragraph 4.4 .

In above passages I have discussed and investigated how important
parking is in road users' lives. By building the Perfect Parking
application it will make road users lives easier and stress free when it
comes to looking for parking. By developing this app, I am also hoping
that it will reduce the carbon emissions as it will prevent road users
from driving around a car park or city in the hopes of finding a parking
spot.

From investigating the issues and importance of parking and how building
an application can benefit road users who struggle to find parking, this
has allowed me to investigate the most ethical way of continuing with
the project from a technological and personal perspective.

I have also learned a lot about two different frameworks these being
Java Spring and ASP.NET, this leaves me with a very important decision
on which framework I will choose to use as they both have great valuable
aspects however, from my research there are also some negatives that
will weigh my decision.

# References {#references .unnumbered}

(n.d.). Retrieved from casrsoftware.com:
https://www.castsoftware.com/glossary/Software-Architecture-definition-examples-explanation-tools-principle

(n.d.). Retrieved from TechVidvan:
https://techvidvan.com/tutorials/why-big-data/

(2021, August 1st). Retrieved from splunk.com:
https://www.splunk.com/en_us/data-insider/what-is-real-time-data.html

(2021, April 24th). Retrieved from geeksforgeeks.org:
https://www.geeksforgeeks.org/why-we-should-use-asp-net/#:\~:text=These%20applications%20have%20windows%20authentication,lot%20of%20strength%20and%20versatility.

(2022). Retrieved from UL.ie:
https://www.ul.ie/presidents-office/university-profile/facts-and-figures

(2022). Retrieved from bankmycell.com:
https://www.bankmycell.com/blog/how-many-phones-are-in-the-world

APCOA. (2022). *APCOA Parking*. Retrieved from APCOA.ie:
https://www.apcoa.ie/location-search/Moylish,%20Limerick,%20Ireland

Ashish. (2022, july 8th). Retrieved from scienceabc.com:
https://www.scienceabc.com/innovation/how-does-google-maps-know-about-traffic-conditions.html#:\~:text=Google%20Traffic%20works%20by%20crowdsourcing,geographic%20location%20with%20the%20app.

Barnett, M. (2017, August 1st). Retrieved from fourthsource.com:
https://www.fourthsource.com/data/importance-real-time-data-five-reasons-need-22014

Bashir, F. (n.d.). Retrieved from educative.io:
https://www.educative.io/answers/what-are-java-spring-framework-advantages-and-disadvantages

Botelho, B. (n.d.). *Big Data*. Retrieved from techtarget.com:
https://www.techtarget.com/searchdatamanagement/definition/big-data

George, M. (2021, january 21st). Retrieved from DZone.com:
https://dzone.com/articles/a-case-study-on-spring-framework

*Google Maps Platform*. (n.d.). Retrieved from Directions API overview:
https://developers.google.com/maps/documentation/directions/overview#:\~:text=The%20Directions%20API%20is%20a,for%20Google%20Maps%20Web%20Services

Hawkins, M. (2020, june 23). *The History And Rise Of APIs*. Retrieved
from forbes.com:
https://www.forbes.com/sites/forbestechcouncil/2020/06/23/the-history-and-rise-of-apis/?sh=9957ddb45c28

Quellmalz, R. (2021, march 18). *6 surprising facts about parking you
probably dont know*. Retrieved from SpotParking.com:
https://www.spotparking.com.au/insights/facts-about-parking-you-probably-didnt-know

Simplilearn. (2022, Febuary 22nd). Retrieved from simplilearn.com:
https://www.simplilearn.com/tutorials/spring-boot-tutorial/what-is-spring-framework-and-its-advantages

Tyler, C. (2022, october 29th). Retrieved from guru99.com:
https://www.guru99.com/what-is-asp-dot-net.html

*What is a Mapping API*. (n.d.). Retrieved from PunNub.com:
https://www.pubnub.com/learn/glossary/what-is-a-map-api/

*What is an API*. (2022). Retrieved from aws.amazon.com:
https://aws.amazon.com/what-is/api/

Wiseley, M. (2018, november 27). Retrieved from wakefly.com:
https://www.wakefly.com/blog/what-is-asp-net-and-why-should-i-use-it/
