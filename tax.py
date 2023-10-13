# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 00:16:56 2022

@author: Winyi
"""
import datetime
import csv
from OOP_Project_Tax_Report_2021 import data


class user(data.calculation):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    
################### User Information##################################################################################        
class user_Infor(user):   
    def __init__(self,first_name,last_name,Mail_Address,PO_Box,RR,City,Prov_Terr, Postal_code,Email_Address,SIN, date_of_birth,date_of_death,Marital_status, Language):
        super().__init__()
    
        self.__first_name=first_name
        
        self.__last_name=last_name
        self.__mail=Mail_Address
        self.__PO_Box=PO_Box
        self.__RR=RR
        self.__city=City
        self.__Prov_Terr=Prov_Terr
        self.__Postal_code=Postal_code
        self.__Email=Email_Address
        self.__SIN=SIN
        self.__date_of_birth=date_of_birth
        self.__date_of_death=date_of_death
        self.__Marital_status=Marital_status
        self.__language=Language
      
    # check first name    
    def set_first_name(self,first_name):
        
        while first_name.isalpha()==False:
            print('Error:Numbers in First name,please re-enter first name')
            first_name=input('First Name\n')
            self.__first_name=first_name
            
        else:
             self.__first_name=first_name
     #check last name   
    def set_last_name(self,last_name):
        while last_name.isalpha()==False:
            print('Error: Numbers in Last name,please re-enter Last name')
            last_name=input('Last Name\n')
            self.__last_name=last_name
            
        else:
             self.__last_name=last_name   
        
        
    def set_Mail_Address(self,Mail_Address):
        
        self.__mail=Mail_Address
        
    def set_PO_Box(self,PO_Box):
                
        self.__PO_Box=PO_Box
        
    def set_RR(self,RR):
                
        self.__RR=RR
    
    #check city
    def set_city(self,City):
        
        while City.isalpha()==False:
            print('Error: Numbers in City,please re-enter City')
            City=input('City\n')
            self.__city=City
            
        else:
             self.__city=City
     #check province   
    def set_Prov_Terr(self, Prov_Terr):
        
        while Prov_Terr.isalpha()==False:
            print('Error: Numbers in Prov_Terr,please re-enter Prov_Terr')
            Prov_Terr=input('Prov./Terr. \n')
            self.__Prov_Terr=Prov_Terr
            
        else:
             self.__Prov_Terr=Prov_Terr
         #check len of postal code    
    def set_Postal_code(self,Postal_code):
        Postal_code=Postal_code.replace(' ','')
        while len(Postal_code)!=6:
            
            print('Error: Postal Code incorrect,please re-enter Postal Code')
            Postal_code=input('Postal Code \n').replace(' ','')
            self.__Postal_code=Postal_code
            
        else:
             self.__Postal_code=Postal_code
        
        
    def set_Email_Address(self,Email_Address):
        
        self.__Email_Address=Email_Address
        
        
    def set_SIN(self,SIN):
        SIN=SIN.replace(' ','')
        while len(SIN)!=9 and SIN.isnumeric()=='False':
            print('Error: Social Insurance Number(SIN) incorrect,please re-enter ')
            SIN=input('Social Insurance Number(SIN) \n').replace(' ','')
            SIN_num=[]
            SIN_num[:]=SIN
        
            self.__SIN=str(SIN_num)
        else:
            SIN_num=[]
            SIN_num[:]=SIN
        
            self.__SIN=str(SIN_num)            
        
        
        
        
    def set_date_of_birth(self, date_of_birth):
        
        try:
            if date_of_birth=='' or datetime.datetime.strptime(date_of_birth, '%Y-%m-%d'):
            
                self.__date_of_birth=date_of_birth
        except ValueError:
            print ('Incorrect format,please re-enter Date of Birth(YYYY-MM-DD)')
            date_of_birth=input('Date of Birth \n')
            self.__date_of_birth=date_of_birth
            
    
    
    def set_date_of_death(self,date_of_death):
        try:
            if date_of_death=='' or datetime.datetime.strptime(date_of_death,'%Y-%m-%d'):
                self.__date_of_death=date_of_death
            
        except ValueError:
            print('Incorrect format, please re-enter Date of Death(YYYY-MM-DD)')
            date_of_death=input('Date of Death \n')
            self.__date_of_death=date_of_death
        
    def set_Marital_status(self,Marital_status):
    
        valid_num=['1','2','3','4','5','6']
        
        while Marital_status not in valid_num:
            
            print('Incorrect information, Please select your current Marital Status as the folloing instruction:'
                  +'\n Enter 1 to choose "Married"'
                  +'\n Enter 2 to choose "Living common-law'
                  +'\n Enter 3 to choose "Windowed"'
                  +'\n Enter 4 to choose "Divorced"'
                  +'\n Enter 5 to choose "Seperated"'
                  +'\n Enter 6 to choose "Single"')
            Marital_status=input('Please enter your selection: ')
            self.Marital_status=Marital_status
            
        if Marital_status=='1' or Marital_status=='Married':
            self.__Marital_status='Married'
        
        elif Marital_status=='2' or Marital_status=='Living common-law':
            self.__Marital_status='Living common-law'
        
        elif Marital_status=='3' or Marital_status=='Windowed':
            self.__Marital_status='Windowed'
            
        elif Marital_status=='4' or Marital_status=='Divorced':
            self.__Marital_status='Divorced'
        
        elif Marital_status=='5' or Marital_status=='Seperated':
            self.__Marital_status='Seperated'
            
        elif Marital_status=='6' or Marital_status=='Single':
            self.__Marital_status='Single'
        
        
        
        
    def set_Language(self,Language):
        
        while Language.isalpha()==False:
            print('Error: Please re-enter Language')
            Language=input('Your language of correspondence: \n'
                            +'Votre langue de correspondance: ')
            self.__language=Language
            
        else:
             self.__language=Language
        

        
    
    def get_first_name(self):
        
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_mail(self):
        return self.__mail
    def get_PO_Box(self):
        return self.__PO_Box
    def get_RR(self):
        return self.__RR
    def get_city(self):
        return self.__city
    def get_Prov_Terr(self):
        return self.__Prov_Terr
    def get_Postal_code(self):
        return self.__Postal_code
    def get_Email(self):
        return self.__Email
    def get_SIN(self):
        return self.__SIN
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_date_of_death(self):
        return self.__date_of_death
    def get_Marital_status(self):
        return self.__Marital_status
    def get_language(self):
        return self.__language
    
  
  
##########Total Income###############################        


class Total_Income( user):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
   
     
   
    
   
class Self_emplyment(Total_Income):
    def __init__ (self,business, profession, commission , farming, fishing):
        super().__init__() 
        
        self.__business=business        
        self.__profession=profession
        self.__commission=commission
        self.__farming=farming
        self.__fishing=fishing


    def set_value(self):
        val= data.Input_val()
        val.set_input(self.__business)
        self.__business=val.get_value()
        val.set_input(self.__profession)
        self.__profession=val.get_value()
        val.set_input(self.__commission)
        self.__commission=val.get_value()
        val.set_input(self.__farming)
        self.__farming=val.get_value()
        val.set_input(self.__fishing)
        self.__fishing=val.get_value()
        

    def set_Sum(self):
        self.__sum_value=self.__business+self.__profession+self.__commission+self.__farming+self.__fishing
        
    def get_value(self):
        return self.__business,self.__profession,self.__commission,self.__farming,self.__fishing
    def get_Sum(self):
        return self.__sum_value
    



    
class Net_Income(Total_Income):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
                 
        
    
  
class Taxable_income(Total_Income):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
               
##############Federal_tax_on_taxable_income##########################################   
        
class Federal_tax(Taxable_income):
    
    
    
    def __init__(self, taxable_income):
        super().__init__()
        self.__Fed_tax=0
        self.__taxable_income=taxable_income

    def set_fed_tax_taxable(self):
        tax1=0.15
        tax2=0.205
        tax3=0.26
        tax4=0.29
        tax5=0.33
        target1=49020
        target2=98040
        target3=151978
        target4=216511
        
        
        if self.__taxable_income<target1:
            self.__Fed_tax=self.__taxable_income*tax1
        elif self.__taxable_income>=target1 and self.__taxable_income<target2:
            self.__Fed_tax=target1*tax1+(self.__taxable_income-target1)*tax2
        elif self.__taxable_income>=target2 and self.__taxable_income<target3:
            self.__Fed_tax=target1*tax1+target2*tax2+(self.__taxable_income-target2)*tax3
        elif self.__taxable_income>=target3 and self.__taxable_income<target4:
            self.__Fed_tax=target1*tax1+target2*tax2+target3*tax3+(self.__taxable_income-target3)*tax4
        elif self.__taxable_income>=target4:
            self.__Fed_tax=target1*tax1+target2*tax2+target3*tax3+target4*tax4+(self.__taxable_income-target4)*tax5

    def get_fed_tax_taxable(self):
        return self.__Fed_tax



############################## From result###########################################################

class Form(user):
        
    def __init__(self):
        super().__init__()
        
        self.__user=0
        self.__tax_year=''
        self.__user_info={}
        self.__total_income=0
        self.__taxable_income=0
        self.__fed_tax_on_taxable_income=0
        self.__dict_form={}
        
    def set_user(self,user):
        self.__user='user'+str(user)
        self.__dict_form['user']=self.__user
    def set_tax_year(self):
        while self.__tax_year!='2021':
            
            tax_year=input('Please enter tax year(tax-form only applicable for 2021): ')
            self.__tax_year=tax_year
            self.__dict_form['tax year']=self.__tax_year
        else:   
            self.__tax_year=tax_year 
            self.__dict_form['tax year']=self.__tax_year
    def set_user_info(self,user_info):
        self.__user_info=user_info
        self.__dict_form['user infor']=self.__user_info
        
    def set_total_income(self,total_income):
        self.__total_income=total_income
        self.__dict_form['Total income']='${:,.2f}'. format(self.__total_income)
        
    def set_taxable_income(self,taxable_income):
        self.__taxable_income=taxable_income
        self.__dict_form['Taxable income']='${:,.2f}'. format(self.__taxable_income)
        
    def set_fed_tax_taxable(self, fed_tax_on_taxable_income):
        self.__fed_tax_on_taxable_income=fed_tax_on_taxable_income
        self.__dict_form['Federal tax on taxable income']='${:,.2f}'. format(self.__fed_tax_on_taxable_income)
    def set_csv(self,first_name,last_name):
        filename='tax_report'+str(first_name)+''+str(last_name)+'.csv'
        with open(filename,'a') as tax_file:
            writer=csv.writer(tax_file)
            for key, value in self.__dict_form.items():
                writer.writerow([key,value])
        
    def get_user(self):
        return self.__user
    
    def get_tax_year(self):
        return self.__tax_year
    def get_user_info(self):
        return self.__user_info
    def get_total_income(self):
        return self.__total_income
    def get_taxable_income(self):
        return self.__taxable_income 
    def get_fed_tax_taxable(self):
        return self.__fed_tax_on_taxable_income
    
    def get_dict_form(self):
        return self.__dict_form
    
    
