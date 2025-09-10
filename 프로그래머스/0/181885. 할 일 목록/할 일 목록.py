def solution(todo_list, finished):
    return [todo * (1-fin)
            for (todo, fin) in zip(todo_list, finished)
           if not fin]