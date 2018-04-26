/*Creating user (member)*/
create table member(
    mId serial primary key ,
    mFirstName varchar(15),
    mLastName varchar(15),
    username varchar(15),
    uPassword char(8),
    phoneNumber char(12),
    email varchar(25)
);

/*Self reference*/
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
);

/*Messages*/
create table messages(
    msgId serial primary key ,
    content varchar(250),
    mId integer references member(mId),
    cId integer references chat(cId),
    postDate date,
    postTime time
);

/*reply*/
create table reply(
    rId serial primary key ,
    repliedToId integer references messages(msgId),
    reponseId integer references  messages(msgId)
);

/*Reactions*/
create table likes(
    lId serial primary key ,
    mId integer references member(mId),
    msgId integer references messages(msgId)
);

create table dislikes(
    dlId serial primary key ,
    mId integer references member(mId),
    msgId integer references messages(msgId)
);

/*user-group relation*/
create table participants(
    mId integer references member(mId),
    cId integer references chat(cId),
    primary key (mId,cId)
);