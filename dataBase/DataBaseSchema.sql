/*User*/
create table user( IdUser serial primary key, uFirstName varchar(15), uLastName varchar(15), 
    username varchar(15) , uPassword varchar(8),  phoneNumber char(10), email varchar(25));

--Self reference
create table contactlist( IdContactList serial primary key, IdOwner integer references user(IdUser),
    IdContact integer references user(IdUser)  );


/*Groups*/
create table group( IdGroup serial primary key, gName varchar(15), 
    IdOwner integer references user (IdUser)/*Este FK es para la relacion de creates*/);

/*Messages*/
create table msg( IdMessage serial primary key, content varchar(250), IdUser integer references user(IdUser), 
    IdGroup integer references group(IdGroup), postDate date, postTime time );

create table reply( IdReply serial primary, IdRepliedTo integer references message(IdMessage), content varchar(250));

/*Reactions*/
create table likes( IdLikes serial primary key, IdUser integer references user(IdUser), 
    IdMessage integer references msg(IdMessage) );

create table dislikes( IdDislikes serial primary key, IdUser integer references user(IdUser), 
    IdMessage integer references msg(IdMessage) );

/*Relations from user-group*/
create table participants( IdUser integer references user(IdUser),IdGroup integer references group(IdGroup) , 
    primary key(IdUser,IdGroup));

/*Relation user-message*/
create table readby( IdUser integer references user(IdUser),IdMessage integer references msg(IdMessage) ,
     primary key(IdUser,IdGroup),readDate date, readTime time );



