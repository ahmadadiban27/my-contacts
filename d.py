import sqlite3
class Inputdata :
    def __init__(self ,db):
        self.con= sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Phonbook(id INTEGER PRIMARY KEY , fname text , lname text , address text , phone text)")
        self.con.commit()
    def insert(self,fname , lname , address , phone):
        self.cur.execute("INSERT INTO Phonbook VALUES(NULL ,?,?,?,?)",(fname , lname ,address, phone))
        self.con.commit()

    def remove(self , id):
        self.cur.execute('DELETE FROM Phonbook WHERE id=? ' , (id,))
        self.con.commit()
        
    def select(self):
        self.cur.execute('SELECT * FROM Phonbook')
        rows=self.cur.fetchall()
        return rows
    
    def update(self, id ,fname,lname,address , phone):
        self.cur.execute('UPDATE Phonbook  SET fname=? , lname = ? , address = ? , phone = ? WHERE id=? ' ,( lname , fname , address , phone , id))
        self.con.commit()
        
    def search(self ,y , x):
        self.cur.execute(f'SELECT * FROM Phonbook WHERE {y} like ?', (x,))
        rsearch = self.cur.fetchall()
        return rsearch
    