from scrapper import simple_get
from questions_parser import *
from questions_xml_generator import *
from regex_repository import *

def generate_questionary_xml(url, correct_answers_path):
    content = get_page(url)
    parsed_content = parse_questions(content, get_answer_list(correct_answers_path))
    file_content = generate_xml_from_dictionary(parsed_content["content"], eliminate_special_characters(parsed_content["title"]))
    title = adapt_title_for_windows(parsed_content["title"])
    folder = get_folder_for_xml()
    return create_xml_file(title, file_content, file_path=folder)

def get_page(url):
    response = simple_get(url)
    if response is not None:
        return response
    raise Exception('Error retrieving contents at {}'.format(url))

def get_answer_list(correct_answers_path):
    answers_file = get_text_from_file(correct_answers_path)
    if answers_file is not None:
        return get_correct_answer_list(answers_file)
    else:
        return None

def parse_questions(content, answer_list):
    return get_questions_in_html(content, answer_list)

def build_xml(parsed_content, title):
    return generate_xml_from_dictionary(parsed_content, title)

def get_folder_for_xml():
    return create_xml_folder()
