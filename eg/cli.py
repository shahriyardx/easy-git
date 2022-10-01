import subprocess

import click


@click.group(chain=True)
def cli():
    """Easy git cli"""


@cli.command("push")
@click.option("--msg", "-m", help="Commit message")
@click.option("--branch", "-b", help="Branch to push", default=None)
def push(msg, branch):
    """Push git repo"""
    if not msg:
        return print("[*] Commit message is required")
    
    subprocess.call(["git", "add", "."])

    commit_content = subprocess.check_output(["git", "commit", "-m", msg])
    print(commit_content.decode("UTF-8"))

    if branch:
        push_content = subprocess.check_output(["git", "push", "-u", "origin", branch])
    else:
        push_content = subprocess.check_output(["git", "push"])

    print(push_content.decode("UTF-8"))


@cli.command("init")
@click.option(
    "--msg", "-m", help="Commit message", default="Initialized using easy-git"
)
@click.option("--branch", "-b", help="Branch [main]", default="main")
@click.option("--origin", "-o", help="Repository url")
def init(msg, origin, branch):
    """Initialize git repo"""
    init_content = subprocess.check_output(["git", "init"])
    add_content = subprocess.check_output(["git", "add", "."])
    commit_content = subprocess.check_output(["git", "commit", "-m", msg])
    branch_content = subprocess.check_output(["git", "branch", "-M", branch])
    remote_content = subprocess.check_output(["git", "remote", "add", "origin", origin])

    print(init_content.decode("UTF-8"))
    print(add_content.decode("UTF-8"))
    print(commit_content.decode("UTF-8"))
    print(branch_content.decode("UTF-8"))
    print(remote_content.decode("UTF-8"))
