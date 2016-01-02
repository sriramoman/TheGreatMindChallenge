import ibm_db
import sys
import ibm_db

source = int(sys.argv[1])
dest = int(sys.argv[2])
stmt=ibm_db.exec_immediate(conn,sql)
a=True
b=[]
while a != False:
     a = ibm_db.fetch_assoc(stmt)
     if a != False:
             b.append(a)

