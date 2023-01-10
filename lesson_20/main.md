### git part 2

```
https://www.geeksforgeeks.org/git-difference-between-git-fetch-and-git-pull/#:~:text=Git%20Fetch%20is%20the%20command,changes%20into%20the%20local%20repository.
git pull  # download changes for current branch from internet to your local directory, git pull = git fetch + git merge
git fetch --all  # download all branches from remote repository

git branch  # shows you your current branch
git checkout -b <branchname>  # locally create new branch with copy of commits from your current branch
git checkout <branchname>  # switches to different already existing branch locally
git push -d <remote_name> <branchname>  # remove branch on remote
git branch -d <branchname>  # remove branch locally, -D for force

git mergetool  # opens some editor that you should use to resolve conflicts

git reset HEAD~2  # remove last 2 commits but keep the changes (files stay unchanged)
git reset --hard origin/master  # makes your local repo exact copy of master branch on remote repo

Monday:         master = A - B - C,             branch_A = A - B - C
Wednesday:      master = A - B - C - D - E - F  branch_A = A - B - C - a - b - c
git pull --rebase origin master  # downloads commits that were added to master after you've branched from it
git pull master  # same but from local repository (not remote)
after rebase:   master = A - B - C - D - E - F  branch_A = A - B - C - D - E - F - a - b - c
git merge origin/master
after merge:    master = A - B - C - D - E - F  branch_A = A - B - C - a - b - c - D - E - F - mrg_c_F

git rebase -i HEAD~3  # interactively update stuff about some of 3 commits
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit

git stash  # save modified changes into temporary stash
git stash -u  # save modified and new files changes into temporary stash
git stash pop  # apply changes from last stash into current branch 
git stash pop <stash_id>  # apply changes from specific stash into current branch
git stash list  # show all stashes
git stash show <stash_id>  # show contents of specified stash 

.gitignore
git cherry-pick <commit>  # copies one specific commit on top of current branch
```
