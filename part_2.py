pass_credit = 0
defer_credit = 0
fail_credit = 0
total_outputs = 0

progress = []
trailer = []
retriever = []
exclude = []

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
            progression_outcome(pass_credit,defer_credit,fail_credit)
            histogram(pass_credit, defer_credit,fail_credit)
            break


def progression_outcome(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        print('Progress\n')
    elif pass_credit == 100:
        print('Progress (module trailer)\n')
    elif (pass_credit + defer_credit) < fail_credit:
        print('Exclude \n')
    else:
        print('Do not progress – module retriever')


def histogram(pass_credit, defer_credit, fail_credit):
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
    

def histogram_view():
    
    print('\n')
    print('-' * 60)
    print('Verticle Histogram\n')
    vertical_histogram_view(vertical_h)
    print('\n')
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
                histogram_view()
                break

            elif quit_menu == 'y':
                pass
                break
            else:
                print("Invalid option.Please Enter 'y' or 'q'")

    return quit_menu


