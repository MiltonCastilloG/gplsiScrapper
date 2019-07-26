from director import *

if __name__ == '__main__':
    while(True):
        text = input('Insert url you want to parse: ')
        if text == "exit":
            break
        else:
            reference = generate_questionary_xml(text)
            print('Your xml has been saved in:' + reference)
            print("-----------------------------------------------------------------------------------------")
