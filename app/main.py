from email.policy import default
import uvicorn 
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
# from model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
import json
from fastapi.middleware.cors import CORSMiddleware
    
posts = [
    {
        "id" : 1,
        "function" : "Bisection",
        "equation" : "x^+25-6"
    }
]

users =[UserSchema(fullname='Plug', email='plug@example.com', password='123')]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get for testing
@app.get('/', tags=['test'])
def greet():
    return {"Hello":"World"}

# Get len of currently data
def get_len():
    with open('save_file.json') as json_file:
        data = json.load(json_file)
    return len(data)

# Get Posts
@app.get('/posts', tags=['posts'])
def get_post():
    with open('save_file.json') as json_file:
        data = json.load(json_file)
    return data

# Get Post by ID
# @app.get('/posts/{id}', tags=['posts'])
# def get_one_post(id : int):
#     if id > len(posts):
#         return{
#             "error" : "Post with this id is not exist!"
#         }
#     for post in posts:
#         if post['id'] == id:
#             return {
#                 "data" : post
#             }
            
# Post a blog post
@app.post('/posts', dependencies=[Depends(jwtBearer())], tags=['posts'])
def add_post(post : PostSchema):
    post.id = get_len() + 1
    # posts.append(post.dict())
    # print(post.function)
    save_new_equation(post.id, post.function, post.equation)
    return {
        "info" : "Post Added!"
    }
    
# User signup 
# @app.post('/user/signup', tags=['user'])
# def user_signup(user : UserSchema = Body(default=None)):
#     users.append(user)
#     print(users)
#     return signJWT(user.email)

def check_user(data : UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post('/user/login', tags=['user'])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid login details"
        }

def save_new_equation(postID, postFunc, postEqua):
    with open('save_file.json') as json_file:
        data = json.load(json_file)

        # print(data)
        data.append(
            {
                "id" : postID,
                "function" : postFunc,
                "equation" : postEqua
            }
        )
        # print(data)

    with open('save_file.json', 'w') as outfile:
        outfile.write(json.dumps(data, indent = 4))