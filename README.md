# The app(API) for taking polls
#### This Poll API maded with Django 2.2.10 and DRF.

Description
-----------------------------------
1. The app uses `Pipenv` for a virtual environment.
2. As development DataBase it uses standart `SQLite` and 
for production it's `PostgreSQL`.

Installation
-----------------------------------
1. Copy the project with  
`git clone https://github.com/RamilPowers/poll_app.git .`
2. Create `environment_variables.py` file in `settings` direction. This file contains all secret variables.
2. Activate the Pipenv virtual environment with  
`pipenv shell`
3. Install packets with  
`pipenv install`
4. Make migrations with  
`python manage.py makemigrations`
5. Apply migrations with  
`python manage.py migrate`
6. And finally you can run the project  
`python manage.py runserver`

API Guide
-----------------------------------
##### URLs:  
1. **polls/** - list of all in progress polls `(GET)`
2. **polls/<<slug:poll_slug>>** - detail of poll `(GET, POST)`
3. **polls/get_result** - list of poll all completed polls by user `(GET)`

##### Take a Poll:  
Your POST request to `polls/<slug:poll_slug>` should be:  
```json
{
  "questions": [
        {
            "text": "Ну как там с деньгами?",
            "question_type": "1",
            "choices": [],
            "answer": "С какими деньгами?"
        }  
    ]
}
```
`Questions` object has questions with answer to them received from front-end.
So, after that POST-request the poll considered passed and User can find it at `polls/get_result` with his answers.  
`question_type` means type of the question:  
* 1 (`text`) - need to write your answer
* 2 (`Choose one`) - need to choose one answer of several
* 3 (`Choose many`) - need to choose multiple answers of several  

