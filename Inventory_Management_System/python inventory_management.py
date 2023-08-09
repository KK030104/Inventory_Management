import time

# Reading the Inventory
fd = open('Inventory.txt','r')  
products = fd.read().split('\n')
fd.close()

# Taking User Input
ui_username = input("Enter your Name: ")
ui_phone    = input("Enter your Phone No: ")
ui_mail     = input("Enter your Mail: ")
ui_prod_id  = input("Enter product ID: ")
ui_prod_qn  = input("Enter product Quantity: ")

updated_product_lst = []

# Going through each product detail
for product in products:
    
    prod_details = product.split(',')
    
    if(prod_details[0] == ui_prod_id):
    # Checking if product exists or not

        if (int(ui_prod_qn) <= int(prod_details[3])):
        # If we're having enough quantity
        
            print("-----------------------------")
            print("Product Name     : ", prod_details[1])
            print("Price            : ", prod_details[2]) 
            print("Quantity         : ", ui_prod_qn) 
            print("-----------------------------")
            print("Billing Amount   : ", int(ui_prod_qn) * int(prod_details[2]))
            print("-----------------------------")

            # Updating Inventory list
            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
            
            # Generating Sales in Sales.txt
            fd = open("Sales.txt",'a')
            sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+prod_details[1] +","+ ui_prod_id +","+ ui_prod_qn +","+ str(int(ui_prod_qn) * int(prod_details[2]))+","+time.ctime()+ "\n"
            fd.write(sales_detail)
            fd.close()
            
        else:
        # If we're not having enough quantity
        
            print("Sorry, We're not having enought quantity.")
            print("We're having only",prod_details[3],'quantity.')
            print("Would you like to purchase it?")
            
            ch = input("Press Y/N: ")
            
            if (ch == 'Y' or ch == 'y'):
            # If you want to purchase with remaining quantity
            
                print("-----------------------------")
                print("Product Name     : ", prod_details[1])
                print("Price            : ", prod_details[2]) 
                print("Quantity         : ", prod_details[3]) 
                print("-----------------------------")
                print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
                print("-----------------------------")
            
                
                fd = open("Sales.txt",'a')
                sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+prod_details[1] +","+ ui_prod_id +","+ prod_details[3] +","+ str(int(prod_details[3]) * int(prod_details[2]))+","+time.ctime()+ "\n"
                fd.write(sales_detail)
                fd.close()
                
                # Updating Inventory list
                prod_details[3] = '0'
                

            else:
                print("Thanks")
            
    # Updating my Inventory List
    updated_product_lst.append(prod_details)
    

    
lst = []

# Updating my Inventory String
for i in updated_product_lst:
    prod = i[0] +","+  i[1] +","+ i[2] +","+ i[3] + '\n'
    lst.append(prod)

    
lst[-1] = lst[-1][:-1]
    

# Updating Inventory File
fd = open('Inventory.txt','w')

for i in lst:
    fd.write(i)

fd.close()

print("-------------------")
print("Inventory Updated")