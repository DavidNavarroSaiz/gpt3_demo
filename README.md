

# to run the api :

uvicorn main:app --reload

and then make a request to the endporint 'extract-information'


curl -X 'POST' \
  'http://127.0.0.1:8000/extract-information/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_input": "my name is david camilo navarro saiz and i live in medellin street 3#56-12 and my objective with this course is to learn new techniques and have a lot of friends, i am not very good with technology and science i am 30 years old and my email is davarros@unal.edu.co"
}'

