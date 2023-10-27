# SafeMarketplace

## Run the Web App

### Deploy app in dev mode without nginx and wsgi

1. Bulid app before first run:

```bash
sudo docker compose -f docker-compose.yml build
```
2. Run app
```bash
sudo docker compose -f docker-compose.yml up
```
3. Add permission for accessing local media by app
```bash
sudo chmod -R a+rwx ./data
```
4. Turn off app
```bash
sudo docker compose -f docker-compose.yml down --volumes
```

### Deploy full app in production mode

1. Bulid app before first run:
```bash
sudo docker compose -f docker-compose-deploy.yml build
```
2. Run app
```bash
sudo docker compose -f docker-compose-deploy.yml up
```
4. Turn off app
```bash
sudo docker compose -f docker-compose-deploy.yml down --volumes
```

## Way of work

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
