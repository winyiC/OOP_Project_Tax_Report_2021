# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:50:37 2022

@author: winyi
"""

class calculation:
    def __init__(self, **kwargs):
        self.__dict1={}
        for key,value in kwargs.items():
            self.__value=value
            self.__key=key
            self.__dict1[key]=value
            setattr(self, key,value)
        self.__sum_value=0
    def  set_Sum(self):
        list1=[]
        sum_value=0
        for value in self.__dict1.values():
            list1.append(value)
        sum_value=sum(list1)    
        self.__sum_value=sum_value
        
    def set_sub(self,val):
        self.__sum_value=val-self.__sum_value
    
    def set_mul(self,val):
        self.__sum_value=val*self.__sum_value

    def get_dict(self):
        return self.__dict1
    def get_Sum(self):
        return self.__sum_value
    def get_value(self):
        return self.__value

    def get_key(self):
        return self.__key
    
##################Input value#######################################    
class Input_val:
    def __init__(self):
        self.__prompt=''
        self.__value=0
        
    def set_input(self,*prompts):
        for prompt in prompts: 
            try:
               
                value=float(input(prompt).replace(',',''))
                self.__value=value
               
            except ValueError:
                print('Please Enter correct Number')
                value=float(input(prompt).replace(',',''))
                self.__value=value
     
            while self.__value<0:
                print('Please Enter correct Number')
                value=float(input(prompt).replace(',',''))
                self.__value=value
              
        
    def get_value(self):
        return self.__value 
   
"""
a='a value: '
b='b value: '



val=Input_val()
val.set_input(a)
v1=val.get_value()
val.set_input(b)
v2=val.get_value()


c=3
d=10
e=2
test=calculation(a=v1,b=v2,c=3)
test.set_Sum()
test.set_sub(d)
#test.set_mul(e)
print(test.get_dict())
print(test.get_Sum())
"""
