#ASSUME THAT ALL STOPS CHUMMA EXISTS WITH NO ROUTE CREATED FOR IT

import ibm_db
import sys
import ibm_db
conn = ibm_db.connect("TGMC1","sriram","1234")

def zins():
	sql="SELECT MAX(ROUTEID) AS MAX FROM ROUTEDB"
	print "Generating key for RouteDB"
	stmt=ibm_db.exec_immediate(conn,sql)
	prevID=ibm_db.fetch_assoc(stmt)
	ID = str(prevID['MAX'] + 1)
	routename = '47B'
	sql="SELECT CID FROM CLASS WHERE MODEID = 1"
	stmt=ibm_db.exec_immediate(conn,sql)
	a=True
	classes=[]
	while a != False:
		a = ibm_db.fetch_assoc(stmt)
		if a != False:
			classes.append(a)
	a=''
	for i in classes:
		a = a + ',CID_' + str(i['CID']) + " INTEGER"
	a=a.replace(",","",1)
	sql = "CREATE TABLE ROUTE_" + routename + "(STOPID INTEGER NOT NULL PRIMARY KEY," + a + ",FOREIGN KEY(STOPID) REFERENCES STOPS)"
	ibm_db.exec_immediate(conn,sql)
	print "Route_" + routename + " table created successfully.."
	#ADditional code: Insert values into route_<id> table
	sqli="INSERT INTO ROUTE_" + routename + " VALUES(1,1,1)"
	ibm_db.exec_immediate(conn,sqli)
	print "value inserted..."
	sqli="INSERT INTO ROUTE_" + routename + " VALUES(2,1,1)"
	ibm_db.exec_immediate(conn,sqli)
	print "value inserted..."
	sqli="INSERT INTO ROUTE_" + routename + " VALUES(4,1,1)"
	ibm_db.exec_immediate(conn,sqli)
	print "value inserted..."
	sqli="INSERT INTO ROUTE_" + routename + " VALUES(5,1,1)"
	ibm_db.exec_immediate(conn,sqli)
	print "value inserted..."
	#ADditional code: Insert values into route_<id> table
	sql="SELECT STOPID FROM ROUTE_" + routename
	stmt=ibm_db.exec_immediate(conn,sql)
	a=True
	stops = []
	while a != False:
		a = ibm_db.fetch_assoc(stmt)
		if a != False:
			stops.append(a)
	a=''
	for i in stops:
		a = a + ',STOP_' + str(i['STOPID']) + " TIME"
	a = a.replace(",","",1)
	sqlF="CREATE TABLE F_" + routename + "(TRIPID INTEGER,CID INTEGER," + a + ",COUNT INTEGER, FOREIGN KEY(CID) REFERENCES CLASS)"
	sqlR="CREATE TABLE R_" + routename + "(TRIPID INTEGER,CID INTEGER," + a + ",COUNT INTEGER, FOREIGN KEY(CID) REFERENCES CLASS)"
	ibm_db.exec_immediate(conn,sqlF)
	print "Forward journey table created.."
	ibm_db.exec_immediate(conn,sqlR)
	print "Return journey table created.."
	#cleanup
	sqlterm="INSERT INTO ROUTEDB VALUES(" + ID + ",'" + routename + "'," + "1)"
	ibm_db.exec_immediate(conn,sqlterm)
	print "All formalities completed successfully. Route successfully registered with database..."
	
zins()
