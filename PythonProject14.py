# CONTACT BOOK 
name=["Karan","Aryan","Rishab","Ashutosh","Abhinav singh","Divesh","Vansh","Amank","Praveen","Vignesh","Harshit","Aryan prasad","Kishlay","Deepti maan","Ashishdeep","Ashish","Bhargav","Vaibahv","Saurabh","Aman","Riya","Pranav","Austin","Piyush","Pranav nanda","Shreya","Ayushi","Ankush","MOhit","Rinchal","Mehak","Sushant"]
total=len(name)
print("Total contacts:",total)
print(name)
phone_numbers=["765199122","91194954","63879439","86034210","83490243","79858382","98170284","62045544","629969821","63615609","70739390","72248905","73577586","76170807","7621001","77044817","83173045","82987986","85949819","85457692","85871162","8590519","85907157","86991352","88470057","903724227","91275270","91448830","9149194","95203954","98725404","99023177"]
for i in range(total):
    print("{}\t\t\t\t\t\t{}".format(name[i], phone_numbers[i]))
b=True
while b==True:
    search_term = input("\nEnter Search Term: ")
    print("Search Result")
    if search_term in name:
            
            x=name.index(search_term)
            phone_number=phone_numbers[x]
            print("Name {}, Phone Number: {}".format(search_term, phone_number))
        
    else:
        print("Name not found")
    
