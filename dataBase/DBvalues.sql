--Values for members
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Gabriel', 'Reyes','Reaper','Talon1288','666-006-0606','reaper@talon.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Brigitte', 'Lindholm','Squire97','EngineeringForeveL12','756-225-8489','brigitaPitta12@gmail.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Shao', 'Kahn','KingOfKing','NeatherRealm188','758-996-3625','getHuemans1@yahoo.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Sonya', 'Blayde','Kissshot','Jaxxx9887','452-052-3625','blondie1288@gmail.com');

--Values for groups (they have keys from 7-8)
insert into groups(groupName, ownerId) values('WomboCombo', 1);
insert into groups(groupName, ownerId) values('BestiasICOM', 3);
insert into groups(groupName, ownerId) values('PUBYI', 4);
insert into groups(groupName, ownerId) values('DIBI', 2);

--Values for messages (los numeros de userId y groupId estan subject to change
insert  into messages(content, userId, groupId, postdate, posttime) values('Heyyyyyyyy',1,1,'2018-03-27','00:03:05');
insert  into messages(content, userId, groupId, postdate, posttime) values('Dimelox!',3,1,'2018-03-27','00:03:06');
insert  into messages(content, userId, groupId, postdate, posttime) values('Comemos en Dennys hoy?',1,1,'2018-03-27','00:03:12');
insert  into messages(content, userId, groupId, postdate, posttime) values('SIIIIIII',2,1,'2018-03-27','00:03:59');
insert  into messages(content, userId, groupId, postdate, posttime) values('Vamo allax!',4,1,'2018-03-27','00:03:05');)
insert  into messages(content, userId, groupId, postdate, posttime) values('Acabaron el projecto?!?!?',2,2,'2018-04-26','23:58:05');
insert  into messages(content, userId, groupId, postdate, posttime) values('Nooo! :(',3,2,'2018-04-26','23:58:06');
insert  into messages(content, userId, groupId, postdate, posttime) values('Y tu??',3,2,'2018-04-26','23:58:06');
insert  into messages(content, userId, groupId, postdate, posttime) values('Tampoco, nos jodimos!!!',2,2,'2018-04-26','23:59:12');
insert  into messages(content, userId, groupId, postdate, posttime) values('Vamos pa Pochinkiii?',2,3,'2018-04-26','23:58:05');
insert  into messages(content, userId, groupId, postdate, posttime) values('Acho no, voy a jugar Fortnite...',3,3,'2018-04-26','23:58:06');
insert  into messages(content, userId, groupId, postdate, posttime) values('Pero KEEEEH!?',3,3,'2018-04-26','23:58:06');
insert  into messages(content, userId, groupId, postdate, posttime) values('Ahhhhh que clase de pussy!',2,3,'2018-04-26','23:59:12');
insert  into messages(content, userId, groupId, postdate, posttime) values('*Shao was kicked from the group*',2,3,'2018-04-26','23:59:12');
insert  into messages(content, userId, groupId, postdate, posttime) values('Hay que empezar la fase 2...',6,4,'2018-04-26','15:00:05');

--Participants
insert  into participants(userId, groupId) values (5,6);
insert  into participants(userId, groupId) values (6,6);
insert  into participants(userId, groupId) values (7,6);
insert  into participants(userId, groupId) values (8,6);
insert  into participants(userId, groupId) values (6,7);
insert  into participants(userId, groupId) values (7,7);
insert  into participants(userId, groupId) values (8,7);
insert  into participants(userId, groupId) values (5,8);
insert  into participants(userId, groupId) values (6,8);
insert  into participants(userId, groupId) values (7,8);
insert  into participants(userId, groupId) values (8,8);
insert  into participants(userId, groupId) values (5,9);
insert  into participants(userId, groupId) values (6,9);
insert  into participants(userId, groupId) values (7,9);
insert  into participants(userId, groupId) values (8,9);

