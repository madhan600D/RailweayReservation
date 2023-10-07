#5 confirmed ticket ,3 RAC,2 waiting list

class Railway:
    #data_base
    confirmed={'hari':['hari',22,'male','yes'],'mari':['mari',21,'female','yes'],
               'bari':['bari',32,'male','no']}
    Rac={'madi':['madi',22,'male','yes'],'Aathi':['Aathi',32,'male','yes'],'pranav':['pranav',24,'male','no']}
    waiting={'sini':['sini',22,'female','yes']}
    total_booked=6
    total_available=8-total_booked
    underage={}
    #data_base
    def __init__(self):
        print("1.Book a ticket\n2.cancel your ticket\n3.print booked ticket\n4.Print available tickets")
        inp=int(input("Enter a command:"))
        if(inp==1):
            self.book()
        elif(inp==2):
            val=str(input("Enter the name:"))
            self.cancel(val)
        elif(inp==3):
            name=str(input("Enter receipient name: "))
            self.PrintRecipt(name)
        elif(inp==4):
            self.available()
        else:
            print("Enter a valid command")
            self.__init__()
    def mover(self):
        #this method moves waiting to RAC
        print("method called")
        if(len(self.confirmed) < 3 and len(self.Rac)>0):
            for key,value in self.Rac.items():
                self.confirmed[key]=value
                del self.Rac[key]
                print(self.confirmed)
                break
        if(len(self.Rac)<3 and len(self.waiting)>0):
                for key,value in self.waiting.items():
                    self.Rac[key]=value
                    del self.waiting[key]
                    print(self.Rac)
                    break
        print(self.waiting)
        self.__init__()
    def Data_adder(self,data):
        if(int(data[1])<=5):
            self.underage[data[0]]=data
            self.total_booked+=1
        else:
            if(len(self.confirmed)<3):
                self.confirmed[data[0]]=data
            else:
                if(len(self.Rac)<2):
                    self.Rac[data[0]]=data
                elif(len(self.waiting)<2):
                    self.waiting[data[0]]=data 
            self.total_booked+=1
        print(self.waiting)
    def book(self):
        temp=[]
        if(len(self.waiting)<2):
            name=str(input("Enter Your Name"))
            age=str(input("Enter Your age"))
            gender=str(input("Enter Your gender"))
            berth=str(input("Enter berth Yes/No"))
            if(berth=="yes" or berth=="no"):
                temp.append(name)
                temp.append(age)
                temp.append(gender)
                temp.append(berth)
                self.Data_adder(temp)
            else:
                print("enter valid berth details")
            self.__init__()
        else:
            print("tickets Not available")
            self.__init__()
        
    def cancel(self,value):
        if(value in self.confirmed):
            del self.confirmed[value]
            print("Removed sucessfully")
            self.mover()
        elif(value in self.Rac):
            del self.Rac[value]
            print("Removed sucessfully")
            self.mover()
        elif(value in self.waiting):
            del self.waiting[value]   
            self.mover()
        else:
            print("Enter a valid name to cancel")
            self.__init__()
    def PrintRecipt(self,val):
        if(val in self.confirmed):
            print("Your recipt is:\n")
            for key,value in self.confirmed.items():
                if(key==val):
                    for i in range(len(value)):
                        if(i==0):
                            print(f"Name of the booker:{value[0]}")
                        if(i==1):
                            print(f"Age of the booker:{value[1]}")
                        if(i==2):
                            print(f"Gender of the booker:{value[2]}")
                        if(i==3):
                            print(f"Berth yes/no:{value[3]}")
            if(val in self.Rac):
                print("Your recipt is:\n")
                for key,value in self.Rac.items():
                    if(key==val):
                        for i in range(len(value)):
                            if(i==0):
                                print(f"Name of the booker:{value[0]}")
                            if(i==1):
                                print(f"Age of the booker:{value[1]}")
                            if(i==2):
                                print(f"Gender of the booker:{value[2]}")
                            if(i==3):
                                print(f"Berth yes/no:{value[3]}")
                print("you are currently allotted to RAC")
        if(val in self.waiting):
            print("Your recipt is:\n")
            for key,value in self.waiting.items():
                if(key==val):
                    for i in range(len(value)):
                        if(i==0):
                            print(f"Name of the booker:{value[0]}")
                        if(i==1):
                            print(f"Age of the booker:{value[1]}")
                        if(i==2):
                            print(f"Gender of the booker:{value[2]}")
                        if(i==3):
                            print(f"Berth yes/no:{value[3]}")
            print("you are currently in waiting stage")
        self.__init__()
    def available(self):
        print(f"Number of available tickets are:{self.total_available}")
train=Railway()
