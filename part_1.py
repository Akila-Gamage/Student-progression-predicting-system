# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210423
# Date:

pass_credit = 0
defer_credit = 0
fail_credit = 0

progress = []
trailer = []
retriever = []
exclude = []

rangelist = [0,20,40,60,80,100,120]

def validation_mode_1():
    validation()
    
def validation_mode_2():
    global pass_credit, defer_credit, fail_credit
    validation()
    histogram(pass_credit, defer_credit, fail_credit)
       

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
            progression_outcome(pass_credit,defer_credit,fail_credit)
            break

def progression_outcome(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        print('Progress\n')
    elif pass_credit == 100:
        print('Progress (module trailer)\n')
    elif (pass_credit + defer_credit) < fail_credit:
        print('Exclude \n')
    else:
        print('Do not progress – module retriever\n5')

def histogram(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        progress.append(0)
    elif pass_credit == 100:
        trailer.append(0)
    elif(pass_credit + defer_credit) < fail_credit:
        exclude.append(0)
    else:
        retriever.append(0)


def histogram_view():
    print('-' * 60)
    print('Horizontal Histogram')
    print('Progress',len(progress),':','*' * len(progress))
    print('Trailer',len(trailer),':','*' * len(trailer))
    print('Retriever',len(retriever),':','*' * len(retriever))
    print('Excluded',len(exclude),':','*' * len(exclude))
    print('\n')
    total_outputs = len(progress) + len(trailer) + len(retriever) + len(exclude)
    print(total_outputs,'outcomes in total.')
    print('-' * 60)

quit_menu = ''

def enter_or_quit():
    global quit_menu
    while True:
        try:
            quit_menu = input("Would you like to enter another set of data?\n"
                              "Enter 'y' for yes or 'q' to quit and view results: ")
            print('\n')
            lower_quit = quit_menu.lower()
            
        except ValueError:
            print("Invalid option.Please Enter 'y' or 'q'")
        else:
            if lower_quit == 'q':
                histogram_view()
                break

            elif lower_quit == 'y':
                pass
                break
            else:
                print("Invalid option.Please Enter 'y' or 'q'")

    return quit_menu



            
    


    
