import subprocess
import click

@click.group(chain=True)
def cli():
    """Easy git cli"""


@cli.command("push")
@click.option("--msg", "-m", help="Message", default=None)
@click.option("--branch", "-b", help="Branch to push", default=None)
def push(msg, branch):
    """Push git repo"""
    subprocess.call(['git', 'add', '.'])

    if (msg):
        commit_content = subprocess.check_output(['git', 'commit', '-m', msg])
        print(str(commit_content))
    
    if branch:
        push_content = subprocess.check_output(['git','push', '-u', 'origin', branch])
    else:
        push_content = subprocess.check_output(['git','push'])
    
    print(str(push_content))


@cli.command("init")
@click.option("--msg", "-m", help="Initial commit message", default="Initialized using easy-git")
@click.option("--branch", "-b", help="Branch [main]", default="main")
@click.option("--origin", "-o", help="Repository url")
def init(msg, origin, branch):
    """Initialize git repo"""
    init_content = subprocess.check_output(['git', 'init'])
    add_content = subprocess.check_output(['git', 'add', '.'])
    commit_content = subprocess.check_output(['git', 'commit', '-m', msg])
    branch_content = subprocess.check_output(['git', 'branch', '-M', branch])
    remote_content = subprocess.check_output(['git', 'remote', 'add', 'origin', origin])
    
    print(str(init_content))
    print(str(add_content))
    print(str(commit_content))
    print(str(branch_content))
    print(str(remote_content))
