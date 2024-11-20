## Introduction

### **1. Git :**

  ![1_sOWIyC1rjrWSUdIS1KvyHw](https://github.com/user-attachments/assets/2803b762-d7f0-4800-888b-a68c81cf5795)

**Git** is a distributed version control system that allows developers to track changes on their codebase and collaborate with other developers. It provides a way to manage and track different versions of a project, making it easier to revert to previous versions if necessary. 

### **2. Github :**

![076ca4ab40fb5f03c83021bdea86443d](https://github.com/user-attachments/assets/60d36268-4af0-43ad-a206-d739df83e1b0)


**Github** is a web-based platform that provides hosting for Git repositories, along with additional features such as issue tracking, pull requests, and code reviews. It also enables collaboration between developers by allowing them to work on the same codebase together, using features such as branches and forks. 

- **Repositories :** A repository is a centralized location where you store and manage all the files and version history of your project, enabling collaboration and tracking of changes over time.


![image](https://github.com/user-attachments/assets/f5878655-ac0d-4b9d-8f3b-d0d450e22a48)

[Raghul-M - Github Profile](https://github.com/Raghul-M)

## Git Commands


![image](https://github.com/user-attachments/assets/6a7d64a3-1014-4df0-a884-da7bf8422146)



 **Git config :** **`git config`** is a command used to configure and manage Git settings on your computer. Git is a version control system commonly used for tracking changes in source code during software development. The **`git config`** command allows you to set, get, and list configuration variables for Git. These configuration variables can be set globally, per user, or per project/repository.

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "your@email.com"
```

 **Git init :** initializes a new Git repository in the current directory.

```bash
$ git init
```

**Git Clone** : Clone a remote repository to create a local copy.

```bash
$ git clone <repository_url>
```

**Git add** : Add changes or files to the staging area.

```bash
$ git add <filename>  [Or]
$ git add . #it will add all the files to staging area
```

**Git commit** : Commit changes in the staging area to the repository.

```bash
$ git commit -m "Commit message"
```

**Git status** : Show the status of files in the repository.

```bash
$ git status
```

**Git Log** : View the commit history.

```bash
$ git log
```

**Git pull** : Fetch and merge changes from a remote repository.

```bash
$ git pull origin <branch-name>
```

**Git push** : Push local changes to a remote repository.

```bash
$ git push origin <branch-name>
```

**Git branch** : List branches in the repository.

```bash
$ git branch (main or master is the main branch)
$ git branch feature (feature branch creation) [Or] git checkout -b feature
```

**Git checkout** : Switch to a different branch or commit.

```bash
$ git checkout <branch>
```

**Git Merge** : Merge changes from one branch into another.

```bash
$ git merge <source_branch> # feature to main
```

**Git fetch** : Fetch changes from a remote repository.

```bash
$ git fetch -all 
```

**Git remote** : Manage remote repositories. Nd show the changes in local and remote repos

```bash
$ git remote -v
```

**Git reset** : Unstage changes or move the HEAD to a different commit.

```bash
$ git reset <file> or git reset <commit>
```

**Git diff** : Show differences between commits, branches, or files.

```bash
$ git diff
```

**Git stash** : Temporarily save changes that are not ready to commit. it saves the changes in the backstage commit. whenever we want we make it front and commit

```bash
$ git stash - To backstage (First we need to add then stash)
$ git stash pop - Bringing the changes front 
$ git stash clear - To remove all
```

**Git remote add**: Add a remote repository.

```bash
$ git remote add <remote_name> <repository_url>
```

**Git remote remove**: Remove a remote repository.

```bash
$ git remote remove <remote_name>
```

**Git help** : Use it for more detailed information on each command's usage and options.

```bash
$ git help <command> 
```

**Git Squash** : Merge all commits into single commit, for that we use command 

```bash
$ git rebase -i <name of the commit>  #i - interactive environment
```



---

### **Git**

**Centralized VCS (SVN) vs Distributed Version Control System (Git)**

- Centralized VCS means everything depends on one server. If it is down, we can't access it. Devs need to depend on the central source.
- In Git, which uses a distributed VCS, we can take a copy of the central main source as our copy and store the changes there, which is called a fork (your copy of the main file). So, it is distributed, and we don't care about a single point of failure.

**Git vs GitHub**

- Git is a VCS tool and it is open source; anyone can download it.
- GitHub - usability, issues, contact, project management (GitLab, Bitbucket). It is a wrapper of Git to provide these functionalities.

```
💡 .git - Which has the Tracking Information of all Files
```
#### These are some of the most commonly used Git commands. 

```
-  git init (It creates the .git file to track history)
-  git add <filename>
-  git status
-  git diff
-  git commit -m "msg"
-  git log
-  git reset --hard <commit hash id>
-  git push
-  git clone <repo URL>
-  git remote -v [Remote reference]
-  git remote add <location URL .git>
-  git checkout -b <branch name> - create and move to branch
-  git branch
-  git log <branch name>
-  git cherry-pick <commit hash id>
-  git merge - Not a linear way; it combines on top of the main
-  git rebase - It will have a linear way so we have all the commits
```
```
💡 To write it in a single line ( git add . && git commit -m "" && git push )
```


**Git Authentication for Cloning**

- HTTPS uses a password or passkey
- SSH uses a public key (to create an SSH key - `$ ssh-keygen -t rsa`)

`git clone` is used to download the repository.
`git fork` is used to make a copy of the project to contribute or make individual development.

**Git Branching Strategy**

![image](https://github.com/user-attachments/assets/9e5f3bf1-6379-4743-9361-8ccbb501e810)


- `master` - which is the main branch of your source code
- `feature` branch - where the testing and additional features are added, and once tested and working properly, it's merged into the `master` or `main` branch.
- `release` branch - It is the branch going for production to customer use once the feature and code have been worked on and tested, so other updates can be directly merged into the `master` for the next release.
- `hotfix` or `bugfix` branch - where any critical bug or issue is addressed, the fix is tested, then it's merged into both `master` and `release` branches to avoid the critical issue. (It will go to both `master` and `release`).
