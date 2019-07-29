import os
from lxml import etree

def generate_xml_from_dictionary(parsed_content, title):
    root = etree.Element('test')
    language = etree.Element('language')
    language.text = title
    root.append(language)
    all_questions_xml = etree.Element('questions')
    for question_index, question_answers in enumerate(parsed_content):
        question_xml = etree.Element('question')
        num_question = etree.Element('numQuestion')
        num_question.text = str(question_index+1)
        question_xml.append(num_question)
        text_question = etree.Element('textQuestion')
        text_question.text = question_answers["question"]
        question_xml.append(text_question)
        all_answers_xml = etree.Element('answers')
        for answer_index, answer in enumerate(question_answers["answers"]):
            if answer["correct_answer"] == True:
                correct_answer = etree.Element('correctAnswer')
                correct_answer.text = str(answer_index+1)
                question_xml.append(correct_answer)
            answer_xml = etree.Element('answer')
            num_option = etree.Element('numOption')
            num_option.text = str(answer_index+1)
            answer_xml.append(num_option)
            text_answer = etree.Element('textAnswer')
            text_answer.text = answer["text"]
            answer_xml.append(text_answer)
            all_answers_xml.append(answer_xml)
        question_xml.append(all_answers_xml)
        all_questions_xml.append(question_xml)
    root.append(all_questions_xml)
    return etree.tostring(root, encoding='utf-8', xml_declaration = True, pretty_print=True)

def create_xml_file(file_title, file_content, file_path=""):
    file_complete_path = file_path+"/"+file_title
    file = open(file_complete_path+".xml", "w", encoding='utf-8')
    file.write(file_content.decode('utf-8'))
    file.close()
    return os.path.abspath(file_complete_path+".xml")

def get_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except:
        return None

def create_xml_folder(folder_name="/xml"):
    folder_dir = os.getcwd() + folder_name
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)
    return folder_dir
