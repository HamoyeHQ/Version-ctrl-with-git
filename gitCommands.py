def git_commands(*commands):
    print('These are some commands to use when working wit git and github:')
    for command in commands:
        print(command)

git_commands('git init','git add','git status','git remote','git checkout','git log','git push')