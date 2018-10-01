import MySQLdb

db = MySQLdb.connect(host="localhost",user="",passwd="",db="")

cur = db.cursor()

platform = raw_input('Enter language: ')

cur.execute("SELECT * FROM platforms WHERE language = '%s';" % platform)

#fix error
#cur.execute("SELECT * FROM platforms WHERE language = %s;", (platform,))

for row in cur.fetchall():
	print (row)

db.close()