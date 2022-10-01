# Easy Git (eg)
Common git operations made simple

## initialize a new git repo
```sh
Command:
>> eg init

Options:
  -m, --msg     TEXT    Initial commit message
  -b, --branch  TEXT    Branch [main]
  -o, --origin  TEXT    Repository url

Example usage:
>> eg init -m "initial commit" -b branch_name -o https://github.com/shahriyardx/easy-git.git

What is does under the hood?
>> git init
>> git add .
>> git commit -m "initial commit"
>> git branch -M branch_name
>> git remote add origin https://github.com/shahriyardx/easy-git.git
```

## Pushing to a repo
```py
Command:
>> eg push

Options:
  -m, --msg     TEXT  Message
  -b, --branch  TEXT  Branch to push

Example Usage:
>> eg push -m "Updated something" -b branch_name

What it does under the hood?
>> git add . 
>> git commit -m "Updated Something"
>> git push -u origin branch_name
```