from bs4 import BeautifulSoup

def get_questions_in_html(html_string):
    html = BeautifulSoup(html_string, 'html.parser')
    title =  html.select('h2')
    questions_answers = {"title":  title[0].text, "content": []}
    for div in html.select('div.pregunta div'):
        q = {"question": "", "answers": []}
        for p in div.select('p'):
            q["question"] = p.text
        for index, span in enumerate(div.select('span')):
            if index % 2 != 0:
                q["answers"].append({"coorrect_answer": False, "text": span.text})
        questions_answers["content"].append(q)
    return questions_answers
