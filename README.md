# SafeMarketplace
### Run the Web App
1. If you run app first time:

```bash
docker compose build
```
2. Run app
```bash
docker compose up
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
