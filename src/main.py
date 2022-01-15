import sys
from bot.bot import discord_client

def main():
    token = ''
    if len(sys.argv) < 2:
        print('Please add the token file path.')
        return
    with open(sys.argv[1], encoding='UTF-8') as ifile:
        token = ifile.read()
    discord_client.run(token)

if __name__ == '__main__':
    main()