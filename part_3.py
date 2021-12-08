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
data_list = []

vertical_h = [progress, trailer, retriever, exclude]

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
            histogram(pass_credit, defer_credit, fail_credit)
            break
                

def progression_outcome(pass_credit,defer_credit,fail_credit):
    if pass_credit == 120:
        print('Progress\n')
        data_list.append(['Progress',pass_credit,defer_credit,fail_credit])
    elif pass_credit == 100:
        print('Progress (module trailer)\n')
        data_list.append(['Progress (module trailer)',pass_credit,defer_credit,fail_credit])
    elif (pass_credit + defer_credit) < fail_credit:
        print('Exclude \n')
        data_list.append(['Exclude',pass_credit,defer_credit,fail_credit])
    else:
        print('Do not progress – module retriever\n')
        data_list.append(['Do not progress – module retriever',pass_credit,defer_credit,fail_credit])

        
def histogram(pass_credit, defer_credit,fail_credit):
    if pass_credit == 120:
        progress.append(0)
    elif pass_credit == 100:
        trailer.append(0)
    elif(pass_credit + defer_credit) < fail_credit:
        exclude.append(0)
    else:
        retriever.append(0)
    global total_outputs
    total_outputs =  len(progress) + len(trailer) + len(retriever) + len(exclude)
    

def histogram_view_1():
    print('-' * 60)
    print('Horizontal Histogram')
    print('Progress  ',len(progress),':','*' * len(progress))
    print('Trailer   ',len(trailer),':','*' * len(trailer))
    print('Retriever ',len(retriever),':','*' * len(retriever))
    print('Excluded  ',len(exclude),':','*' * len(exclude))
    print('\n')
    total_outputs = len(progress) + len(trailer) + len(retriever) + len(exclude)
    print(total_outputs,'outcomes in total.')
    print('-' * 60)
    

def histogram_view_2():
    print('-' * 60)
    print('Verticle Histogram\n')
    vertical_histogram_view(vertical_h)
    print(total_outputs,'outcomes in total.')
    print('-' * 60)


def vertical_histogram_view(vertical_h):
    print('Progress',len(progress),'|', 'Trailer',len(trailer),'|', 'Retriever',len(retriever),'|', 'Exclude',len(exclude))

    for i in range(total_outputs):
        for x in vertical_h:
            if len(x) > 0:
                print('     ','*','    ', end = '')
                x.pop()
            else:
                print('     ',' ','    ', end = '')
        print()

def list_view():
    print('-' * 60)
    for x in data_list:
        print(f'''{x[0]} - {x[1]},{x[2]},{x[3]}''')
        

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
                histogram_view_1()
                histogram_view_2()
                list_view()
                break

            elif quit_menu == 'y':
                pass
                break
            else:
                print("Invalid option.Please Enter 'y' or 'q'")

    return quit_menu
