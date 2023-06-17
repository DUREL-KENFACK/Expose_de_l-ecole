from tkinter import *
from creation_base import *
fen1=Tk()
fen1.title("enregistrement")
Label(text="Nom : ").grid(row=0, padx=10 , pady=10 ,sticky=W)
entre1=Entry()
entre1.grid(row=0, column=1)

Label(text="Prenom :").grid(row=1,padx=10 , pady=10 , sticky=W)
entre2=Entry()
entre2.grid(row=1, column=1)

Label(text="Sexe : ").grid(row=2,padx=10 , pady=10 , sticky=W)
entre3=Entry()
entre3.grid(row=2, column=1)

Label(text="tel:                    ").grid(row=3,padx=10 , pady=10 , sticky=W)
entre4=Entry()
entre4.grid(row=3, column=1)

Label(text="date naissance :").grid(row=4,padx=10 , pady=10 , sticky=W)
entre5=Entry()
entre5.grid(row=4, column=1)

Label(text="Age :").grid(row=5, padx=10 , pady=10 , sticky=W)
entre6=Entry()
entre6.grid(row=5, column=1)
fram=Frame(fen1, width=200, height=20)
fram.grid(row=6, column=0, columnspan=2)
chaine=Label(fram, bg='blue')
chaine.grid()
def recup():
    global age, date, tel, sexe, prenom, nom, req, val
    age=entre6.get()
    date=entre5.get()
    tel=entre4.get()
    sexe=entre3.get()
    prenom=entre2.get()
    nom=entre1.get()
    sql="INSERT INTO patient(nom,prenom,sexe,tel,date,age) VALUES(%s,%s,%s,%s,%s,%s) "
    val=(nom,prenom,sexe,tel,date,age)
    mycursor.execute(sql,val)
    mydb.commit()
    chaine.configure(text="les information ont ete ajouter")
    mydb.close()
bout1=Button(fen1, text="Enregistrer", command=recup)
bout1.grid(padx=100)

fen1.mainloop()