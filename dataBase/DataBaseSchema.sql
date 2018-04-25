/*Creating (users)*/
create table users(
    userId serial primary key ,
    FirstName varchar(15),
    LastName varchar(15),
    username varchar(15),
    userPassword char(8),
    phoneNumber char(12),
    email varchar(25)
);

/*Self reference*/
create table contactList(
    ownerId integer references users(userId),
    contactId integer references users(userId),
    primary key(ownerId,contactId) 
);

/*Groups*/
create table groups(
    groupId serial PRIMARY KEY ,
    groupName varchar(25),
    ownerId integer references users(userId) --id del Owner
);

/*Messages*/
create table messages(
    msgId serial primary key ,
    content varchar(250),
    userId integer references users(userId),
    groupId integer references groups(groupId),
    postDate date,
    postTime time
);

/*reply*/
create table replies(
    repliedToId integer references messages(msgId),
    msgId integer references  messages(msgId),
    primary key( repliedToId, msgId)
);

/*Reactions*/
create table likes(
    likeId serial primary key ,
    userId integer references users(userId),
    msgId integer references messages(msgId)
);

create table dislikes(
    dislikeId serial primary key ,
    userId integer references users(userId),
    msgId integer references messages(msgId)
);

/*user-group relation*/
create table participants(
    userId integer references users(userId),
    groupId integer references groups(groupId),
    primary key (userId,groupId)
);