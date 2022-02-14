import sqlite3
conn=sqlite3.connect('exercise.db')
c= conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS movies(
        name text,
        director text,
        actor text,
        actress text,
        year_of_release text)""")
records = [('Iron Man','Jon Favreau','Robert D. Junior','Gwyneth Paltrow','2008'),
			('The Incredible Hulk','Louis Leterrier','Edward Norton ','Liv Tyler','2008'),
			('Iron Man 2','Jon Favreau','Robert D. Junior','Gwyneth Paltrow','2010'),
			('Thor','Kenneth Branagh','Chris Hemsworth','Natalie Portman','2011'),
			('Captain America: The First Avenger','Joe Johnston','Chris Evans','Hayley Atwell','2011'),
			('Iron Man 3','Shane Black','Robert D. Junior','Gwyneth Paltrow','2013'),
			('Thor:The Dark World','Alan Taylor','Chris Hemsworth','Natalie Portman','2013'),
			('Captain America: The Winter Soldier','Russo Brothers','Chris Evans','Scarlett Johansson','2014'),
			('Guardians of the Galaxy','James Gunn','Chris Pratt','Zoe Saldana','2014'),
			('Ant Man','Peyton Reed','Paul Rudd','Evangeline Lilly','2015'),
			('Captain America: Civil War','Russo Brothers','Chris Evans','Scarlett Johansson','2016'),
			('Doctor Strange','Scott Derrickson','Benedict Cumberbatch','Rachel McAdams','2016'),
			('Guardians of the Galaxy Vol. 2','James Gunn','Chris Pratt','Zoe Saldana','2017'),
			('Spider-Man: Homecoming','Jon Watts','Tom Holland','Zendaya','2017'),
			('Thor:Ragnarok','Taika Watiti','Chris Hemsworth','Tessa Thompson','2017'),
			('Black Panther','Ryan Coogler','Chadwick Boseman','Lupita Nyongo','2018'),
			('Ant Man and the Wasp','Peyton Reed','Paul Rudd','Evangeline Lilly','2018'),
			('Captain Marvel','Anna Boden and Ryan Fleck','Samuel L. Jackson' ,'Brie Larson','2019'),
			('Spider-Man: Far From Home','Jon Watts','Tom Holland','Zendaya','2019')
			]
c.execute("SELECT * FROM movies")
records1 = c.fetchall()
if not records1:
	c.executemany("INSERT INTO movies VALUES(?,?,?,?,?);",records)
	#print('We have inserted', c.rowcount, 'records to the table.')
for row in records1:
	print("Movie :", row[0],", Director :",row[1],", actor :",row[2],", actress:",row[3],", release year:",row[4])
	print("\n")

actor_input=input("Enter the name of actor :")
c.execute("SELECT * FROM movies WHERE actor =?",(actor_input,))
records2 = c.fetchall()
if not records2:
	print("No records found for this actor")
else:
	print("Following details are found for ",actor_input,":")
	for row in records2:
		print("Movie :", row[0],", Director :",row[1],", actress:",row[3],", release year:",row[4])
		print("\n")
conn.commit()
conn.close()