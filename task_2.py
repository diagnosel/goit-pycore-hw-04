
from importlib.resources import path


def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age, *_ = line.strip().split(',')
                    age = int(age)
                    cat = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat)   
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError: 
        return []
    return cats_info
    
    
cat = get_cats_info('cats.txt')
print(cat)