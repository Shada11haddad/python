from fastapi import FastAPI

api = FastAPI()


TODO_TITLE_CREATE_LIST = 'Create a todo list'

all_todos = [
    {'todo_id': 1 , 'title': TODO_TITLE_CREATE_LIST,'descrption':'Explaine the task', 'completed': False},
    {'todo_id': 1 , 'title': 'workout','descrption':'Run for 30min', 'completed': False},
    {'todo_id': 1 , 'title': TODO_TITLE_CREATE_LIST,'descrption':'Explaine the task', 'completed': False},
    {'todo_id': 1 , 'title': TODO_TITLE_CREATE_LIST,'descrption':'Explaine the task', 'completed': False},
    {'todo_id': 1 , 'title': TODO_TITLE_CREATE_LIST,'descrption':'Explaine the task', 'completed': False},
]



#get , post , put . delete

@api.get('/')
def index():
    return{"message":"Hello World"}


@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result':todo}
        else:
            return {'message': 'Todo not found'}


@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    all_todos.append({'todo_id': new_todo_id, 'title': todo['title'], 'description': todo['description'], 'completed': False})
    return new_todo_id
