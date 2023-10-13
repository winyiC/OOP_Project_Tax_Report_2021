# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 23:58:06 2022

@author: Winyi
"""

from OOP_Project_Tax_Report_2021 import data as d, tax


def user_num(num):
    
    user_num= tax.user(Num=num)
    

    return user_num.get_value()

def user_id():
    
    dict1={}
    first_name=input('First Name \n')
    
    last_name=input('Last Name \n ')
    
    Mail_Address=input('Mail Adress \n ' )
    PO_Box=input('PO_BOX \n ')
    RR=input('RR \n ')
    City=input('City \n ').capitalize()
    Prov_Terr=input('Prov./Terr. \n ').capitalize()
    Postal_code=input('Postal code \n ').upper()
    Email_Address=input('Email Address \n ')
    SIN=input('Social insurance number(SIN) \n ')
    date_of_birth=input('Date of birth(eg.1990-12-01) \n ')
    date_of_death=input('if this return is for a deceased person,'+'\n enter the date of death (eg. 1990-12-01) \n ')
    Marital_status=input('Marital status on December 31,2021'+
                                           '\n (select the number as following: '+'\n1:Married, 2:Living common-law, 3:Windowed, 4:Divored, 5: Seperated, 6:Single)  : ')
    Language=input('English or Francais \n ').capitalize()
    
    user_info= tax.user_Infor(first_name, last_name, Mail_Address, PO_Box, RR, City, Prov_Terr, Postal_code, Email_Address, SIN, date_of_birth, date_of_death, Marital_status, Language)
    user_info.set_first_name(first_name)
    user_info.set_last_name(last_name)
    user_info.set_Mail_Address(Mail_Address)
    user_info.set_Postal_code(Postal_code)
    user_info.set_SIN(SIN)
    user_info.set_date_of_birth(date_of_birth)
    user_info.set_date_of_death(date_of_death)
    user_info.set_Marital_status(Marital_status)
    user_info.set_Language(Language)
    
    dict1['First Name']=user_info.get_first_name()
    dict1['Last Name']=user_info.get_last_name()
    dict1['Mailing address']=user_info.get_mail()
    dict1['Postal code']=user_info.get_Postal_code()
    dict1['SIN']=user_info.get_SIN()
    dict1['Date of birth']=user_info.get_date_of_birth()
    dict1['Date of death']=user_info.get_date_of_death()
    dict1['Marital_status']=user_info.get_Marital_status()
    dict1['Language']=user_info.get_language()
    
    print(dict1)
    
    return dict1,user_info.get_first_name(),user_info.get_last_name()

def Self_Employment():
    print('\n\nSelf-employment income(see Guide T4002): \n')
    business='Business income Net #13500 \n'
    profession='Professional income Net #13700 \n'
    commission='Commission income Net #13900 \n'
    farming='Farming income Net #14100 \n'
    fishing='Fishing income Net #14300 \n'

    self_empl= tax.Self_emplyment(business, profession, commission, farming, fishing)
    self_empl.set_value()
    self_empl.set_Sum()
    
    return self_empl.get_Sum()

def Total_income(): 
  

   print('\n\nSection:Total Income \n')
   print('\n\nPlease enter \'0\' ,if you have not recieved any following income.\n')
   
   
   val=d.Input_val()
   inc1='Employ Income (box 14 of all T4 slips) #10100 \n'
   inc2='Other employment income \n'
   inc3='Old age security(OAS) pension(see line 104000 of the guide #10400 \n'
   inc4='CPP_or_QPP_benefits(box 20 of the T4A(P) slip #11400 \n'
   inc5='Universal child care benefit(UCCB) (see the RC62 slip) #11700 \n'
   inc6='Employment insurance and other benefits(box 14 of the T4E slip #11700 \n'
   inc7='Taxable amount of dividends from taxable Canadian corporations(use Federal Worksheet):\n'+'Amount of dividends (eligibel and other than eligible) #12000 \n'
   inc8='Interest and other investment income(use Federal Worksheet) \n'
   inc9='Retal Income \n'
   inc10='Taxable capital gains \n'
   inc11='Registered retirement savings plan(RRSP) income \n'
   inc12='Other income (specify)\n'
   inc13='Taxable scholarships, fellowships, bursaris, and artist\'s project grants \n'
   inc14='Workers\' compensation benefits \n'
   inc15='Social assistance payments \n'
   inc16='Net federal supplements paid(box 21 of the T4A(OAS) slip \n'
   
 
   val.set_input(inc1)
   Empl_income=val.get_value()
   val.set_input(inc2)
   Other_empl_income=val.get_value()
   val.set_input(inc3)
   Pension=val.get_value()
   val.set_input(inc4)
   CPP_or_QPP_benefit=val.get_value()
   val.set_input(inc5)
   childcare_benefit=val.get_value()
   val.set_input(inc6)
   Empl_insurance=val.get_value()
   val.set_input(inc7)
   Taxable_div=val.get_value()
   val.set_input(inc8)
   Invest_income=val.get_value()
   val.set_input(inc9)
   Rental=val.get_value()
   val.set_input(inc10)
   Capital_gain=val.get_value()
   val.set_input(inc11)
   RRSP_income=val.get_value()
   val.set_input(inc12)
   Other=val.get_value()
   val.set_input(inc13)
   Grants=val.get_value()
   Self_empl=Self_Employment()
   val.set_input(inc14)
   Compensation=val.get_value()
   val.set_input(inc15)
   Social_assistance=val.get_value()
   val.set_input(inc16)
   Net_fed_supp_paid=val.get_value()
  
   
   
   income= tax.Total_Income(Employment_income=Empl_income, Other_employment_income=Other_empl_income, OAS_pension=Pension, CPP_or_QPP_benefits=CPP_or_QPP_benefit, Child_care_benefit=childcare_benefit, Employment_Insurance=Empl_insurance, Taxable_dividents=Taxable_div, Investment_Income=Invest_income, Rental_Income=Rental, Taxable_capital_gains=Capital_gain, RRSP_Income=RRSP_income, Other_Income=Other, Taxable_grants=Grants, Self_Employment_Income=Self_empl, Worker_compensation_benefit=Compensation, Social_assistance_payments=Social_assistance, Net_federal_support_paid=Net_fed_supp_paid)
   income.set_Sum()
   total=income.get_Sum()
   print('Total Income:$ {:,.2f}'.format(total))
   Net_total=Net_income(total)
   if Net_total<=0:
       Net_total=0
        
   print('\n Net_income: $ {:,.2f}'.format(Net_total))

   
   return Net_total
   

def Net_income(Total_income):
    
  
    print('\n\n Section: Net income\n')
    
    val=d.Input_val()
    exp1='Registered pension plan(RPP) deduction'+'\n (box 20 of all T4 slips andbox 032 of T4A slips)'+'\n#20700 \n'
    exp2='RRSP deduction (see Schedule 7 and attach receipts) #20810\n'
    exp3='Deduction for elected split-pension amount(complete Form T1032) #21000\n '
    exp4='Annal union, professional, or like dues(receipts and box 44 of all T4 slips) #21200\n '
    exp5='Universal child care benefit repayment(box 12 of all RC62 slips) #21300\n '
    exp6='Child care expenses (complete Form T778) \n '
    exp7='Disability supports deduction (complete Form T929) #21500\n '
    exp8='Business investment loss(see Guide T4037) Allowable deduction #21700\n '
    exp9='Moving Expenses (complete Form T1-M \n'
    exp10='Support payments made(see Guide P102) Allowable deduction #22000 \n '
    exp11='Carrying charges, interest expensecs, and other expenses (use Federal Worksheet) #22100 \n '
    exp12='Deduction for CPP or QPP enhanced contributions on  self_employment income and other earnings'+'\n(complete Schedule 8 or Form RC381, whichever applies) #22200\n'
    exp13='Deduction for CPP or QPP contributions on employment income \n'+'(complete Schedual 8 or Form 381, whichever applies)'+'\n(maximum $290.50 ) #22215\n'
    exp14='Exploration and development expenses #22400 \n'
    exp15='Other employment expenses (see Guide T4044) #22900\n'
    exp16='Clergy residence deduction (complete Form T1229) #23100 \n '
    exp17='Other deductions #23200\n '
    exp18='Fedreal COVID-19 benefits repayment(box 201 of all federal T4A slips) #23210 \n'
    
    
    
    val.set_input(exp1)
    RPP_de=val.get_value()
    
    val.set_input(exp2)
    RRSP_de=val.get_value()
    
    val.set_input(exp3)
    De_elected=val.get_value()
    
    val.set_input(exp4)
    Union=val.get_value()
    
    val.set_input(exp5)
    Child_care=val.get_value()
    
    val.set_input(exp6)
    Child_Exp=val.get_value()
    
    val.set_input(exp7)
    Disable_sup=val.get_value()
    
    val.set_input(exp8)
    invest_loss=val.get_value()
    
    val.set_input(exp9)
    Moving_Exp=val.get_value()
    
    val.set_input(exp10)
    Sup_payments=val.get_value()
    
    val.set_input(exp11)
    Other_Exp=val.get_value()
    
    val.set_input(exp12)
    De_self_emp=val.get_value()
    
    val.set_input(exp13)
    De_empl=val.get_value()
    
    val.set_input(exp14)
    Explor_and_dev_Exp=val.get_value()
    
    val.set_input(exp15)
    Other_empl_Exp=val.get_value()
    
    val.set_input(exp16)
    recidence_de=val.get_value()
    
    val.set_input(exp17)
    Other_de=val.get_value()
    
    val.set_input(exp18)
    Covid_19_ben_repay=val.get_value()
    

    
    Net= tax.Net_Income(RPP_deduction=RPP_de, RRSP_deuction=RRSP_de, Deduction_for_elected_splited_pesion_amount=De_elected, Annual_union=Union, Universal_Child_Care_benefit=Child_care, Child_care_expenses=Child_Exp, Disability_support_deduction=Disable_sup, Bussiness_investment_loss=invest_loss, Moving_expense=Moving_Exp, Support_payments=Sup_payments, Exploration_and_development_expenses=Explor_and_dev_Exp, Other_expenses=Other_Exp, Deduction_CPP_QPP_on_self_employment=De_self_emp, Deduction_CPP_QPP_on_employment=De_empl, Other_employment_expenses=Other_empl_Exp, Cleray_residence_deduction=recidence_de, Other_deductions=Other_de, Federal_COVID_19_benefits_repayments=Covid_19_ben_repay)
    Net.set_Sum()
    Net.set_sub(Total_income)
    
    return Net.get_Sum()
   
def Taxable_income(total_income):
    
    print('\n\nSection:Taxable_income\n')
    
    val=d.Input_val()
    de1='Canadian Armed Forces personnel and police deduction (box 43 of all T4 slips) #24400 \n'
    de2='Security options deductions (boxes 39 and 41 of T4 slips or see Form T1212) #24900 \n'
    de3='Other payment deduction (enter the amount form line 14700 if you did not enter an anount on line 14600; otherwise, user Fedreal Worksheet)'+'\n#25000\n'
    d4='Limited partnetship losses of other years #25100 \n'
    d5='Non-capital losses of other years #25200 \n'
    d6='Net capital losses of other years #25300 \n'
    d7='Capital gains deduction(complete Form T657) #25400 \n'
    d8='Northen residents deductions(complete Form T2222) #25500 \n'
    d9='Addition deductions #25600 \n'
    val.set_input(de1)
    Armed_Force_de=val.get_value()
    val.set_input(de2)
    Secur_Op_de=val.get_value()
    val.set_input(de3)
    Other_pay=val.get_value()
    val.set_input(d4)
    Lim_Par_losses=val.get_value()
    val.set_input(d5)
    Non_cap_losses=val.get_value()
    val.set_input(d6)
    Net_cap_losses=val.get_value()
    val.set_input(d7)
    Cap_gains_de=val.get_value()
    val.set_input(d8)
    North_re_de=val.get_value()
    val.set_input(d9)
    Add_de=val.get_value()
    
    
    Tax_inc= tax.Taxable_income(Canadian_Armed_Forces_deduction=Armed_Force_de, Security_options_deductions=Secur_Op_de, Other_payments_deduction=Other_pay, Linited_Partnership_losses_of_other_year=Lim_Par_losses, Non_capital_losses_of_other_years=Non_cap_losses, Net_capital_losses_of_other_years=Net_cap_losses, Capital_gains_deduction=Cap_gains_de, Northern_residents_deductions=North_re_de, Additional_deductions=Add_de)
    Tax_inc.set_Sum()
    Tax_inc.set_sub(total_income)
    
    Tax_inc_f=Tax_inc.get_Sum()
    print('\n Taxable income: ${:,.2f} '. format(Tax_inc_f))
    return Tax_inc_f

def Fed_tax(tax_income):
    print('\n\nSection:Fed_tax\n')
    fed_tax= tax.Federal_tax(tax_income)
    fed_tax.set_fed_tax_taxable()
    final_tax=fed_tax.get_fed_tax_taxable()
    print('Federal tax on taxable income: ${:,.2f} '. format(final_tax))
    return final_tax


def main():
    
    again=0
    num=0
    while again==0:
        t1= tax.Form()
        num=num+1
        user=user_num(num)
        t1.set_user(user)
        print(t1.get_user())
        t1.set_tax_year()
        user_info,first_name,last_name=user_id()
        t1.set_user_info(user_info)
        total_income=Total_income()
        t1.set_total_income(total_income)
        taxable_income=Taxable_income(total_income)
        t1.set_taxable_income(taxable_income)
        Fed_tax_taxable=Fed_tax(taxable_income)
        t1.set_fed_tax_taxable(Fed_tax_taxable)
        print(t1.get_dict_form())
        t1.set_csv(first_name,last_name)
        again=int(input('Report tax for other user(o:yes,1:no)\n'))
        
        
main()



