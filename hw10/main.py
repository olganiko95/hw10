from flask import Flask
from utils import load_candidates, formate_candidates, get_candidate_by_pk, get_candidate_by_skill

app = Flask(__name__)

@app.route('/')
def page_main():
    '''Главная страница'''
    candidates = load_candidates('candidates.json')
    result = formate_candidates(candidates)
    return result

@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    '''поиск киндидата по pk'''
    candidate = get_candidate_by_pk(uid)
    result = f'< img src = "{candidate["picture"]}" >'
    result += formate_candidates([candidate])
    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    '''поиск киндидата по скиллу'''
    skill_lower = skill.lower()
    candidates = get_candidate_by_skill(skill_lower)
    result = formate_candidates(candidates)
    return result


app.run(host='127.0.0.2', port=80)
