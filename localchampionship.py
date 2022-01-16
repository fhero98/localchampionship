import	sqlite3;	
from	tkinter	import	*	
from	tkinter	import	ttk
def makeform(root,	fields):	
			entries	=	{};	
			for	field	in	fields:	
						row	=	Frame(root);	
						lab	=	Label(row,	
						width=12,	text=field+":	",	anchor='w');	
						ent	=	Entry(row);	
						ent.insert(0,"0");	
						row.pack(side	=	TOP,	fill	=	X,	padx	=	5	,	pady	=	5);	
						lab.pack(side	=	LEFT);	
						ent.pack(side	=	RIGHT,	expand	=	YES,	fill	=	X);	
						entries[field]	=	ent;	
			return	entries;
			
def closeall():	
			conn.commit();	
			conn.close();	
			root.quit();
def inserttuple(t):	
			first	=	t['First	Name'].get();	
			last	=	t['Last	Name'].get();	
			afm	=	int(t['AFM'].get());	
			sex	=	t['Sex'].get();	
			salary	=	int(t['Salary'].get());	
			superafm	=	int(t['Supervisor'].get());	
			dept	=	t['Department'].get();	
			conn.execute(‘’’’ INSERT	INTO	EMPLOYEE	
	 	 VALUES(?,	?,	?,	?,	?,	?,	?);’’’,	
	 	(first,	last,	afm,	sex,	salary,	superafm,	dept));	
conn	=	sqlite3.connect("DBCourse.db");			root	=	Tk();
root.title("EMPLOYEE	FORM");	
root.configure(background	=	"white");	
fields	=	("First	Name",	"Last	Name",	"AFM",	"Sex",	
				"Salary",	"Supervisor",	"Department");	
ents	=	makeform(root,	fields);	
b1	=	Button(root,	text	=	'Submit',	
command=(lambda:	inserttuple(ents)))	;	
b1.pack(side	=	LEFT,	padx	=	5,	pady	=	5);	
b2	=	Button(root,	text	=	'Quit',	
command=(lambda:	closeall()));	
b2.pack(side	=	LEFT,	padx	=	5,	pady	=	5);		
root.mainloop();