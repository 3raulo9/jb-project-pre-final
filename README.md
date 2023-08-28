
# John Brice - Full Stack project 7732/3 number 1

submited by: Raul Asadov

### Introducing my CRM website: A dynamic hub where businesses forge deeper customer connections.
### Uncover insights from data-driven interactions to enhance decision-making, elevate experiences, and drive growth.

1. download the project:

      link - https://github.com/3raulo9/jb-project-pre-final
      
3. create a virtual environment:
      ```
       python -m venv <virtual-environment-name>
      ```
      or
      ```
      conda create <virtual-environment-name>
      ```
4. activate virtual environment (on windows):
      ```
      <virtual-environment-name>\Scripts\activate.bat
      ```
      or
      ```
      conda activate <virtual-environment-name>
      ```
5. donwloading packages:
      1. location of the requirements file:
      - ```
        cd .\jb-project-pre-final\JBcrmProject\
        ```
      2. donwload requirments:
      - ```
        pip install -r requirements.txt
        ```
6. now to activate the project you need to do the following -
      (check that you're in the right directory)
      ```
      cd .\jb-project-pre-final\JBcrmProject\
      ```
      1. migrate models:
            1. ```
                  python.exe .\manage.py migrate
                  ```
            2. ```
                  python.exe .\manage.py makemigrations
                  ```
            3. ```
                  python.exe .\manage.py migrate
                  ```
      2. create super user (admin):
      - ```
        python.exe .\manage.py createsuperuser
        ```
      
      3. **run server:**
      - ```
        python.exe ./manage.py runserver
        ```

## Project models

There is only one model the project

Record: ```
        - created_at 
        - first_name 
        - last_name 
        - email 
        - phone 
        - address 
        - city 
        - state
        - zipcode 
        ```
