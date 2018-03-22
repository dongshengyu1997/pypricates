import random
import mysql.connector
def support():
    suplist = []
    for i in range(20):
        listcode = ''
        for n in range(3):
            listcode += str(random.randint(0, 10))
        for n1 in range(4):
            listcode += str(chr(random.randint(65,90)))
        for n2 in range(3):
            listcode += str(random.randint(0,10))
        suplist.append(listcode)
    return suplist
if __name__ == '__main__':
    suplist = support()
    conn = mysql.connector.connect(user='root', password='dong1997', database='prictise2')
    cour = conn.cursor()
    for i in range(20):
        cour.execute("INSERT INTO py3 VALUES (%d,\'%s\')"%(i,suplist[i]))
    cour.close()
    conn.commit()
    conn.close
    print(suplist)