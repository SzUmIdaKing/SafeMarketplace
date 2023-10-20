# SafeMarketplace
### Installation process 
1. Install the required dependencies using Poetry:

```bash
poetry install
poetry shell
```
<!--
2. Only before firs run:
 To jest komentarz 

```bash
cd puddle/
python3 manage.py makemigrations
python3 manage.py migrate
```
-->
   
2. Run the Web App:

```bash
cd puddle/
python3 manage.py runserver
```

### Way of work
1. Work allways on your branch

```bash
git checkout <your branch name>
```

2. Allways push your changes after finished work

```bash
git add
git commit -m "message"
git push origin <your branch name>
```

3. Before merge into main, get changes from main into your branch 
```bash
git checkout main
git pull origin main
git checkout <your branch name>
git merge main
code . (to resolve merge conflicts)
git add
git commit
git push origin <your branch name>
git checkout main
git merge <your branch name>
git push origin main 
```
