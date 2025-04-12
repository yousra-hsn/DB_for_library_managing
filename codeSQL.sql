CREATE TABLE Membre (
  login varchar(30) PRIMARY KEY,
  motDePasse varchar(30) NOT NULL,
  nom varchar(50),
  prenom varchar(50),
  adresse varchar(100),
  email varchar(30)
);

CREATE TABLE Adherent (
  login varchar(30) PRIMARY KEY,
  motDePasse varchar(30) NOT NULL,
  nom varchar(50),
  prenom varchar(50),
  adresse varchar(100),
  email varchar(30)
  dateNaissance date,
  telephone integer,
  adhesion boolean,
  blacklist boolean,
  droitPret boolean
);

CREATE TABLE Ressource (
  code varchar(10) PRIMARY KEY,
  titre varchar(30),
  dateApparition date,
  editeur varchar(30),
  genre varchar(30),
  codeClassification varchar(30) UNIQUE
);

CREATE TABLE Livre (
  code varchar(10) PRIMARY KEY,
  titre varchar(30),
  dateApparition date,
  editeur varchar(30),
  genre varchar(30),
  codeClassification varchar(30) UNIQUE,
  isbn varchar(10) UNIQUE,
  resume varchar(255),
  langue varchar(30),
  FOREIGN KEY (code) REFERENCES Ressource(code)
);

CREATE TABLE OeuvreMusicale (
  code varchar(10) PRIMARY KEY,
  titre varchar(30),
  dateApparition date,
  editeur varchar(30),
  genre varchar(30),
  codeClassification varchar(30) UNIQUE,
  longueur int(5),
  FOREIGN KEY (code) REFERENCES Ressource(code)
);

CREATE TABLE Film (
  code varchar(10) PRIMARY KEY,
  titre varchar(30),
  dateApparition date,
  editeur varchar(30),
  genre varchar(30),
  codeClassification varchar(30) UNIQUE,
  langue varchar(30),
  duree int(5),
  synopsis varchar(255),
  FOREIGN KEY (code) REFERENCES Ressource(code)
);

CREATE TABLE Contributeur (
  idContributeur varchar(10) PRIMARY KEY,
  nom varchar(30) NOT NULL,
  prenom varchar(50) NOT NULL,
  dateNaisance date,
  nationalite varchar(30)
);

CREATE TABLE EtatExemplaire (
  nom varchar(30) PRIMARY KEY
);

CREATE TABLE Exemplaire (
  idExemplaire varchar(10) PRIMARY KEY,
  etat varchar(30) NOT NULL REFERENCES EtatExemplaire(nom),
  disponible boolean,
  ressource varchar(10) NOT NULL REFERENCES Ressource(code),
  reserve varchar(30) REFERENCES Adherent(login)
);

CREATE TABLE Pret (
  idPret varchar(15) PRIMARY KEY,
  dateDebut date,
  dateRetourPrevue date,
  dateRetourReelle date,
  etatRetour varchar REFERENCES EtatExemplaire(nom),
  exemplaire varchar(10) NOT NULL REFERENCES Exemplaire(idExemplaire),
  adherent varchar(30) NOT NULL REFERENCES Adherent(login),
  CHECK (dateDebut<=dateRetourPrevue),
  CHECK (dateDebut<=dateRetourReelle),
  CHECK (etatRetour in ('bon','abime','perdu'))
);

CREATE TABLE MotifSanction (
  nom varchar(30) PRIMARY KEY
);

CREATE TABLE Sanction (
  idSanction varchar(10) PRIMARY KEY,
  motif varchar(30) NOT NULL REFERENCES MotifSanction(nom),
  dateDebut date,
  dateFin date,
  adherent varchar(30) NOT NULL REFERENCES Adherent(login),
  pret varchar(15) NOT NULL REFERENCES Pret(idPret)
);

CREATE TABLE AEcrit (
  contributeur varchar(10) REFERENCES Contributeur(idContributeur),
  livre varchar(10) REFERENCES Livre(code),
  PRIMARY KEY (contributeur, livre)
);

CREATE TABLE ACompose (
  contributeur varchar(10) REFERENCES Contributeur(idContributeur),
  oeuvre varchar(10) REFERENCES OeuvreMusicale(code),
  PRIMARY KEY (contributeur, oeuvre)
);

CREATE TABLE AInterprete (
  contributeur varchar(10) REFERENCES Contributeur(idContributeur),
  oeuvre varchar(10) REFERENCES OeuvreMusicale(code),
  PRIMARY KEY (contributeur, oeuvre)
);

CREATE TABLE ARealise (
  contributeur varchar(10) REFERENCES Contributeur(idContributeur),
  film varchar(10) REFERENCES Film(code),
  PRIMARY KEY (contributeur, film)
);

CREATE TABLE AJoueDans (
  contributeur varchar(10) REFERENCES Contributeur(idContributeur),
  film varchar(10) REFERENCES Film(code),
  PRIMARY KEY (contributeur, film)
);

INSERT INTO EtatExemplaire VALUES ('neuf');
INSERT INTO EtatExemplaire VALUES ('bon');
INSERT INTO EtatExemplaire VALUES ('abime');
INSERT INTO EtatExemplaire VALUES ('perdu');

INSERT INTO MotifSanction VALUES ('retard');
INSERT INTO MotifSanction VALUES ('deterioration');
INSERT INTO MotifSanction VALUES ('perte');

INSERT INTO Membre VALUES ('fontmar', '1893FMart', 'Fontenay', 'Martine', '12 Avenue Foch, 94300 Vincennes', 'martine.fontenay71@yahoo.fr');
INSERT INTO Membre VALUES ('pethel', 'pitith2', 'Petit', 'Heloise', '35 Rue Saint-Antoine 60200 Compiègne', 'petit44@gmail.com');
INSERT INTO Membre VALUES ('dujpie', 'FFf3j7iu', 'Dujardin', 'Pierre', '2 Rue de Paris, 75010 Paris', 'pierredujardin@protonmail.com');

INSERT INTO Adherent VALUES ('hasyou', 'effnk', 'Hassan', 'Yousra', '3 Rue Georges Bernanos, 60200 Compiègne', 'hassra@gmail.com', '2002-03-02', 0689273729, true, false, true);
INSERT INTO Adherent VALUES ('rouale', 'rrrji2KE3', 'Roullet', 'Augustin', '15 Rue des Lombards, 60200 Compiègne', 'alex43@yahoo.fr', '2002-06-21', 0630572933, true, false, true);
INSERT INTO Adherent VALUES ('honjul', 'JSOL44', 'Hong', 'Julie', '30 Rue Notre-Dame de Bon Secours, 60200 Compiègne', 'julie.hong@etu.utc.fr', '1999-04-28', 0781170283, true, false, false);
INSERT INTO Adherent VALUES ('pauale', 'o8u24huD', 'Pauvarel', 'Alexandre', '9 Boulevard Gambetta, 60200 Compiègne', 'alexandrepauv5@gmail.com', '2022-04-12', 0628663517, true, false, true);

INSERT INTO Contributeur VALUES ('1czs', 'Poquelin', 'Jean-Baptiste', '1673-02-17', 'Français');
INSERT INTO Contributeur VALUES ('2tss', 'Raymond', 'Usher', '1978-10-14', 'Américain');
INSERT INTO Contributeur VALUES ('356Hz', 'Beethoven Van', 'Ludwig', '1770-12-16', 'Allemand');

INSERT INTO Contributeur VALUES ('12esok', 'Lucas', 'George', '1944-05-14', 'Americain');
INSERT INTO Contributeur VALUES ('13jis2', 'Hamill', 'Mark', '1951-09-25', 'Americain');
INSERT INTO Contributeur VALUES ('10Lsj', 'Rowling', 'Joanne', '1965-07-31', 'Britannique');
INSERT INTO Contributeur VALUES ('11iugs4', 'Reed', 'Lou', '1942-03-02', 'Americain');

INSERT INTO Ressource values (
  '001',
  'Harry Potter a l''ecole des sorciers',
  '1997-06-26',
  'Bloomsbury',
  'Fantasie',
  'a-001'
);

INSERT INTO Ressource values (
  '101',
  'Transformer',
  '1972-12-08',
  'RCA',
  'Glam Rock',
  'b-101'
);

INSERT INTO Ressource values (
  '201',
  'Star Wars Un Nouvel Espoire',
  '1977-05-25',
  'Lucasflims',
  'Science-Fiction',
  'c-201'
);

INSERT INTO Ressource values (
  '002',
  '1984',
  '1949-06-08',
  'Secker and Warburg',
  'dystopie',
  'a-002'
);

INSERT INTO Ressource values (
  '102',
  'Avatar',
  '2009-12-18',
  '20th Century Fox',
  'science-fiction',
  'b-102'
);

INSERT INTO Ressource values (
  '202',
  'Thriller',
  '1982-11-10',
  'Epic',
  'pop',
  'c-202'
);

INSERT INTO Ressource values (
  '103',
  'Leto',
  '2018-05-09',
  'Hype film',
  'biopic',
 'b-103'
);

INSERT INTO Livre values (
  '001',
  'Harry Potter a l''ecole des sorciers',
  '1997-06-26',
  'Bloomsbury',
  'Fantasie',
  'a-001',
'0747532699',
'Harry Potter decouvre qu''il est un sorcier et va etudier a l''ecole de sorcellerie de Poudlard',
'anglaise'
);


INSERT INTO OeuvreMusicale values (
  '101',
  'Transformer',
  '1972-12-08',
  'RCA',
  'Glam Rock',
  'b-101',
37
);


INSERT INTO Film values (
  '201',
  'Star Wars Un Nouvel Espoire',
  '1977-05-25',
  'Lucasflims',
  'Science-Fiction',
  'c-201',
'anglaise',
121,
'Luke doit transmettre les plans de l''etoile noire a l''alliance rebelle'
);



INSERT INTO Livre values (
  '002',
  '1984',
  '1949-06-08',
  'Secker and Warburg',
  'dystopie',
  'a-002',
'0452284236',
'Depuis les annees 1950 le monde est divise en 3 empires: Oceania, Eurasia et Estasia, qui sont diriges par des regimes totalitaires',
'anglaise'
);


INSERT INTO Film values (
  '102',
  'Avatar',
  '2009-12-18',
  '20th Century Fox',
  'science-fiction',
  'b-102',
'anglais',
162,
'Une multinationale va envaillir une planete pour recuperer un minerai'
);



INSERT INTO OeuvreMusicale values (
  '202',
  'Thriller',
  '1982-11-10',
  'Epic',
  'pop',
  'c-202',
43
);


INSERT INTO Film values (
  '103',
  'Leto',
  '2018-05-09',
  'Hype film',
  'biopic',
 'b-103',
'russe',
126,
'l''histoire de la relation entre le guitariste Russe Viktor Tsoi et son mentor Mikhail Naoumenko'
);

INSERT INTO AEcrit values ('10Lsj', '001');
INSERT INTO ACompose values ('11iugs4', '101');
INSERT INTO AInterprete values ('11iugs4', '101');
INSERT INTO ARealise values ('12esok', '201');
INSERT INTO AJoueDans values ('13jis2', '201');

INSERT INTO Exemplaire values ('145678sf3', 'neuf', false, '001', NULL);
INSERT INTO Exemplaire values ('3234es678', 'neuf', true, '101', NULL);

INSERT INTO Pret values ('2362sec5', '2022-11-10', '2022-12-10', NULL, NULL, '145678sf3', 'honjul');
INSERT INTO Pret values ('ouha356j', '2022-09-12', '2022-10-12', '2022-10-01', 'abime', '3234es678', 'hasyou');

INSERT INTO Sanction values ('24jjr', 'deterioration', '2022-10-01', '2022-11-10', 'hasyou','ouha356j');

--Afficher les membres
SELECT nom, prenom, email
FROM Membre;

--Afficher les informations de l'utilisateur dont le login est 'hasyou'
SELECT login, nom, prenom, adresse, email, dateNaissance, telephone 
FROM Adherent 
WHERE login='hasyou';

--Afficher les informations de l'utilisateur Roullet Augustin
SELECT login, nom, prenom, adresse, email, dateNaissance, telephone 
FROM Adherent 
WHERE nom='Roullet' AND prenom='Augustin';

--Afficher si un adherent est blacklisté ou pas
SELECT login, nom, prenom, blacklist 
FROM Adherent 
WHERE login='hongjul';

--Afficher les informations du livre scanné avec le code
SELECT titre, dateApparition, editeur, genre, codeClassification
FROM Ressources 
WHERE code='001';

--Afficher si un adhérent peut emprunter
SELECT login, nom, prenom, droitPret
FROM Adherent 
WHERE login='pauale';

--Afficher le code de la ressource grâce au titre de la ressource
SELECT code 
FROM Ressource 
WHERE titre='Avatar';

--Afficher les exemplaires empruntables de Transformer
SELECT idExemplaire, titre, codeClassification 
FROM Exemplaire 
WHERE ressource='Transformer' 
AND disponible=TRUE
AND (etat = 'neuf' or etat = 'bon') 
AND reserve IS NULL;

--Afficher les prêts d'un utilisateur
SELECT * 
FROM Pret 
WHERE adherent='hongjul';

--Afficher les prêts en retard d'un utilisateur
SELECT * 
FROM Pret 
WHERE adherent='hongjul' AND dateRetourReelle>dateRetourPrevue;

--Afficher les adhérents qui le sont encore actuellement
SELECT login, nom, prenom
FROM Adherent 
WHERE adhesion=True;

--Afficher le nombre de prêts actuels de l'utilisateur 'pauale'
SELECT count (*) 
FROM Adherent INNER JOIN Pret 
ON Adherent.login = Pret.adherent 
WHERE dateRetourReelle > current_date AND login='pauale';

--Afficher le nombre de sanctions de l'utilisateur 'hasyou'
SELECT count (*) 
FROM Adherent INNER JOIN Sanction 
ON Adherent.login = Sanction.adherent 
WHERE (DateFinSanction > current_date OR DateFinSanction IS NULL) 
AND login='hasyou';

--Afficher la disponibilité d'un titre de ressource, si pas disponible afficher sa date de retour prévue
SELECT R.titre, E.disponible, P.dateRetourPrevue F
ROM (Exemplaire E INNER JOIN Ressource R ON E.ressource = R.code) LEFT OUTER JOIN Pret P 
ON E.idExemplaire = P.exemplaire 
WHERE R.titre = 'Transformer'
ORDER BY idExemplaire;

--Afficher les informations du contributeur
SELECT * 
FROM Contributeur 
WHERE nom='Rowling' AND prenom'Joanne';


-- nombre de prets actuels par adherent
SELECT adherent, sum(idPret)
FROM Pret
WHERE dateRetourReelle IS NULL
GROUP BY adherent

-- nombre de prets de l'année 2022 par titre
SELECT titre, sum(idPret)
FROM Pret P (INNER JOIN Exemplaire E ON P.exemplaire=E.idExemplaire) INNER JOIN Ressource R ON E.ressource=R.code
WHERE dateDebut > 2022-01-01 AND dateRetourReelle < 2022-12-31
GROUP BY titre;

-- nombre de sanctions par adherent
SELECT adherent, sum(idSanction)
FROM Sanction
GROUP BY adherent;

-- ressource la plus empruntée et les autres dans l'ordre
SELECT titre, sum(idPret)
FROM Pret P (INNER JOIN Exemplaire E ON P.exemplaire=E.idExemplaire) INNER JOIN Ressource R ON E.ressource=R.code
GROUP BY titre
ORDER BY sum(idPret);

-- nombre d'exemplaires par etat pour savoir combien de ressources sont à restaurer
SELECT titre, etat, sum(etat)
FROM Exemplaire E INNER JOIN Ressource R
ON E.ressource=R.code
GROUP BY etat;
