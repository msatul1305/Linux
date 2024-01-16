I. Basic flow:
  1. git clone "url"
  2. git status
  3. git checkout "some branch"
  4. git add .
  5. git commit -m "something"
  6. git push

II. To undo git add . (remove all files from stage):
  git reset

III. To undo git add to specific file:
  git reset <file>
  
IV. Explicitly remove a tracked file from tracking in git(like a config file):
  git rm --cached path/filename
  
V. get current branch:
  git status | grep 'On branch'
  
VI. difference between current version and last updated version of a file:
  git diff "filename"
  
VII. get config list:
    git config --list

Get git diff line numbers where changes are made: git diff --unified=0 | grep -Po '^\+\+\+ ./\K.*|^@@ -[0-9]+(,[0-9]+)? \+\K[0-9]+(,[0-9]+)?(?= @@)' 

Reset and sync local repository with remote branch:
Note: This command will destroy all local changes 
git fetch origin && git reset --hard origin/master && git clean -f -d
get host id to do telnet: host "servername"
e.g. host MSI


VIII. Git rebase vs merge: https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Both of these commands are designed to integrate changes from one branch into another branch.
- The Merge Option 
  - The easiest option is to merge the main branch into the feature branch using something like the following:
    git checkout feature
    git merge main
    Or, you can condense this to a one-liner:
    git merge feature main
  - As an alternative to merging, you can rebase the feature branch onto main branch using the following commands:
  git checkout feature
  git rebase main
    - This moves the entire feature branch to begin on the tip of the main branch, 
    - effectively incorporating all the new commits in main. 
    - But, instead of using a merge commit, rebasing re-writes the project history by creating brand-new 
      commits for each commit in the original branch.
    - The major benefit of rebasing is that you get a much cleaner project history. 
  - Interactive Rebasing: Interactive rebasing gives you the opportunity to alter commits as they are moved to the new branch.

- Set up git SSH
  - Step 1: Generate SSH Key Pair
    - Open a terminal on your local machine and run the following command to generate an SSH key pair:
    - ```ssh-keygen -t rsa -b 4096 -C "your_email@example.com"```
  - Step 2: Add SSH Key to SSH Agent (Optional but recommended)
    - ```eval "$(ssh-agent -s)"```
    - ```ssh-add ~/.ssh/id_rsa```
  - Step 3: Add SSH Key to Git Hosting Service
    - Copy the contents of the public key (~/.ssh/id_rsa.pub) using the following command:
      - ```cat ~/.ssh/id_rsa.pub```
    - Now, go to your Git hosting service (e.g., GitHub, GitLab, Bitbucket) and add the copied SSH key in your account settings. 
    - It's usually found under "SSH and GPG keys" or a similar section.
  - Step 4: Configure Git to Use SSH
    - Open a terminal and run the following commands to configure Git to use SSH:
    - ```git config --global user.email "your_email@example.com"```
      ```git config --global user.name "Your Name"```
      ```git config --global core.sshCommand "ssh -i ~/.ssh/id_rsa -F /dev/null"```
  - Step 5: Test the SSH Connection
    - ```ssh -T git@github.com```
  - Step 6: to clone repositories using the SSH URL:
    - ```git clone git@github.com:user/repo.git```
