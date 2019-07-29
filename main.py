from director import *

if __name__ == '__main__':
    while(True):
        text = input('Insert url you want to parse: ')
        if text == "exit":
            break
        else:
            print('Insert path of html answers.\
            \nWrite whatever if you don\'t have it, answer will automatically be set to the last option of each question')
            answers_path = input('::')
            reference = generate_questionary_xml(text, answers_path)
            print('Your xml has been saved in:' + reference)
            try:
                i =1
            except:
                print(\
                "There was an error, please check your internet connection and your URL.\
                \nRememeber this program only works with URL of http://gplsi.dlsi.ua.es/proyectos/examinador/{name_of_the_file}.php")
            print("-----------------------------------------------------------------------------------------")
