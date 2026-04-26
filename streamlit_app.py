import streamlit as st
st.write("Welcome to Shiva Sweet shop")
st.write()
st.write("""Type 1 for menu 
Type 2 to exit""")
st.write()
a = int(st.text_input("Enter 1/2 = "))
st.write()
if a==2:
    st.write("Hope to see you again")
else:
    match  a :
        case 1 : 
            st.write("""Menu
Type 1 for Gulab Jamun
Type 2 for Rasgulla
Type 3 for Jalebi
Type 4 for Kaju Katli
Type 5 for Barfi (Plain)
Type 6 for Ladoo (Besan)
Type 7 for Chandrakala
Type 8 for Kalakand
Type 9 for Peda
Type 10 for Soan Papdi
Type 11 for Carrot Halwa (Gajar ka Halwa)
Type 12 for Rabri
Type 13 for Moong Dal Halwa
Type 14 for Mysore Pak
Type 15 for Sandesh""")
        case _ :
            st.write("Hope to see you again")
    st.write()
    menu = int(st.text_input("Enter the item number = "))
    if menu>=16:
        st.write("Error")
    else:    
        match menu:
            case 1:
                sn = "Gulab Jamun"
                sp = 900
            case 2:
                sn = "Rasgulla"
                sp = 750
            case 3:
                sn = "Jalebi"
                sp = 300
            case 4:
                sn = "Kaju Katli"
                sp =  840
            case 5:
                sn = "Barfi (Plain)"
                sp = 540
            case 6:
                sn = "Ladoo (Besan)"
                sp = 400
            case 7:
                sn = "Chandrakala"
                sp = 120
            case 8:
                sn = "Kalakand"
                sp =  200
            case 9:
                sn = "Peda"
                sp = 240
            case 10:
                sn = "Soan Papdi"
                sp = 250
            case 11:
                sn = "Carrot Halwa (Gajar ka Halwa)"
                sp = 400
            case 12:
                sn = "Rabri"
                sp =  450
            case 13:
                sn = "Moong Dal Halwa"
                sp = 350
            case 14:
                sn = "Mysore Pak"
                sp = 450
            case 15:
                sn = "Sandesh"
                sp = 450
            case _:
                sn = "Invalid Item Number"
                sp =  0
        st.write() 
        st.write("Sweet Name = ",sn)
        st.write("Sweer Price = Rs.",sp)
        st.write()
        qty=float(st.text_input("Enter Quantity in kg only = "))
        st.write("Qunatity of item = ",qty)
        st.write()
        bill = sp*qty
        st.write("Your bill = Rs",bill)
        st.write()
        st.write("Thank You for shopping")
        st.write()
        st.write("Choose Mode of Payment")
        st.write()
        st.write("""Type 1 for Cash Payment
Type 2 for UPI
Type 3 for Net Banking""")
        st.write()
        mode = int(st.text_input("Enter the code for Payment mode = "))
        st.write()
        match mode:
            case 1:
                st.write("Your mode of payment is Cash")
            case 2:
                st.write("Your mode of payment is UPI")
                st.write("Please wait while we direct you to payent gateway")
            case 3:
                st.write("Your mode of payment is Net Banking")
                st.write("Please wait while we direct you to payent gateway")
            case _:
                st.write("Your mode of payment is invalid. Please! try again later")
        st.write("Hope to see to again")





