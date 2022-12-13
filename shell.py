import os


def deploy():
    os.system("git add .")
    os.system("git commit -m 'deploy'")
    os.system("git push")


def main():
    deploy()


if __name__ == "__main__":
    main()
