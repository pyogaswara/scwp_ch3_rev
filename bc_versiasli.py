class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
        self.output=[]
        
    
    def __str__(self):
        category_title=self.name.center(30,"*")
        self.output.append(category_title)
        for i in range (0,len(self.ledger)):
            #print((self.ledger[i]["description"]))
            l=str((self.ledger[i]["description"])[:23])
            m=(" "*(23-len(self.ledger[i]["description"])))
            r=(str(('%.2f' % self.ledger[i]["amount"])).rjust(7))
            c=f'{l}{m}{r}'
            self.output.append(c)
        total=self.get_balance()
        nl='\n'
        z=f"{nl.join(str(x) for x in self.output)}\n"\
          f"Total: {total}"
        return z

    def check_funds(self,amount):
        funds=0
        for i in range (0,len(self.ledger)):
            funds=funds+self.ledger[i]["amount"]
        if funds > amount:       
            return True 
        else:
            return False
        
    def deposit(self,*deposit):
      len_deposit=len(deposit)
      amount=deposit[0]
      if len_deposit==2:
        description=deposit[1]
      else:
        description=""
        #self.ledger.append([description,amount])
      self.ledger.append({"amount":amount,"description":description})
      #print(self.ledger)
      
    def withdraw(self,*withdraw):
        withdrawn_amount=withdraw[0]
        len_withdraw=len(withdraw)
        if self.check_funds(withdrawn_amount):
            amount=(-1)*(withdraw[0])
            if len_withdraw==2:
                description=withdraw[1]
            else:
                description=""
            #self.ledger.append([description,amount])
            self.ledger.append({"amount":amount,"description":description})
            return True
        else:
            print("insufficient funds")
            return False

    def get_balance(self):
        self.balance=0
        for i in range (0,len(self.ledger)):
            self.balance=self.balance+self.ledger[i]["amount"]
        return self.balance

    def transfer(self,amount,category):
        if self.check_funds(amount):
            amount=(-1)*amount
            description=f'Transfer to {category.name}'
            #self.ledger.append([description,amount])
            self.ledger.append({"amount":amount,"description":description})
            destination_description=f'Transfer from {self.name}'
            destination_amount=amount*(-1)
            #category.ledger.append([destination_description,destination_amount])
            category.ledger.append({"amount":destination_amount,"description":destination_description})
            return True
        else:
            print("insufficient funds")
            return False

              

#Food=Category("Food")
#Clothing=Category("Clothing")

##transaction1=(1000,"initial deposit")
#transaction2=(1250,"second deposit")
#transaction3=(500,"thirddddddddddddd deposit")
##transaction4=(750,"jajan-jajan")
#transaction5=(450,"jajan terus")
#transaction6=(55,"jajan siomay")


#Food.deposit(1000,"initial deposit")
#Food.withdraw(750,"jajan-jajan")
#Food.transfer(175,"Clothing")

#Clothing.deposit(250,"initial deposit")
#Food.transfer(25,"Clothing")

#Food.check_funds(100)

#Clothing.check_funds(100)
#Clothing.transfer(275,"Food")
#Food.get_balance()
#Clothing.get_balance()


def create_spend_chart(charts):
    all_spend=[]
    portion_spend=[]
    spending_category=[]
    for s in range (0,len(charts)):
        category_name=charts[s].name
        spending_category.append(category_name)

    for i in range (0,len(charts)):
        category_name=charts[i].name
        spending_category[i]=[]
        for j in range(0,(len(charts[i].ledger))):
            spend=(charts[i].ledger[j][1])
            if spend < 0:                 
                spending_category[i].append(spend)
        total_spend_percategory=(sum(spending_category[i]))
        all_spend.append(total_spend_percategory)
    total_spend=sum(all_spend)

    for i in range(0,len(charts)):
        percentage=(all_spend[i]*10)//(total_spend)
        portion_spend.append(percentage)     


    category=charts
    percentage=["100|","90|","80|","70|","60|","50|","40|","30|","20|","10|","0|"]
    graph_height=[]
    for i in range (0,3):
        length_o=("o"*(int(portion_spend[i])+1)).rjust(11)
        graph_height.append(length_o)

    graph_position=[]
    for i in range(len(percentage)):
        graph_position.append([percentage[i].rjust(4)])
        for j in range(0,len(graph_height)):
            graph_position[i].append((graph_height[j][i]))

    nl='\n'
    graph=f"{nl.join((str(' '.join(str(y).center(2) for y in x))) for x in graph_position)}"



    dash=f'{("-"*(3*len(category)+1)).rjust(3*len(category)+5)}'

   
    per_element_size=[]
    for i in range (0,len(charts)):
        per_element_size.append(len(category[i].name))
    max_element_size=max(per_element_size)
    category_legend=[]
    for j in range (0,len(charts)):
        charts[j].name=(charts[j].name).ljust(max_element_size)
        category_legend.append(charts[j].name)
    left_empty=[]
    for e in range (0,max_element_size):
        left_empty.append(' ')

    legend_list=[]
    for i in range(len(left_empty)):
        legend_list.append([left_empty[i].rjust(4)])
        for j in range(0,len(category_legend)):
            legend_list[i].append((category_legend[j][i]))

    nl='\n'
    legend=f"{nl.join((str(' '.join(str(y).center(2) for y in x))) for x in legend_list)}"


    percentage_charts=f'Percentage spent by category\n'\
                      f'{graph}\n'\
                      f'{dash}\n'\
                      f'{legend}'
    return percentage_charts