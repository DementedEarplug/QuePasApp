/*User*/
create table user( IdUser serial primary key, uFirstName varchar(15), uLastName varchar(15), username varchar(15), uPassword varchar(8) /*(How to say this is encrypted*/ );
create table phone( IdPhone serial primary key, IdUser integer references user(IdUser), phoneNumber char(10));
create table emails( IdEmail serial primary key, IdUser integer references user (IdUser), email varchar(25));
/*Tables for contacts*/


/*groups*/
create table group( IdGroup serial primary key, gName varchar(15), IdUser integer references user (IdUser)/*Este FK es para la relacion de creates*/);
create table participants( IdParticipants serial primary key, IdGroup integer references group(IdGroup) );

/*Messages and reactions*/
create table msg( IdMessage serial primary key, content varchar(250), IdUser integer references user(IdUser), IdGroup integer references group(IdGroup), postDate date, postTime time );
/*Table for replies*/
create table reactions( IdReaction serial primary key, IdUser integer references user(IdUser), IdMessage integer references msg(IdMessage) );
create table likes( IdLikes serial primary key);
create table dislikes( IdDislikes serial primary key);

/*Relations from user-group*/
create table belongsTo( IdUser integer references user(IdUser),IdGroup integer references group(IdGroup) , primary key(IdUser,IdGroup));

/*Relation user-reaction*/
create table makes( IdUser integer references user(IdUser),IdReaction integer references reactions(IdReaction) , primary key(IdUser,IdReaction));

/*Relation user-message*/
create table readby( IdUser integer references user(IdUser),IdMessage integer references msg(IdMessage) , primary key(IdUser,IdGroup),readDate date, readTime time );



