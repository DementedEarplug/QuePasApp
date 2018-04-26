<<<<<<< HEAD
/*Creating user (member)*/
create table member(
    mId serial primary key ,
    mFirstName varchar(15),
    mLastName varchar(15),
    username varchar(15),
    uPassword char(8),
=======
/*Creating (users)*/
create table users(
    userId serial primary key ,
    FirstName varchar(15),
    LastName varchar(15),
    username varchar(15),
    userPassword char(8),
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
    phoneNumber char(12),
    email varchar(25)
);

/*Self reference*/
<<<<<<< HEAD
create table contacList(
    clId serial primary key ,
    ownerId integer references member(mId),
    contactId integer references member(mId)
);

/*Chats*/
create table chat (
    cId serial PRIMARY KEY ,
    cName varchar(25),
    mId integer references member(mId) --id del Owner
=======
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
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
);

/*Messages*/
create table messages(
    msgId serial primary key ,
    content varchar(250),
<<<<<<< HEAD
    mId integer references member(mId),
    cId integer references chat(cId),
=======
    userId integer references users(userId),
    groupId integer references groups(groupId),
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
    postDate date,
    postTime time
);

/*reply*/
<<<<<<< HEAD
create table reply(
    rId serial primary key ,
    repliedToId integer references messages(msgId),
    reponseId integer references  messages(msgId)
=======
create table replies(
    repliedToId integer references messages(msgId),
    msgId integer references  messages(msgId),
    primary key( repliedToId, msgId)
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
);

/*Reactions*/
create table likes(
<<<<<<< HEAD
    lId serial primary key ,
    mId integer references member(mId),
=======
    likeId serial primary key ,
    userId integer references users(userId),
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
    msgId integer references messages(msgId)
);

create table dislikes(
<<<<<<< HEAD
    dlId serial primary key ,
    mId integer references member(mId),
=======
    dislikeId serial primary key ,
    userId integer references users(userId),
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
    msgId integer references messages(msgId)
);

/*user-group relation*/
create table participants(
<<<<<<< HEAD
    mId integer references member(mId),
    cId integer references chat(cId),
    primary key (mId,cId)
=======
    userId integer references users(userId),
    groupId integer references groups(groupId),
    primary key (userId,groupId)
>>>>>>> 77446cd962ea0d1bd98a1deb9452e96124906b45
);