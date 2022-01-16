DROP TABLE IF EXISTS PROKIPTEI;
DROP TABLE IF EXISTS EDREVEI;
DROP TABLE IF EXISTS DIEUTHINETAI;
DROP TABLE IF EXISTS PROPONEITAI;
DROP TABLE IF EXISTS SKORAREI;
DROP TABLE IF EXISTS SIMETEXEI;
DROP TABLE IF EXISTS TIMORIA;
DROP TABLE IF EXISTS PAIZEI;
DROP TABLE IF EXISTS PODOSFAIRISTIS;
DROP TABLE IF EXISTS OMADA;
DROP TABLE IF EXISTS PROPONHTHS;
DROP TABLE IF EXISTS GHPEDO;
DROP TABLE IF EXISTS DIAITITIS;
DROP TABLE IF EXISTS AGONAS;

CREATE TABLE PODOSFAIRISTIS(
arithmos_adeias INTEGER,
name nvarchar(100),
hm_gennisews date,
topos_gennisews varchar(100),
ethnikotita varchar(100),
CONSTRAINT pk_podosfairistis PRIMARY KEY (arithmos_adeias)
);

 CREATE TABLE OMADA(
 kodikos_omadas INTEGER,
 dieuthinsi varchar(100),
 name varchar(100),
 tilefono varchar(10),
 CONSTRAINT pk_omada PRIMARY KEY (kodikos_omadas)
 );
 
 CREATE TABLE PAIZEI(
 arithmos_adeias INTEGER,
 kodikos_omadas INTEGER,
 CONSTRAINT pk_paizei PRIMARY KEY (arithmos_adeias,kodikos_omadas),
 CONSTRAINT fk_podosfairistis_paizei FOREIGN KEY (arithmos_adeias) REFERENCES PODOSFAIRISTIS(arithmos_adeias),
 CONSTRAINT fk_omada_paizei FOREIGN KEY (kodikos_omadas) REFERENCES OMADA(kodikos_omadas)
 );
 
 CREATE TABLE PROPONHTHS(
 diploma_proponitikis INTEGER,
 name varchar(100),
 ethnikotita varchar(100),
 CONSTRAINT pk_proponitits PRIMARY KEY (diploma_proponitikis)
 );
 
 CREATE TABLE GHPEDO(
kodikos_ghpedou INTEGER,
hm_kataskeuvis date,
poli varchar(100),
xoritikotita_gipedou varchar(100),
CONSTRAINT pk_ghpedo PRIMARY KEY (kodikos_ghpedou)
);

CREATE TABLE AGONAS(
arithmos_agonistikis INTEGER,
entos_edras_omada varchar(100),
ektos_edras_omada varchar(100),
hmirominia datetime,
CONSTRAINT pk_agonas PRIMARY KEY(arithmos_agonistikis)
); 
 
 CREATE TABLE DIAITITIS(
 arithmos_diaititi INTEGER,
 name varchar(100),
 poli varchar(100),
 katigoria_diaititi varchar(100),
 CONSTRAINT pk_diaititi PRIMARY KEY (arithmos_diaititi)
 );
 
 CREATE TABLE TIMORIA(
 arithmos_timorias INTEGER,
 eidos varchar(10),
 xronos time,
 kodikos_podosfairisti INTEGER,
 CONSTRAINT pk_timoria PRIMARY KEY (arithmos_timorias),
 CONSTRAINT fk_timoria_podosfairistis FOREIGN KEY (kodikos_podosfairisti) REFERENCES PODOSFAIRISTIS(arithmos_adeias)
 );
 
 CREATE TABLE SIMETEXEI(
 arithmos_adeias INTEGER,
 arithmos_agonistikis INTEGER,
 allagi datetime,--NULL an paizei apo tin arxei
 CONSTRAINT pk_simetexei PRIMARY KEY (arithmos_adeias , arithmos_agonistikis),
 CONSTRAINT fk_podosfairisti_simetexei FOREIGN KEY (arithmos_adeias) REFERENCES PODOSFAIRISTIS (arithmos_adeias),
 CONSTRAINT fk_simetexei_agonas FOREIGN KEY (arithmos_agonistikis) REFERENCES AGONAS (arithmos_agonistikis)
 );
 
 CREATE TABLE SKORAREI(
 arithmos_adeias INTEGER,
 arithmos_agonistikis INTEGER,
 skor_entos_edras_omada INTEGER,
 skor_ektos_edras_omada INTEGER,
 xronos time,
 CONSTRAINT pk_skorarei PRIMARY KEY (arithmos_adeias, arithmos_agonistikis),
 CONSTRAINT fk_podosfairisti_skorarei FOREIGN KEY (arithmos_adeias) REFERENCES PODOSFAIRISTIS (arithmos_adeias),
 CONSTRAINT fk_agonas_skorarei FOREIGN KEY(arithmos_agonistikis) REFERENCES AGONAS(arithmos_agonistikis)
 );
 
 CREATE TABLE PROPONEITAI(
 kodikos_omadas INTEGER,
 diploma_proponitikis INTEGER,
 hm_enarksi_simvoleou date,
 hm_liksis_simvoleou date,
 CONSTRAINT pk_proponeitai PRIMARY KEY (kodikos_omadas,diploma_proponitikis),
 CONSTRAINT fk_omada_proponite FOREIGN KEY (kodikos_omadas) REFERENCES OMADA(kodikos_omadas),
 CONSTRAINT fk_agonas_proponite FOREIGN KEY (diploma_proponitikis) REFERENCES PROPONHTHS(diploma_proponitikis)
 );
 
 CREATE TABLE EDREVEI(
 kodikos_omadas INTEGER,
 kodikos_ghpedou INTEGER,
 CONSTRAINT pk_edrevei PRIMARY KEY (kodikos_omadas,kodikos_ghpedou),
 CONSTRAINT fk_omada_edrevei FOREIGN KEY (kodikos_omadas) REFERENCES OMADA (kodikos_omadas),
 CONSTRAINT fk_ghpedo_edrevei FOREIGN KEY (kodikos_ghpedou) REFERENCES GHPEDO (kodikos_ghpedou)
 );
 
CREATE TABLE DIEUTHINETAI(
arithmos_diaititi INTEGER,
arithmos_agonistikis INTEGER,
CONSTRAINT pk_dieuthinetai PRIMARY KEY (arithmos_diaititi,arithmos_agonistikis),
CONSTRAINT fk_agonas_dieuthinetai FOREIGN KEY (arithmos_agonistikis) REFERENCES AGONAS(arithmos_agonistikis),
CONSTRAINT fk_diaititis_dieuthinetai FOREIGN KEY (arithmos_diaititi) REFERENCES DIAITITIS(arithmos_diaititi)
);

CREATE TABLE PROKIPTEI(
arithmos_agonistikis INTEGER,
arithmos_timorias INTEGER,
CONSTRAINT pk_prokiptei PRIMARY KEY (arithmos_agonistikis,arithmos_timorias),
CONSTRAINT fk_timoria_prokiptei FOREIGN KEY(arithmos_timorias) REFERENCES TIMORIA(arithmos_timorias),
CONSTRAINT fk_agonas_prokiptei FOREIGN KEY(arithmos_agonistikis) REFERENCES AGONAS(arithmos_agonistikis)
);