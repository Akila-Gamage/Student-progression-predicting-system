# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210423
# Date: 

import part_1
import part_2
import part_3


main_menu = ''
quit_menu = ''


def menu():
    global main_menu, quit_menu
    while True:
       
        main_menu = input("Enter '1' to Open Students Version: \n"
                          "Enter '2' to Open Students Version(Validation): \n"
                          "Enter '3' to Open Staff Version with Histogram: \n"
                          "Enter '4' to Open Staff Version with Histogram (vertical mode): \n"
                          "Enter '5' to Open Staff Version with : \n"
                          "Enter 'q' to Quit: ")

        if main_menu == 'q':
            print('Quit Programme')
            quit()

        elif main_menu == '1':
            print('~' * 60)
            print('Student Version\n')
            pass_credit = int(input('Please enter your credits at pass: '))
            defer_credit = int(input('Please enter your credits at defer: '))
            fail_credit= int(input('Please enter your credits at fail: '))
            part_1.progression_outcome(pass_credit, defer_credit, fail_credit)
            print('~' * 60)
            
            
        elif main_menu == '2':
            print('~' * 60)
            print('Student Version(Validation)\n')
            part_1.validation_mode_1()
            print('~' * 60)
            
        elif main_menu == '3':
            print('~' * 60)
            print('Staff version with Histogram\n')
            while True:
                part_1.validation_mode_2()
                quit_menu = part_1.enter_or_quit()
                if quit_menu == 'q':
                    break
            print('~' * 60)
            
        elif main_menu == '4':
            print('~' * 60)
            print('Staff version with Histogram(Vertical mode)\n')
            while True:
                part_2.validation()
                quit_menu = part_2.enter_or_quit()
                if quit_menu == 'q':
                    break                      
            print('~' * 60)

        elif main_menu == '5':
            print('~' * 60)
            print('Staff version with \n')
            while True:
                part_3.validation()
                quit_menu = part_3.enter_or_quit()
                if quit_menu == 'q':
                    break
            print('\n')
            print('~' * 60)
            
                
        
        else:
            print("Please Enter '1' or '2' or '3' or '4' or 'q'\n")

menu()
            
        

    


