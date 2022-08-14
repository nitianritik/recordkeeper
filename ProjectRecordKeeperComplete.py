
###############################
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import time
from typing import Pattern
import pymysql
import random
# import pandas

from tkinter import font 


root = Tk()
root.title('Project Record Keeper')
root.config(bg='gold2')
root.geometry('1174x700+200+150')
# root.iconbitmap('ICON.ico')
root.resizable(False,False)
############################## Connect Database
#_________________ALL FUNCTIONST___________________#

def addproject():
    
      def submitadd():
            scholar = scholarval.get()
            studentname=studentnameval.get()
            projectname =  projectnameval.get()
            minimarks =  minimarksval.get()
            midmarks = midmarksval.get()
            endmarks = endmarksval.get()
            status = statusval.get()
            description = descriptionval.get()
            supervisor =  supervisornameval.get()
            addeddate = time.strftime("%d/%m/%Y")
            addedtime = time.strftime("%H:%M:%S")

            try:
                strr = 'insert into projectsdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr,(scholar,studentname,projectname,minimarks,midmarks,endmarks,status,description,supervisor,addeddate,addedtime))
                con.commit()
                res = messagebox.askyesnocancel('Notification','scholar {} Name {} Added Sucessfully... and want to clean the form'.format(scholar,studentname),parent=addroot)

                if(res==True):
                    scholarval.set('')
                    projectnameval.set('')
                    studentnameval.set('')
                    minimarksval.set('')
                    midmarksval.set('')
                    endmarksval.set('')
                    statusval.set('')
                    descriptionval.set('')
                    supervisornameval.set('')
                    
            except:
                messagebox.showerror('Notification','Scholar No already exist. Please Enter another or update that one...',parent=addroot)
            
            strr = 'select * from projectsdata;'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            projecttable.delete(*projecttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                projecttable.insert('',END,values=vv)
               # print(vv)




      addroot= Toplevel(master=DataEntryFrame)
      addroot.grab_set()
      addroot.geometry('470x600+220+200')
      addroot.title('Add New Project Record')
      addroot.config(bg="blue")
    #   addroot.iconbitmap('ICON.ico')
      addroot.resizable(False,False)
      #____ 1. ADD LABELS ____
      
      scholarlabel = Label(addroot,text='Scholar No. : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      scholarlabel.place(x=10,y=10)

      studentnamelabel = Label(addroot,text='Student Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      studentnamelabel.place(x=10,y=70)

      projectnamelabel = Label(addroot,text='Project Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      projectnamelabel.place(x=10,y=130)

      minimarkslabel = Label(addroot,text='Mini Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      minimarkslabel.place(x=10,y=190)

      midtermmarkslabel = Label(addroot,text='Mid Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      midtermmarkslabel.place(x=10,y=250)

      endtermmarkslabel = Label(addroot,text='End Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      endtermmarkslabel.place(x=10,y=310)

      statuslabel = Label(addroot,text='Status : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      statuslabel.place(x=10,y=370)

      descriptionlabel = Label(addroot,text='Description  : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      descriptionlabel.place(x=10,y=430)

      supervisornamelabel = Label(addroot,text='Supervisor : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      supervisornamelabel.place(x=10,y=490)

      #____ 1. ADD Entry Boxes ____
    
      scholarval= StringVar()
      studentnameval= StringVar()
      projectnameval= StringVar()
      minimarksval= StringVar()
      midmarksval= StringVar()
      endmarksval= StringVar()
      statusval= StringVar()
      descriptionval= StringVar()
      supervisornameval= StringVar()
      

      scholarentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=scholarval)
      scholarentry.place(x=250,y=10)

      studentnameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=studentnameval)
      studentnameentry.place(x=250,y=70)
      
      projectnameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=projectnameval)
      projectnameentry.place(x=250,y=130)
      
      minimarksentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=minimarksval)
      minimarksentry.place(x=250,y=190)
      
      midmarksentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=midmarksval)
      midmarksentry.place(x=250,y=250)
      
      endmarksentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=endmarksval)
      endmarksentry.place(x=250,y=310)
      
      statusentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=statusval)
      statusentry.place(x=250,y=370)
      
      descriptionentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=descriptionval)
      descriptionentry.place(x=250,y=430)
      
      supervisorentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=supervisornameval)
      supervisorentry.place(x=250,y=490)
      
      
     ###### ADD KA BUTTON ######
      submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
      submitbtn.place(x=150,y=550)

      addroot.mainloop()


#__________________________________________________________________________________________________________________________________

def searchproject():
      def search():
            scholar = scholarval.get()
            studentname=studentnameval.get()
            projectname =  projectnameval.get()
            minimarks =  minimarksval.get()
            midmarks = midmarksval.get()
            endmarks = endmarksval.get()
            status = statusval.get()
            description = descriptionval.get()
            supervisor =  supervisornameval.get()
            addeddate = time.strftime("%d/%m/%Y")



            if(scholar != ''):
                strr = 'select * from projectsdata where scholarno=%s'
                mycursor.execute(strr,(scholar))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)
                      

            elif(studentname != ''):
                strr = 'select * from projectsdata where studentname=%s'
                mycursor.execute(strr,(studentname))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)

            elif(projectname != ''):
                strr = 'select * from projectsdata where projectname=%s'
                mycursor.execute(strr,(projectname))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)                      


                      

            elif(minimarks != ''):
                strr = 'select * from projectsdata where minimarks=%s'
                mycursor.execute(strr,(minimarks))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      

            elif(midmarks != ''):
                strr = 'select * from projectsdata where midmarks=%s'
                mycursor.execute(strr,(midmarks))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      

            elif(endmarks != ''):
                strr = 'select * from projectsdata where endmarks=%s'
                mycursor.execute(strr,(endmarks))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      




                      

            elif(status != ''):
                strr = 'select * from projectsdata where status=%s'
                mycursor.execute(strr,(status))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      

            elif(description != ''):
                strr = 'select * from projectsdata where description=%s'
                mycursor.execute(strr,(description))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      

            elif(supervisor != ''):
                strr = 'select * from projectsdata where supervisorname=%s'
                mycursor.execute(strr,(supervisor))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)


                      

            elif(addeddate != ''):
                strr = 'select * from projectsdata where date=%s'
                mycursor.execute(strr,(addeddate))
                datas = mycursor.fetchall()
                projecttable.delete(*projecttable.get_children())
                for i in datas:
                      vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                      projecttable.insert('',END,values=vv)




      searchroot= Toplevel(master=DataEntryFrame)
      searchroot.grab_set()
      searchroot.geometry('470x670+220+200')
      searchroot.title('Add New Project Record')
      searchroot.config(bg="firebrick1")
    #   searchroot.iconbitmap('ICON.ico')
      searchroot.resizable(False,False)
      #____ 1. ADD LABELS ____
      
      scholarlabel = Label(searchroot,text='Scholar No. : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      scholarlabel.place(x=10,y=10)

      studentnamelabel = Label(searchroot,text='Student Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      studentnamelabel.place(x=10,y=70)

      projectnamelabel = Label(searchroot,text='Project Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      projectnamelabel.place(x=10,y=130)

      minimarkslabel = Label(searchroot,text='Mini Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      minimarkslabel.place(x=10,y=190)

      midtermmarkslabel = Label(searchroot,text='Mid Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      midtermmarkslabel.place(x=10,y=250)

      endtermmarkslabel = Label(searchroot,text='End Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      endtermmarkslabel.place(x=10,y=310)

      statuslabel = Label(searchroot,text='Status : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      statuslabel.place(x=10,y=370)

      descriptionlabel = Label(searchroot,text='Description : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      descriptionlabel.place(x=10,y=430)

      supervisornamelabel = Label(searchroot,text='Supervisor : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      supervisornamelabel.place(x=10,y=490)

      datelabel = Label(searchroot,text='Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      datelabel.place(x=10,y=550)

      #____ 1. ADD Entry Boxes ____
    
      scholarval= StringVar()
      studentnameval= StringVar()
      projectnameval= StringVar()
      minimarksval= StringVar()
      midmarksval= StringVar()
      endmarksval= StringVar()
      statusval= StringVar()
      descriptionval= StringVar()
      supervisornameval= StringVar()
      dateval= StringVar()
      
      
      scholarentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=scholarval)
      scholarentry.place(x=250,y=10)

      studentnameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=studentnameval)
      studentnameentry.place(x=250,y=70)
      
      projectnameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=projectnameval)
      projectnameentry.place(x=250,y=130)
      
      minimarksentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=minimarksval)
      minimarksentry.place(x=250,y=190)
      
      midmarksentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=midmarksval)
      midmarksentry.place(x=250,y=250)
      
      endmarksentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=endmarksval)
      endmarksentry.place(x=250,y=310)
      
      statusentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=statusval)
      statusentry.place(x=250,y=370)
      
      descriptionentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=descriptionval)
      descriptionentry.place(x=250,y=430)
      
      supervisorentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=supervisornameval)
      supervisorentry.place(x=250,y=490)

      dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
      dateentry.place(x=250,y=550)
      
      
      
     ###### SEARCH KA BUTTON ######
      submitbtn=Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
      submitbtn.place(x=150,y=620)

      searchroot.mainloop()


#__________________________________________________________________________________________________________________________________


def deleteproject():
    cc=projecttable.focus()
    content = projecttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from projectsdata where scholarno=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Scholar no = {} deleted sucessfully...'.format(pp))

    strr = 'select * from projectsdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    projecttable.delete(*projecttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
        projecttable.insert('',END,values=vv)




#__________________________________________________________________________________________________________________________________


def updateproject():
      def update():
            scholar = scholarval.get()
            studentname=studentnameval.get()
            projectname =  projectnameval.get()
            minimarks =  minimarksval.get()
            midmarks = midmarksval.get()
            endmarks = endmarksval.get()
            status = statusval.get()
            description = descriptionval.get()
            supervisor =  supervisornameval.get()
            date = dateval.get()
            time = timeval.get()

            strr = 'update projectsdata set studentname=%s,projectname=%s,minimarks=%s,midmarks=%s,endmarks=%s,status=%s,description=%s,supervisorname=%s,date=%s,time=%s where scholarno=%s'
            mycursor.execute(strr,(studentname,projectname,minimarks,midmarks,endmarks,status,description,supervisor,date,time,scholar))
            con.commit()
            messagebox.showinfo('Notification','Scholar no = {} Updated sucessfully...'.format(scholar),parent=updateroot)
            strr = 'select * from projectsdata'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            projecttable.delete(*projecttable.get_children())
            for i in datas:
                  vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                  projecttable.insert('',END,values=vv)
            updateroot.destroy()



      updateroot= Toplevel(master=DataEntryFrame)
      updateroot.grab_set()
      updateroot.geometry('470x730+220+200')
      updateroot.title('Add New Project Record')
      updateroot.config(bg="firebrick1")
    #   updateroot.iconbitmap('ICON.ico')
      updateroot.resizable(False,False)
      #____ 1. ADD LABELS ____
      
      scholarlabel = Label(updateroot,text='Scholar No. : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      scholarlabel.place(x=10,y=10)

      studentnamelabel = Label(updateroot,text='Student Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      studentnamelabel.place(x=10,y=70)

      projectnamelabel = Label(updateroot,text='Project Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      projectnamelabel.place(x=10,y=130)

      minimarkslabel = Label(updateroot,text='Mini Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      minimarkslabel.place(x=10,y=190)

      midtermmarkslabel = Label(updateroot,text='Mid Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      midtermmarkslabel.place(x=10,y=250)

      endtermmarkslabel = Label(updateroot,text='End Term Marks : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      endtermmarkslabel.place(x=10,y=310)

      statuslabel = Label(updateroot,text='Status : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      statuslabel.place(x=10,y=370)

      descriptionlabel = Label(updateroot,text='Desctiption : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      descriptionlabel.place(x=10,y=430)

      supervisornamelabel = Label(updateroot,text='Supervisor : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      supervisornamelabel.place(x=10,y=490)

      datelabel = Label(updateroot,text='Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      datelabel.place(x=10,y=550)

      timelabel = Label(updateroot,text='Time : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor="w")
      timelabel.place(x=10,y=610)

      #____ 1. ADD Entry Boxes ____
    
      scholarval= StringVar()
      studentnameval= StringVar()
      projectnameval= StringVar()
      minimarksval= StringVar()
      midmarksval= StringVar()
      endmarksval= StringVar()
      statusval= StringVar()
      descriptionval= StringVar()
      supervisornameval= StringVar()
      dateval= StringVar()
      timeval= StringVar()
      
      
      scholarentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=scholarval)
      scholarentry.place(x=250,y=10)

      studentnameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=studentnameval)
      studentnameentry.place(x=250,y=70)
      
      projectnameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=projectnameval)
      projectnameentry.place(x=250,y=130)
      
      minimarksentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=minimarksval)
      minimarksentry.place(x=250,y=190)
      
      midmarksentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=midmarksval)
      midmarksentry.place(x=250,y=250)
      
      endmarksentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=endmarksval)
      endmarksentry.place(x=250,y=310)
      
      statusentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=statusval)
      statusentry.place(x=250,y=370)
      
      descriptionentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=descriptionval)
      descriptionentry.place(x=250,y=430)
      
      supervisorentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=supervisornameval)
      supervisorentry.place(x=250,y=490)

      dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
      dateentry.place(x=250,y=550)

      timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
      timeentry.place(x=250,y=610)
      
      
      
      
      ###### UPDATE KA BUTTON ######
      submitbtn=Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
      submitbtn.place(x=150,y=680)

      cc=projecttable.focus()
      content = projecttable.item(cc)
      pp = content['values']
      if(len(pp) != 0 ):
          
                    scholarval.set(pp[0])
                    studentnameval.set(pp[1])
                    projectnameval.set(pp[2])
                    minimarksval.set(pp[3])
                    midmarksval.set(pp[4])
                    endmarksval.set(pp[5])
                    statusval.set(pp[6])
                    descriptionval.set(pp[7])
                    supervisornameval.set(pp[8])
                    dateval.set(pp[9])
                    timeval.set(pp[10])



      updateroot.mainloop()


#__________________________________________________________________________________________________________________________________


def showproject():
            strr = 'select * from projectsdata'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            projecttable.delete(*projecttable.get_children())
            for i in datas:
                  vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                  projecttable.insert('',END,values=vv)



#__________________________________________________________________________________________________________________________________



def exportproject():
    pass
    # ff= filedialog.asksaveasfilename()
    # gg=projecttable.get_children()
    # scholarno,studentname,projectname,minimarks,midmarks,endmarks,status,description,supervisorname,addeddate,addedtime=[],[],[],[],[],[],[],[],[],[],[]
    # for i in gg:
    #     content = projecttable.item(i)
    #     pp = content['values']
    #     scholarno.append(pp[0]),studentname.append(pp[1]),projectname.append(pp[2]),minimarks.append(pp[3]),midmarks.append(pp[4]),endmarks.append(pp[5]),status.append(pp[6]),description.append(pp[7]),supervisorname.append(pp[8]),addeddate.append(pp[9]),addedtime.append(pp[10])
           
    # dd = ['Scholar No.','Student Name','Project Name','Mini Marks','Mid Marks','End Marks','Status','Description','Supervisor Name','Added Time','Added Date']
    # df = pandas.DataFrame(list(zip(scholarno,studentname,projectname,minimarks,midmarks,endmarks,status,description,supervisorname,addeddate,addedtime)),columns=dd)
    
    # paths = r'{}.csv'.format(ff)
    # df.to_csv(paths,index=False)
    # messagebox.showinfo('Notification','Student data is saved {}'.format(paths))



#__________________________________________________________________________________________________________________________________



def exitt():
    res= messagebox.askyesnocancel('Alert','Do you want to exit')
    if(res==True):
        root.destroy()
    
    
#__________________________________________________________________________________________________________________________________




#__________________________________________________#


############################## Connect Database


def Connectdb():

    
    def submitdb():
        # global con,mycursor
        # host = hostval.get() ### localhost
        # user = userval.get()  #### root
        # password = passwordval.get()  ###Ritik@123



        global con,mycursor
        host = "localhost"
        user = "root"
        password = "985632"
       
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Alert','Data is incorrect, please try again',parent=dbroot)
            return

        try:
            strr='create database projectrecordkeeper3' 
            mycursor.execute(strr)
            strr='use projectrecordkeeper3'
            mycursor.execute(strr)
            strr='create table projectsdata(scholarno int,studentname varchar(40),projectname varchar(40),minimarks varchar(20),midmarks varchar(20),endmarks varchar(20),status varchar(60),description varchar(60),supervisorname varchar(30),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table projectsdata modify column scholarno int not null'
            mycursor.execute(strr)
            strr='alter table projectsdata modify column scholarno int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','DataBase Created ! Now you are connected to the DataBase...',parent=dbroot)


        except:
            strr='use projectrecordkeeper3'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the DataBase...',parent=dbroot)
        dbroot.destroy()



#projecttable = Treeview(ShowDataFrame,columns=('Scholar No.','Student Name','Project Name',"Mini marks",'Mid Marks','End marks','Status','Description','Supervisor Name','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    # dbroot.iconbitmap('ICON.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #.......................#Connect DB labels
   
    hostlabel=Label(dbroot,text="Enter Host : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel=Label(dbroot,text="Enter User : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel=Label(dbroot,text="Enter Password : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #.......................#Connect DB input Boxes

    hostval=StringVar()
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userval=StringVar()
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordval=StringVar()
    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #.......................#Connect (submit) Button

    submitbutton = Button(dbroot,text='Submit',bd=5,font=('roman',15,'bold'),width=20,bg='red',activebackground="blue",activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
 
 
##############################

def tick():
     time_string = time.strftime("%H:%M:%S")
     date_string = time.strftime("%d/%m/%Y")

    #  print(time_string)

     clock.config(text='Date :'+date_string+"\nTime : "+time_string)
     clock.after(200,tick)

######################## INTRO SLIDER


def IntroLableTick():
    global count,text
    if(count>=len(ss)):

         count = 0
         text =''
         SliderLable1.config(text=text)
    else:
        text = text+ss[count]
        SliderLable1.config(text=text)
        count+=1
    SliderLable1.after(200,IntroLableTick)


####################################   Frames

#.........................# Data Entry Frame intro


DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel=Label(DataEntryFrame,text='______WELCOME______',width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Project',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=addproject)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Project',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=searchproject)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Project',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=deleteproject)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Project',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=updateproject)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All Project',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=showproject)
showallbtn.pack(side=TOP,expand=True)

# exportbtn = Button(DataEntryFrame,text='6. Export Data',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=exportproject)
# exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='6. Exit',width='25',font=("chiller",20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground="white",command=exitt)
exitbtn.pack(side=TOP,expand=True)



#.........................# SHow data Frame
#.........................# SHow data Frame
#.........................# SHow data Frame
#.........................# SHow data Frame





ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

style=ttk.Style()
style.configure('Treeview.Heading',font=('default',10,'bold'),foreground="blue")
style.configure('Treeview',font=('default',10,'bold'),foreground="black",background='cyan')


scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

projecttable = Treeview(ShowDataFrame,columns=('Scholar No.','Student Name','Project Name',"Mini marks",'Mid Marks','End marks','Status','Description','Supervisor Name','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=projecttable.xview)
scroll_y.config(command=projecttable.yview)

projecttable.heading('Scholar No.',text='Scholar No.')
projecttable.heading('Student Name',text='Student Name')
projecttable.heading('Project Name',text='Project Name')
projecttable.heading('Mini marks',text='Mini marks')
projecttable.heading('Mid Marks',text='Mid Marks')
projecttable.heading('End marks',text='End marks')
projecttable.heading('Status',text='Status')
projecttable.heading('Description',text='Description')
projecttable.heading('Supervisor Name',text='Supervisor Name')
projecttable.heading('Added Date',text='Added Date')
projecttable.heading('Added Time',text='Added Time')

projecttable['show']='headings'

projecttable.column('Scholar No.',width=100)
projecttable.column('Student Name',width=100)
projecttable.column('Project Name',width=100)
projecttable.column('Mini marks',width=100)
projecttable.column('Mid Marks',width=100)
projecttable.column('End marks',width=100)
projecttable.column('Status',width=100)
projecttable.column('Description',width=100)
projecttable.column('Supervisor Name',width=100)
projecttable.column('Added Date',width=100)
projecttable.column('Added Time',width=100)



projecttable.pack(fill=BOTH,expand=1)
 


################################### Slider
ss='Welcome to Project Record Manager'
count =0
text = ''
#######
SliderLable1 = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=3,width=35,bg='cyan')
SliderLable1.place(x=260,y=0)
IntroLableTick()

#################################### Clock

clock =Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=3,bg='lawn green')
clock.place(x=0,y=0)
tick()

################################### Connect Database Button

connectbutton = Button(root,text='Connect to Dastabase',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,bg='green2',activebackground="blue",activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)

root.mainloop()



