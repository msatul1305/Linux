# GitHub & Git Guide

## I. Basic Git Workflow

1. Clone a repository: `git clone "url"`
2. Check status: `git status`
3. Switch branch: `git checkout "some branch"`
4. Stage changes: `git add .`
5. Commit changes: `git commit -m "something"`
6. Push to remote: `git push`

## II. Undoing Changes

### Undo `git add .` (remove all files from stage)
```bash
git reset
```

### Undo `git add` for a specific file
```bash
git reset <file>
```

### Explicitly remove a tracked file from git (e.g., config file)
```bash
git rm --cached path/filename
```

## III. Git Status & Information

### Get current branch
```bash
git status | grep 'On branch'
```

### View differences between current and last updated version of a file
```bash
git diff "filename"
```

### Get git diff line numbers where changes are made
```bash
git diff --unified=0 | grep -Po '^\+\+\+ ./\K.*|^@@ -[0-9]+(,[0-9]+)? \+\K[0-9]+(,[0-9]+)?(?= @@)'
```

### Get git config list
```bash
git config --list
```

## IV. Remote Synchronization

### Reset and sync local repository with remote branch
> **⚠️ Warning:** This command will destroy all local changes
```bash
git fetch origin && git reset --hard origin/master && git clean -f -d
```

## V. Branching

### List all branches
```bash
git branch -a
```

### Create a new branch from current branch
```bash
git checkout -b "new-branch_name"
```

### Get host ID for telnet
```bash
host "servername"
# Example: host MSI
```

## VI. Git Rebase vs Merge

See: https://www.atlassian.com/git/tutorials/merging-vs-rebasing

Both commands integrate changes from one branch into another branch.

### Merge Option
Merge the main branch into the feature branch:
```bash
git checkout feature
git merge main
```

Or as a one-liner:
```bash
git merge feature main
```

### Rebase Option
Rebase the feature branch onto the main branch:
```bash
git checkout feature
git rebase main
```

**Benefits of Rebasing:**
- Moves the entire feature branch to begin on the tip of the main branch
- Effectively incorporates all new commits from main
- Re-writes the project history by creating brand-new commits for each commit in the original branch
- Results in a much cleaner project history

**Interactive Rebasing:**
Interactive rebasing gives you the opportunity to alter commits as they are moved to the new branch.

## VII. Setting Up Git SSH

### Step 1: Generate SSH Key Pair
Open a terminal and run:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### Step 2: Add SSH Key to SSH Agent (Optional but recommended)
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### Step 3: Add SSH Key to Git Hosting Service
Copy the contents of your public key:
```bash
cat ~/.ssh/id_rsa.pub
```
Now go to your Git hosting service (GitHub, GitLab, Bitbucket, etc.) and add the SSH key in your account settings. It's usually found under "SSH and GPG keys" or a similar section.

### Step 4: Configure Git to Use SSH
```bash
git config --global user.email "your_email@example.com"
git config --global user.name "Your Name"
git config --global core.sshCommand "ssh -i ~/.ssh/id_rsa -F /dev/null"
```

### Step 5: Test the SSH Connection
```bash
ssh -T git@github.com
```

### Step 6: Clone Repositories Using SSH URL
```bash
git clone git@github.com:user/repo.git
```
