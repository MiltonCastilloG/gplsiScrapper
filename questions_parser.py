from bs4 import BeautifulSoup

def get_questions_in_html(html_string, answer_list):
    html = BeautifulSoup(html_string, 'html.parser')
    title =  html.select('h2')
    questions_answers = {"title":  title[0].text, "content": []}
    for div in html.select('div.pregunta div'):
        q = {"question": "", "answers": []}
        for p in div.select('p'):
            q["question"] = p.text
        options_list = div.select('span')
        correct_answer = None
        if answer_list is not None:
            correct_answer = find_answer_of_question(q["question"], answer_list)
        for index, span in enumerate(options_list):
            if index % 2 != 0:
                correct_answer_flag = False
                if span.text == correct_answer:
                    correct_answer_flag = True
                elif index + 1 == len(options_list):
                        if correct_answer is None:
                            correct_answer_flag = None
                q["answers"].append({"correct_answer": correct_answer_flag, "text": span.text})
        questions_answers["content"].append(q)
    return questions_answers

def get_correct_answer_list(answer_html_string):
    answer_html = BeautifulSoup(answer_html_string, 'html.parser')
    questions_correct_answers = []
    question = None
    i = 0
    for p in answer_html.select("#contenido p"):
        i += 1
        if i==1:
            question = p.text
        if i==4:
            questions_correct_answers.append({"question": question, "answer": p.text.split("Solución: ")[1]})
            i = 0
    return questions_correct_answers

def find_answer_of_question(question, list):
    for qa in list:
        if qa['question'] == question:
            return qa['answer']
    return None
