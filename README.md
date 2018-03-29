# QuePasApp
Social network application

With this application users will be able to chat with each other through message posts in group chats. Also, users will be able to add other users to their contact lists for future reference when creating a group chat. Reactions for chat messages are possible (like and dislike) and possibly the user could post a message with an image or video. The main page of the web application will contain a dashboard where the user can see the trending topics (via #), and the total number of messages per day, replies per day, and likes and dislikes per day. Lastly, it will present the most active users depending on their group chat activity (message posting, reactions, replies)

## Entity Relationship Diagram

Our ER Diagram consists of 4 Main Entitities: Users, Groups and Messages, Reaction. These have various relationships between each other such as: Participant, Creates, Posts, Read by, Makes, Contains, Has, Reply.

![alt text](https://i.imgur.com/I9aHxxQ.jpg "QuePasApp - ER Diagram")

## Entities Description

### Users

A user is a person with the necessary credentials to use QuePasApp

1. IdUser : Unique identifier for users
2. uName: Name of the user
   1. uFirstName - First Name of user 
   2. uLastName - Last name of the user
3. Email: the email address of the user, used to add the user to a group and as a login credential
4. Phone: the telephone number of the user, used to add the user to a group
5. Username: a unique string that identifies the user, used and as a login credential
6. password: a string that combined with the email or the username, serves a the users credentials

### Groups

A group is a chat where multiple members can send and read messages, as well as reply or react to the messages

1. IdGroup - Unique identifier for the group
2. gName - A string that represents the title of the group

### Message

A message is a string that an user sends to a group

1. IdMessage
2. IdUser
3. content

### Reactions

A reaction is either a like or a dislike, that is attached to a message

1. IdReaction - a unique identifier for the Reaction
2. IdUser - creator of the Message
3. IdMessage - the message where the reaction is attached

### Like

A Like is a reaction that is attached to a message, that represents that the user agrees or likes that message

1. IdLike -  a unique identifier for the Like

*Contains every attribute of a Reaction* 

### Dislike

A Dislike is a reaction that is attached to a message, that represents that the user does not likes that message or disagrees with it

1. IdDislike - a unique identifier for the dislike

*Contains every attribute of a Reaction* 

## Entity Relationships

### Users - Participant - Groups

This entity will have a participant table because many users can belong to many groups. The participant relationship will be mapped using the User's id and the Group's ids to create the table's primary key. 

### Users - Creates - Groups
A creates relationship with Groups is defined because one user will be able to create many groups. The creates relationship will not be mapped because it is a one to many relationship with total participation. The Groups entity will contain an attribute that will be a foreign key of the chat creator's id (owner).

### Users - Posts - Messages
A posts relationship will be held with the Messages entity to be able to keep track of who has posted what message. Mapping Posts is not necessary due to it being a one to many relationship with total participation. Messages will contain an attribute that will be a foreign key of the message writers id.

### Users - Read by - Messages
A read by relationship will be held with the Messages entity to be able to keep track of who has read what message and when. In the case of the Read By relationship we need to map it and we utilize the readers id, the messages id, and the time and date it was read. Using the readers id and the messages id we create a primary key for this relation.

### Users - Makes - Reactions
A makes relationship will be held between Users and Reactions to be able to keep track of what reaction  was done by which user to what meessage. This table will contain a serial primary key and references to the writers id and to the messages id.

### Groups - Contains - Messages
A contains relationship was defined between Groups and Messages because every group will contain a list of messages. This relationship will not be mapped because of it being a one to many relationship with total participation. Messages will contain a foreign key that will reference the group where the message is contained.

### Messages - Has - Reaction
Knowing that messages will have reactions we defined a relationship between these. As previosly mentioned in other relationship, this one will not be mapped either because of it being a one to many relationship with total participation. Reaction will contain the message id of the message it belongs to.

## API Routing

Designing a mockup of what the API implementation could be was important for the development of the backend. Using swaggerhub we were able to prepare the design of the API. [View in this link](https://app.swaggerhub.com/apis/Ykram12/QuePasApp/1.0.0#/)

## Story Map

A projection of the web-applications development was done. Although due to the way phases are delivered we may not follow this story map strictly. 

![alt text](https://i.imgur.com/TpUXHln.jpg "QuePasApp - Story Map")

