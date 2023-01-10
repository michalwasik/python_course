### git part 1

```
install windows terminal
install git through pycharm
git config --global core.editor "notepad"

https://stackoverflow.com/questions/20889346/what-does-git-remote-mean

ssh-keygen  # generate ssh key pair

git config --global user.name "John Doe"  # globally set your user info   
git config --global user.email johndoe@example.com  

git init  # make current directory a local git repository
git clone  # download git repository from internet

git remote add origin ...  # connect your git repository with git repository on the internet
git remote -v  # list url of git repository your project is connected to

git status  # show what's currently going on - what files you've changed, what's commited and what's now

git add -A  # add all locally changed/added/removed files to batch for commit
git commit -m 'commit message'  # create commit with batched changes with some comment
git commit --amend --no-edit  # adds new changes to previous commit
git push -u origin  # send your commit history to git repository on the internet
git push -f  # same as above but override remote history all at cost

git log  # shows all commits of current branch
```
