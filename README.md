# QuePasApp
Social network application

With this application users will be able to chat with each other through message posts in group chats. Also, users will be able to add other users to their contact lists for future reference when creating a group chat. Reactions for chat messages are possible (like and dislike) and possibly the user could post a message with an image or video. 

## ER Diagram

Our ER Diagram consists of 3 Main Entitities: Users, Groups and Messages. Related to these you also have the Reactions entity and various other relations between the entities such as: Participant, Creates, Posts, Read by, Makes, Contains, Has, Reply.

![alt text](https://i.imgur.com/fK9Ob1o.jpg "QuePasApp - ER Diagram")

### Users **Participant** Groups
This entity will have a participant table because many users can belong to many groups. The participant relationship will be mapped using the User's id and the Group's ids to create the table's primary key. 

### Users **Owner** Groups
A owner relationship with Groups is defined because one user will be able to create many groups. The owner relationship will not be mapped because it is a one to many relationship with total participation. The Groups entity will contain an attribute that will be a foreign key of the chat owners's id.

### Users **Author** Messages
An author relationship will be held with the Messages entity to be able to keep track of who has posted what message. Mapping Author is not necessary due to it being a one to many relationship with total participation. Messages will contain an attribute that will be a foreign key of the message authors id.

### Users **Responder** Reactions
A responder relationship will be held between Users and Reactions to be able to keep track of what reaction was done by which user to what meessage. This table will contain a serial primary key and references to the author's id and to the message's id.

### Groups **Contained** Messages
A contained relationship was defined between Groups and Messages because every group will contain a list of messages. This relationship will not be mapped because of it being a one to many relationship with total participation. Messages will contain a foreign key that will reference the group where the message is contained.

### Messages **Has** Reaction
Knowing that messages will have reactions we defined a relationship between these. As previosly mentioned in other relationship, this one will not be mapped either because of it being a one to many relationship with total participation. Reaction will contain the message id of the message it belongs to.

### Messages **Reply** Messages
A reply relationship is held with Messages itself due to the fact that a reply is also a message. This relationship will be mapped with a reply id as primary key and the id of the message replied as one of its attributes.

## API Routing

Designing a mockup of what the API implementation could be was important for the development of the backend. Using swaggerhub we were able to prepare the design of the API. [View in this link](https://app.swaggerhub.com/apis/Ykram12/QuePasApp/1.0.0#/)

## Story Map

A projection of the web-applications development was done. Although due to the way phases are delivered we may not follow this story map strictly. 

![alt text](https://i.imgur.com/TpUXHln.jpg "QuePasApp - Story Map")

