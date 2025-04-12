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

CREATE TABLE Membre (
  login varchar(30) PRIMARY KEY,
  motDePasse varchar(30) NOT NULL,
  nom varchar(50),
  prenom varchar(50),
  adresse varchar(100),
  email varchar(30)
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
  adherent JSON NOT NULL,
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
  adherent JSON NOT NULL,
  pret varchar(15) NOT NULL REFERENCES Pret(idPret)
);

CREATE TABLE AEcrit (
  contributeur JSON NOT NULL,
  livre varchar(10) REFERENCES Livre(code),
  PRIMARY KEY (contributeur, livre)
);

CREATE TABLE ACompose (
  contributeur JSON NOT NULL,
  oeuvre varchar(10) REFERENCES OeuvreMusicale(code),
  PRIMARY KEY (contributeur, oeuvre)
);

CREATE TABLE AInterprete (
  contributeur JSON NOT NULL,
  oeuvre varchar(10) REFERENCES OeuvreMusicale(code),
  PRIMARY KEY (contributeur, oeuvre)
);

CREATE TABLE ARealise (
  contributeur JSON NOT NULL,
  film varchar(10) REFERENCES Film(code),
  PRIMARY KEY (contributeur, film)
);

CREATE TABLE AJoueDans (
  contributeur JSON NOT NULL,
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

INSERT INTO Ressource VALUES (
  '001',
  'Harry Potter a l''ecole des sorciers',
  '1997-06-26',
  'Bloomsbury',
  'Fantasie',
  'a-001'
);

INSERT INTO Ressource VALUES (
  '101',
  'Transformer',
  '1972-12-08',
  'RCA',
  'Glam Rock',
  'b-101'
);

INSERT INTO Ressource VALUES (
  '201',
  'Star Wars Un Nouvel Espoire',
  '1977-05-25',
  'Lucasflims',
  'Science-Fiction',
  'c-201'
);

INSERT INTO Ressource VALUES (
  '002',
  '1984',
  '1949-06-08',
  'Secker and Warburg',
  'dystopie',
  'a-002'
);

INSERT INTO Ressource VALUES (
  '102',
  'Avatar',
  '2009-12-18',
  '20th Century Fox',
  'science-fiction',
  'b-102'
);

INSERT INTO Ressource VALUES (
  '202',
  'Thriller',
  '1982-11-10',
  'Epic',
  'pop',
  'c-202'
);

INSERT INTO Ressource VALUES (
  '103',
  'Leto',
  '2018-05-09',
  'Hype film',
  'biopic',
 'b-103'
);

INSERT INTO Livre VALUES (
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


INSERT INTO OeuvreMusicale VALUES (
  '101',
  'Transformer',
  '1972-12-08',
  'RCA',
  'Glam Rock',
  'b-101',
37
);


INSERT INTO Film VALUES (
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


INSERT INTO Livre VALUES (
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


INSERT INTO Film VALUES (
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

INSERT INTO OeuvreMusicale VALUES (
  '202',
  'Thriller',
  '1982-11-10',
  'Epic',
  'pop',
  'c-202',
43
);


INSERT INTO Film VALUES (
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

INSERT INTO AEcrit VALUES ('{"nom":"Rowling", "prenom":"Joanne", "dateNaissance":"1965-07-31", "nationalite":"Britannique"}', '001');
INSERT INTO ACompose VALUES ('{"nom":"Beethoven Van", "prenom":"Ludwig", "dateNaissance":"1770-12-16", "nationalite":"Allemand"}', '101');
INSERT INTO AInterprete VALUES ('{"nom":"Raymond", "prenom":"Usher", "dateNaissance":"1978-10-14", "nationalite":"Americain"}', '101');
INSERT INTO ARealise VALUES ('{"nom":"Lucas", "prenom":"Georges", "dateNaissance":"1944-05-14", "nationalite":"Americain"}', '201');
INSERT INTO AJoueDans VALUES ('{"nom":"Hamill", "prenom":"Mark", "dateNaissance":"1951-11-25", "nationalite":"Americain"}', '201');

INSERT INTO Exemplaire VALUES ('145678sf3', 'neuf', false, '001', NULL);
INSERT INTO Exemplaire VALUES ('3234es678', 'neuf', true, '101', NULL);

INSERT INTO Pret VALUES ('2362sec5', '2022-11-10', '2022-12-10', NULL, NULL, '145678sf3', '{"motDePasse":"rrrji2KE3", "nom":"Roullet", "prenom":"Augustin", "adresse":"15 Rue des Lombards, 60200 Compiègne", "email":"alex43@yahoo.fr", "dateNaissance":"2002-06-21", "telephone":"0630572933","adhesion":"true","blacklist":"false","droitPret":"true}');
INSERT INTO Pret VALUES ('ouha356j', '2022-09-12', '2022-10-12', '2022-10-01', 'abime', '3234es678', '{"login":"hasyou","motDePasse":"effnk", "nom":"Hassan", "prenom":"Yousra", "adresse":"3 Rue Georges Bernanos, 60200 Compiègne", "email":"hassra@gmail.com", "dateNaissance":"2002-03-02", "telephone":"0689273729","adhesion":"true","blacklist":"false","droitPret":"true}');

INSERT INTO  Sanction (idSanction, motif, dateDebut, dateFin, adherent, pret) VALUES (
'24jjr',
'deterioration',
'2022-10-01',
'2022-11-10',
'{"login":"hasyou","motDePasse":"effnk", "nom":"Hassan", "prenom":"Yousra", "adresse":"3 Rue Georges Bernanos, 60200 Compiègne", "email":"hassra@gmail.com", "dateNaissance":"2002-03-02", "telephone":"0689273729","adhesion":"true","blacklist":"false","droitPret":"true}'
'ouha356j'
);

INSERT INTO Sanction (idSanction, motif, dateDebut, dateFin, adherent, pret) VALUES (
'44gjr',
'retard',
'2022-12-08',
'2023-03-01',
'{"motDePasse":"rrrji2KE3", "nom":"Roullet", "prenom":"Augustin", "adresse":"15 Rue des Lombards, 60200 Compiègne", "email":"alex43@yahoo.fr", "dateNaissance":"2002-06-21", "telephone":"0630572933","adhesion":"true","blacklist":"false","droitPret":"true}'
'2362sec5'
);
