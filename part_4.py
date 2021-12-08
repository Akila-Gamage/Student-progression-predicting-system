# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210423
# Date: 08/12/2021

pass_credit = 0
defer_credit = 0
fail_credit = 0
total_outputs = 0

progress = []
trailer = []
retriever = []
exclude = []

rangelist = [0, 20, 40, 60, 80, 100, 120]

def validation():
    global pass_credit, defer_credit, fail_credit
    while True:
        try:
            pass_credit = int(input('Enter your total PASS credits: '))
        except ValueError:
            print('Integer required\n')
            continue
        else:
            if pass_credit not in rangelist:
                print('Out of range\n')
            elif pass_credit in rangelist:
                break

    while True:
        try:
            defer_credit = int(input('Enter your total DEFER credits: '))
        except ValueError:
            print('Integer required\n')
            continue
        else:
            if defer_credit not in rangelist:
                print('Out of range')
            elif defer_credit in rangelist:
                break

    while True:
        try:
            fail_credit = int(input('Enter your total FAIL credits: '))
        except ValueError:
            print('Integer required\n')
            continue
        else:
            if fail_credit not in rangelist:
                print('Out of range\n')
            elif fail_credit in rangelist:
                break

    while True:
        total_credit = pass_credit + defer_credit + fail_credit
        if total_credit != 120:
            print('Total incorrect\n')
            validation()
            break
        else:
            progression_outcome(pass_credit, defer_credit, fail_credit)
            break

def progression_outcome(pass_credit,defer_credit,fail_credit):
    if pass_credit == 120:
        print('Progress\n')
        file.write('Progress - ' +str(pass_credit)+','+str(defer_credit)+','+str(fail_credit)+ '\n')
        file.close()
    elif pass_credit == 100:
        print('Progress (module trailer)\n')
        file.write('Progress (module trailer) - '+str(pass_credit)+','+str(defer_credit)+','+str(fail_credit)+ '\n')
        file.close()
    elif (pass_credit + defer_credit) < fail_credit:
        print('Exclude \n')
        file.write('Exclude - ' +str(pass_credit)+','+str(defer_credit)+','+str(fail_credit)+ '\n')
        file.close()
    else:
        print('Do not progress – module retriever\n')
        file.write('Do not progress – module retriever - ' +str(pass_credit)+','+str(defer_credit)+','+str(fail_credit)+ '\n')
        file.close()

def text_file():
    global file
    file = open('Staff_version_outputs.txt','a')
    validation()

def text_file_print():
    print('-' * 60)
    file = open('Staff_version_outputs.txt','r')
    print(file.read())
    

quit_menu = ''

def enter_or_quit():
    global quit_menu
    while True:
        try:
            quit_menu = input("Would you like to enter another set of data?\n"
                              "Enter 'y' for yes or 'q' to quit and view results: ")
            print('\n')
            
        except ValueError:
            print("Invalid option.Please Enter 'y' or 'q'")
        else:
            if quit_menu == 'q':
                text_file_print()
                break

            elif quit_menu == 'y':
                pass
                break
            else:
                print("Invalid option.Please Enter 'y' or 'q'")

    return quit_menu
