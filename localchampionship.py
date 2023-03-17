import sqlite3;
from tkinter import *
from tkinter import ttk
import tkinter as tk


def makeform(root, fields):
    entries = {};
    for field in fields:
        row = Frame(root);
        lab = Label(row,
                    width=12, text=field + ":	", anchor='w');
        ent = Entry(row);
        ent.insert(0, "0");
        row.pack(side=TOP, fill=X, padx=5, pady=5);
        lab.pack(side=LEFT);
        ent.pack(side=RIGHT, expand=YES, fill=X);
        entries[field] = ent;
    return entries;


def closeall():
    conn.commit();
    conn.close();
    root.quit();


def insertpodosfairisti(t,window):
    arithmos_adeias = t['arithmos_adeias'].get();
    name = t['name'].get();
    hm_gennisews = t['hm_gennisews'].get();
    topos_gennisews = t['topos_gennisews'].get();
    ethnikotita = t['ethnikotita'].get();
    conn.execute("INSERT INTO PODOSFAIRISTIS VALUES(?, ?, ?, ?, ?);",
                 (arithmos_adeias, name, hm_gennisews, topos_gennisews, ethnikotita));
    conn.commit()
    window.destroy();


def insertpodosfairistiform():
    root1 = Tk();
    root1.title("PODOSFAIRISTIS	FORM");
    root1.configure(background="white");
    fields = ("arithmos_adeias", "name", "hm_gennisews", "topos_gennisews","ethnikotita");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertpodosfairisti(ents,root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertomada(t,window):
    kodikos_omadas = t['kodikos_omadas'].get();
    dieuthinsi= t['dieuthinsi'].get();
    name = t['name'].get();
    tilefono = t['tilefono'].get();


    conn.execute("INSERT INTO OMADA VALUES(?, ?, ?, ?);",
                 (kodikos_omadas,dieuthinsi, name, tilefono));
    conn.commit()
    window.destroy();

def insertomadaform():
    root1 = Tk();
    root1.title("OMADA	FORM");
    root1.configure(background="white");
    fields = ("kodikos_omadas", "dieuthinsi","name",  "tilefono");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertomada(ents,root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertpaizei(t,window):
    arithmos_adeias = t['arithmos_adeias'].get();
    kodikos_omadas= t['kodikos_omadas'].get();

    conn.execute("INSERT INTO PAIZEI VALUES(?, ?);",
                 (arithmos_adeias,kodikos_omadas));
    conn.commit()
    window.destroy();

def insertpaizeiform():
    root1 = Tk();
    root1.title("PAIZEI	FORM");
    root1.configure(background="white");
    fields = ("arithmos_adeias", "kodikos_omadas");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertpaizei(ents,root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertproponhths(t,window):
    diploma_proponitikis= t['diploma_proponitikis'].get();
    name = t['name'].get();
    ethnikotita= t['ethnikotita'].get();


    conn.execute("INSERT INTO PROPONHTHS VALUES(?, ?, ?);",
                 (diploma_proponitikis, name, ethnikotita));
    conn.commit()
    window.destroy();

def insertpropnhthsform():
    root1 = Tk();
    root1.title("PROPONHTHS	FORM");
    root1.configure(background="white");
    fields = ("diploma_proponitikis","name",  "ethnikotita");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertproponhths(ents,root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertghpedo(t,window):
    kodikos_ghpedou = t['kodikos_ghpedou'].get();
    hm_kataskeuvis= t['hm_kataskeuvis'].get();
    poli = t['poli'].get();
    xoritikotita_gipedou = t['xoritikotita_gipedou'].get();


    conn.execute("INSERT INTO GHPEDO VALUES(?, ?, ?, ?);",
                 (kodikos_ghpedou,hm_kataskeuvis, poli, xoritikotita_gipedou));
    conn.commit()
    window.destroy();

def insertghpedoform():
    root1 = Tk();
    root1.title("GHPEDO	FORM");
    root1.configure(background="white");
    fields = ("kodikos_ghpedou", "hm_kataskeuvis", "poli","xoritikotita_gipedou");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertghpedo(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);


def insertagonas(t, window):
    arithmos_agonistikis = t['arithmos_agonistikis'].get();
    entos_edras_omada = t['entos_edras_omada'].get();
    ektos_edras_omada = t['ektos_edras_omada'].get();
    hmirominia = t['hmirominia'].get();

    conn.execute("INSERT INTO AGONAS VALUES(?, ?, ?, ?);",
                 (arithmos_agonistikis, entos_edras_omada, ektos_edras_omada, hmirominia));
    conn.commit()
    window.destroy();

def insertagonasform():
    root1 = Tk();
    root1.title("AGONAS	FORM");
    root1.configure(background="white");
    fields = ("arithmos_agonistikis", "entos_edras_omada", "ektos_edras_omada","hmirominia");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertagonas(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertdiaititis(t, window):
    arithmos_diaititi = t['arithmos_diaititi'].get();
    name = t['name'].get();
    poli = t['poli'].get();
    katigoria_diaititi = t['katigoria_diaititi'].get();

    conn.execute("INSERT INTO DIAITITIS VALUES(?, ?, ?, ?);",
                 (arithmos_diaititi, name, poli, katigoria_diaititi));
    conn.commit()
    window.destroy();

def insertdiaititisform():
    root1 = Tk();
    root1.title("DIAITITIS	FORM");
    root1.configure(background="white");
    fields = ("arithmos_diaititi", "name", "poli","katigoria_diaititi");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertdiaititis(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def inserttimoria(t, window):
    arithmos_timorias = t['arithmos_timorias'].get();
    eidos = t['eidos'].get();
    xronos = t['xronos'].get();
    kodikos_podosfairisti = t['kodikos_podosfairisti'].get();

    conn.execute("INSERT INTO TIMORIA VALUES(?, ?, ?, ?);",
                 (arithmos_timorias, eidos, xronos, kodikos_podosfairisti));
    conn.commit()
    window.destroy();

def inserttimoriaform():
    root1 = Tk();
    root1.title("TIMORIA FORM");
    root1.configure(background="white");
    fields = ("arithmos_timorias", "eidos", "xronos","kodikos_podosfairisti");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: inserttimoria(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertsimetexei(t, window):
    arithmos_adeias = t['arithmos_adeias'].get();
    arithmos_agonistikis = t['arithmos_agonistikis'].get();
    allagi = t['allagi'].get();

    conn.execute("INSERT INTO SIMETEXEI VALUES(?, ?, ?);",
                 (arithmos_adeias, arithmos_agonistikis, allagi));
    conn.commit()
    window.destroy();

def insertsimetexeiform():
    root1 = Tk();
    root1.title("SIMETEXEI FORM");
    root1.configure(background="white");
    fields = ("arithmos_adeias", "arithmos_agonistikis", "allagi");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertsimetexei(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertskorarei(t, window):
    arithmos_adeias = t['arithmos_adeias'].get();
    arithmos_agonistikis = t['arithmos_agonistikis'].get();
    skor_entos_edras_omada = t['skor_entos_edras_omada'].get();
    skor_ektos_edras_omada = t['skor_ektos_edras_omada'].get();
    xronos = t['xronos'].get();

    conn.execute("INSERT INTO SKORAREI VALUES(?, ?, ?, ?, ?);",
                 (arithmos_adeias, arithmos_agonistikis, skor_entos_edras_omada,skor_ektos_edras_omada,xronos));
    conn.commit()
    window.destroy();

def insertskorareiform():
    root1 = Tk();
    root1.title("SKORAREI FORM");
    root1.configure(background="white");
    fields = ("arithmos_adeias", "arithmos_agonistikis", "skor_entos_edras_omada","skor_ektos_edras_omada","xronos");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertskorarei(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertproponeitai(t, window):
    kodikos_omadas = t['kodikos_omadas'].get();
    diploma_proponitikis = t['diploma_proponitikis'].get();
    hm_enarksi_simvoleou = t['hm_enarksi_simvoleou'].get();
    hm_liksis_simvoleou = t['hm_liksis_simvoleou'].get();

    conn.execute("INSERT INTO PROPONEITAI VALUES(?, ?, ?, ?);",
                 (kodikos_omadas, diploma_proponitikis, hm_enarksi_simvoleou,hm_liksis_simvoleou));
    conn.commit()
    window.destroy();

def insertproponeitaiform():
    root1 = Tk();
    root1.title("PROPONEITAI FORM");
    root1.configure(background="white");
    fields = ("kodikos_omadas", "diploma_proponitikis", "hm_enarksi_simvoleou","hm_liksis_simvoleou");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertproponeitai(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertedrevei(t, window):
    kodikos_omadas = t['kodikos_omadas'].get();
    kodikos_ghpedou = t['kodikos_ghpedou'].get();

    conn.execute("INSERT INTO EDREVEI VALUES(?, ?);",
                 (kodikos_omadas, kodikos_ghpedou));
    conn.commit()
    window.destroy();

def insertedreveiform():
    root1 = Tk();
    root1.title("EDREVEI FORM");
    root1.configure(background="white");
    fields = ("kodikos_omadas", "kodikos_ghpedou");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertedrevei(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertdieuthinetai(t, window):
    arithmos_diaititi = t['arithmos_diaititi'].get();
    arithmos_agonistikis = t['arithmos_agonistikis'].get();

    conn.execute("INSERT INTO DIEUTHINETAI VALUES(?, ?);",
                 (arithmos_diaititi, arithmos_agonistikis));
    conn.commit()
    window.destroy();

def insertdieuthinetaiform():
    root1 = Tk();
    root1.title("DIEUTHINETAI FORM");
    root1.configure(background="white");
    fields = ("arithmos_diaititi", "arithmos_agonistikis");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertdieuthinetai(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def insertprokiptei(t, window):
    arithmos_agonistikis = t['arithmos_agonistikis'].get();
    arithmos_timorias = t['arithmos_timorias'].get();

    conn.execute("INSERT INTO PROKIPTEI VALUES(?, ?);",
                 ( arithmos_agonistikis,arithmos_timorias));
    conn.commit()
    window.destroy();

def insertprokipteiform():
    root1 = Tk();
    root1.title("PROKIPTEI FORM");
    root1.configure(background="white");
    fields = ( "arithmos_agonistikis","arithmos_timorias");
    ents = makeform(root1, fields);
    b1 = Button(root1, text='Submit',
                command=(lambda: insertprokiptei(ents, root1)));
    b1.pack(side=TOP, padx=5, pady=5);

def q0():
    root1 = Tk();
    root.title("LOCAL CHAMPIONSHIP DB");
    root1.configure(background="white");

    b1 = Button(root1, text='Insert Podosfairistis', command=(lambda: insertpodosfairistiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Omada', command=(lambda: insertomadaform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Paizei', command=(lambda: insertpaizeiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Proponitis', command=(lambda: insertpropnhthsform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Ghpedo', command=(lambda: insertghpedoform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Agonas', command=(lambda: insertagonasform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Diaititis', command=(lambda: insertdiaititisform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Timoria', command=(lambda: inserttimoriaform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Simetexei', command=(lambda: insertsimetexeiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Skorarei', command=(lambda: insertskorareiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Proponeitai', command=(lambda: insertproponeitaiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Edrevei', command=(lambda: insertedreveiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Dieuthinetai ', command=(lambda: insertdieuthinetaiform()));
    b1.pack(side=TOP, padx=5, pady=5);

    b1 = Button(root1, text='Insert Prokiptei ', command=(lambda: insertprokipteiform()));
    b1.pack(side=TOP, padx=5, pady=5);

def q1():
    root1 = Tk();
    root1.title("All Scorers");
    root1.configure(background="white");
    tree = ttk.Treeview(root1, column=("c1", "c2", "c3"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Name")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Arithmos Adeias")

    cur1 = conn.cursor()
    cur1.execute("SELECT DISTINCT p.name,s.arithmos_adeias FROM PODOSFAIRISTIS as p JOIN SKORAREI as s on s.arithmos_adeias=p.arithmos_adeias  "
                 "ORDER BY s.arithmos_adeias;")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    tree.pack()


def q2():
    root1 = Tk();
    root1.title("More home goals");
    root1.configure(background="white");
    tree = ttk.Treeview(root1, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="entos_edras_omada")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="skor_entos_edras_omada")
    cur1 = conn.cursor()
    cur1.execute("SELECT entos_edras_omada,sum(skor_entos_edras_omada) FROM AGONAS as a  JOIN SKORAREI as s on s.arithmos_agonistikis=a.arithmos_agonistikis "
                 "ORDER BY entos_edras_omada,skor_entos_edras_omada DESC;")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    tree.pack()

def q3():
    root1 = Tk();
    root1.title("More away goals");
    root1.configure(background="white");
    tree = ttk.Treeview(root1, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="ektos_edras_omada")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="skor_ektos_edras_omada")
    cur1 = conn.cursor()
    cur1.execute("SELECT ektos_edras_omada,sum(skor_ektos_edras_omada) FROM AGONAS as a  JOIN SKORAREI as s on s.arithmos_agonistikis=a.arithmos_agonistikis "
                 "ORDER BY skor_ektos_edras_omada DESC")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    tree.pack()

def q4():
    root1 = Tk();
    root1.title("All Matches");
    root1.configure(background="white");
    tree = ttk.Treeview(root1, column=("c1", "c2", "c3"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Entos")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Ektos")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Hmerominia")
    cur1 = conn.cursor()
    cur1.execute("SELECT entos_edras_omada,ektos_edras_omada,hmirominia FROM AGONAS")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    tree.pack()

def q5():
    root1 = Tk();
    root1.title("All punishment");
    root1.configure(background="white");
    tree = ttk.Treeview(root1, column=("c1", "c2", "c3","c4"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="arithmos_timorias")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="eidos")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="kodikos_podosfairisti")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="name")
    cur1 = conn.cursor()
    cur1.execute("SELECT arithmos_timorias,eidos,kodikos_podosfairisti,name FROM TIMORIA as t JOIN PODOSFAIRISTIS as p on t.kodikos_podosfairisti=p.arithmos_adeias")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    tree.pack()


conn = sqlite3.connect("C:\\Users\\herod\\Desktop\\DB Browser for SQLite\\localchampionship.db");
root = Tk();

root.title("LOCAL CHAMPIONSHIP DB");
root.configure(background="white");

b1 = Button(root, text='Insert Data', command=(lambda: q0()));
b1.pack(side=TOP, padx=5, pady=5);

b2 = Button(root, text='All Scorers', command=(lambda: q1()));
b2.pack(side=TOP, padx=5, pady=5);

b2 = Button(root, text='More home goals', command=(lambda: q2()));
b2.pack(side=TOP, padx=5, pady=5);

b2 = Button(root, text='More away goals', command=(lambda: q3()));
b2.pack(side=TOP, padx=5, pady=5);

b2 = Button(root, text='All Matches', command=(lambda: q4()));
b2.pack(side=TOP, padx=5, pady=5);

b2 = Button(root, text='All punishment', command=(lambda: q5()));
b2.pack(side=TOP, padx=5, pady=5);

btnexit = Button(root, text='Quit', command=(lambda: closeall()));
btnexit.pack(side=TOP, padx=5, pady=5);

root.mainloop();
