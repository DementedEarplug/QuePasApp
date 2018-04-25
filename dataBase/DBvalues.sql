--Values for members
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Gabriel', 'Reyes','Reaper','Talon1288','666-006-0606','reaper@talon.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Brigitte', 'Lindholm','Squire97','EngineeringForeveL12','756-225-8489','brigitaPitta12@gmail.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Shao', 'Kahn','KingOfKing','NeatherRealm188','758-996-3625','getHuemans1@yahoo.com');
insert into member(mfirstname, mlastname, username, mupassword, phonenumber, email) 
    values('Sonya', 'Blayde','Kissshot','Jaxxx9887','452-052-3625','blondie1288@gmail.com');

--Values for chat (they have keys from 7-8)
insert into chat(cname, mid) values('WomboCombo', 5);
insert into chat(cname, mid) values('BestiasICOM', 7);
insert into chat(cname, mid) values('PUBYI', 6);
insert into chat(cname, mid) values('DIBI', 8);

--Values for messages (los numeros de mid y cid estan subject to change
insert  into messages(content, mid, cid, postdate, posttime) values('Heyyyyyyyy',5,6,'2018-03-27','00:03:05');
insert  into messages(content, mid, cid, postdate, posttime) values('Dimelox!',7,6,'2018-03-27','00:03:06');
insert  into messages(content, mid, cid, postdate, posttime) values('Comemos en Dennys hoy?',5,6,'2018-03-27','00:03:12');
insert  into messages(content, mid, cid, postdate, posttime) values('SIIIIIII',6,6,'2018-03-27','00:03:59');
insert  into messages(content, mid, cid, postdate, posttime) values('Vamo allax!',8,6,'2018-03-27','00:03:05');)
insert  into messages(content, mid, cid, postdate, posttime) values('Acabaron el projecto?!?!?',6,8,'2018-04-26','23:58:05');
insert  into messages(content, mid, cid, postdate, posttime) values('Nooo! :(',7,8,'2018-04-26','23:58:06');
insert  into messages(content, mid, cid, postdate, posttime) values('Y tu??',7,8,'2018-04-26','23:58:06');
insert  into messages(content, mid, cid, postdate, posttime) values('Tampoco, nos jodimos!!!',6,7,'2018-04-26','23:59:12');
insert  into messages(content, mid, cid, postdate, posttime) values('Vamos pa Pochinkiii?',6,8,'2018-04-26','23:58:05');
insert  into messages(content, mid, cid, postdate, posttime) values('Acho no, voy a jugar Fortnite...',7,8,'2018-04-26','23:58:06');
insert  into messages(content, mid, cid, postdate, posttime) values('Pero KEEEEH!?',7,8,'2018-04-26','23:58:06');
insert  into messages(content, mid, cid, postdate, posttime) values('Ahhhhh que clase de pussy!',6,8,'2018-04-26','23:59:12');
insert  into messages(content, mid, cid, postdate, posttime) values('*Shao was kicked from the group*',6,8,'2018-04-26','23:59:12');
insert  into messages(content, mid, cid, postdate, posttime) values('Hay que empezar la fase 2...',6,8,'2018-04-26','15:00:05');

--Participants
insert  into participants(mid, cid) values (5,6);
insert  into participants(mid, cid) values (6,6);
insert  into participants(mid, cid) values (7,6);
insert  into participants(mid, cid) values (8,6);
insert  into participants(mid, cid) values (6,7);
insert  into participants(mid, cid) values (7,7);
insert  into participants(mid, cid) values (8,7);
insert  into participants(mid, cid) values (5,8);
insert  into participants(mid, cid) values (6,8);
insert  into participants(mid, cid) values (7,8);
insert  into participants(mid, cid) values (8,8);
insert  into participants(mid, cid) values (5,9);
insert  into participants(mid, cid) values (6,9);
insert  into participants(mid, cid) values (7,9);
insert  into participants(mid, cid) values (8,9);

