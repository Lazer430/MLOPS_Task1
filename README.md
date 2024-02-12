
# MLOPS_Task1

This repository is to practice github commands and simulate a simple team project. 

## Authors

- [@Lazer430 (i200432)](https://github.com/Lazer430) 
- [@AhsanRasheed (i200474)](https://github.com/ahsanrbaloch)

## Task

### Step 1: Create Github Repo
Here we open Github and create a new public repository.
Then we add the team members as collaborators.
### Step 2: Clone the repository
Create a folder named MLOPS_Task1 and clone the repository:
```
git clone https://github.com/Lazer430/MLOPS_Task1.git
```

### Step 3: Set up the scaffolding for the flask project
Here we set up the folder structure as follows:
```
app.py
/templates/index.html
/static/style.css
```
### Step 4: Stage the scaffolding and commit
```
git add .
git commit -m "initial commint"
git status
```

The output was:
```
PS C:\Users\fasih\OneDrive\Desktop\MLOPS\Task1\MLOPS_Task1> git add .
PS C:\Users\fasih\OneDrive\Desktop\MLOPS\Task1\MLOPS_Task1> git commit -m "initial commit"
[main de9cdd4] initial commit
 3 files changed, 33 insertions(+)
 create mode 100644 app.py
 create mode 100644 static/style.css
 create mode 100644 templates/index.html
PS C:\Users\fasih\OneDrive\Desktop\MLOPS\Task1\MLOPS_Task1> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
### Steo 5: Push the initial commit to main
```
git push origin main
```

Output:
```
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 885 bytes | 442.00 KiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Lazer430/MLOPS_Task1.git
   2e80c62..de9cdd4  main -> main
```
### Step 5: Create the dev branches
Here we make the dev branch from main and then use that as a template for branches i200432 and i200474.

### Step 6: Checkout to branch
```
git checkout -b i200432_FasihAbdullah
git checkout -b i200474_AhsanRahseed
```

### Step 7: Make changes in individual branch
Here both of us write some code in our branches and push changes.

```
git add .
git commit -m "feature XYZ"
git push origin i200432_FasihAbdullah
```
```
git add .
git commit -m "feature XYZ"
git push origin i200474_AhsanRahseed
```
### Step 8: Merge Branches with dev
Ahsan made changes, pushed to his branch and made a pull request from his branch to dev.

Fasih pulled from dev, added his code, pushed to his branch and made a pull request from his branch to dev.

### Step 9: Test branch
Made test branch from dev after code was finalized. Code was tested manually.

### Extra commands used/tried
```
git checkout -b main
git branch -d dev
git fetch
git status
git pull origin dev:i200432_FasihAbdullah
git log
git annotate
```
