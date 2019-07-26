from scrapper import simple_get
from questions_parser import *
from questions_xml_generator import *
from regex_repository import *

def generate_questionary_xml(url):
    content = get_page(url)
    parsed_content = parse_questions(content)
    file_content = generate_xml_from_dictionary(parsed_content["content"], eliminate_special_characters(parsed_content["title"]))
    title = adapt_title_for_windows(parsed_content["title"])
    folder = get_folder_for_xml()
    return create_xml_file(title, file_content, file_path=folder)

def get_page(url):
    response = simple_get(url)
    if response is not None:
        return simple_get(url)
    raise Exception('Error retrieving contents at {}'.format(url))

def parse_questions(content):
    return get_questions_in_html(content)

def build_xml(parsed_content, title):
    return generate_xml_from_dictionary(parsed_content, title)

def get_folder_for_xml(folder_name="/xml"):
    folder_dir = os.getcwd() + folder_name
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)
        print("Directory " , folder_dir ,  " created ")
    return folder_dir
