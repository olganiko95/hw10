import json

def load_candidates(file):
    with open(file, 'r', encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates


def formate_candidates(candidates):
    '''Форматирование списка кандидатов'''
    result = '<pre>'

    for candidate in candidates:
        result += f'''
            Имя кандидата: {candidate['name']}
            Позиция кандидата: {candidate['position']}
            Навыки кандидата: {candidate['skills']}

        '''
    result += '<pre>'
    return result



def get_candidate_by_pk(pk):
    candidates = load_candidates('candidates.json')
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None

def get_candidate_by_skill(skill):
    candidates = load_candidates('candidates.json')
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result