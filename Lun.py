import discord
import Functions
import asyncio
from Chess import Chess

client = discord.Client()
test = Chess()
lun = '<@!720307801091735623>'
mlun = '<@720307801091735623>'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='smarter than you | @Lun'))


@client.event
async def on_message(message):
    message.content = message.content.lower()

    async def print_formatted_board(formatted_board):
        split_board = formatted_board.split('\n')
        split_board.remove('')
        if test.white_turn:
            for i in range(len(split_board)):
                await message.channel.send(split_board[i] + Chess.rank_list[7 - i])
            await message.channel.send(Chess.white_files)
        else:
            for i in range(len(split_board)):
                await message.channel.send(split_board[i] + Chess.rank_list[i])
            await message.channel.send(Chess.black_files)
            # if i == 3:
                # await asyncio.sleep(4.5)

    if message.author == client.user:
        return
    if message.content.startswith(lun + " factorial ") or message.content.startswith(mlun + " factorial "):  # factorial
        if message.content.startswith(lun + " factorial "):
            string_integer = message.content.replace(lun + " factorial ", '')
        else:
            string_integer = message.content.replace(mlun + " factorial ", '')
        try:
            integer = int(string_integer)
        except:
            await message.channel.send("Please enter an integer value n for 'lun factorial n'.")
        if integer >= 808:
            await message.channel.send("Number exceeds Discord's character limit. Stick to factorial 807 or lower.")
        elif integer < 0:
            await message.channel.send("Undefined.")
        else:
            factorial = Functions.factorial(integer)
        await message.channel.send(factorial)
    if message.content.startswith(lun + " sentiment ") or message.content.startswith(mlun + " sentiment "):  # sentiment analysis
        if message.content.startswith(lun + " sentiment "):
            string = message.content.replace(lun + " sentiment ", '')
        else:
            string = message.content.replace(mlun + " sentiment ", '')
        await message.channel.send(Functions.sentiment_analysis(string))
    if message.content.startswith(lun + " combinations ") or message.content.startswith(mlun + " combinations "):  # combinations
        if message.content.startswith(lun + " combinations "):
            string = message.content.replace(lun + " combinations ", '')
        else:
            string = message.content.replace(mlun + " combinations ", '')
        string_list = string.split(",")
        try:
            n = int(string_list[0])
            r = int(string_list[1])
        except:
            await message.channel.send("Please request in format n, r.")
        if n < r or n < 0 or r < 0:
            await message.channel.send("Please enter n >= r >= 0.")
        else:
            await message.channel.send(Functions.combinations(n, r))
    if message.content.startswith(lun + " help") or message.content.startswith(mlun + " help"):  # help
        await message.channel.send("**Current commands list:**\n"
        + "sentiment <phrase>: Analyzes phrase and returns a sentiment value. (-1 most negative, 1 most positive.)\n"
        + "factorial <integer>: Returns the factorial of a given integer.\n"
        + "combinations <n, r>: Returns number of ways to choose sample of size r from n objects.\n"
        + "flip: Flips a coin.\n"
        + "yesorno <question>: Lun answers a yes or no question.\n"
        + "chess: Play chess with a friend!\n")
    if message.content.startswith(lun + " flip") or message.content.startswith(mlun + " flip"):
        await message.channel.send(Functions.coin_flip())
    if message.content.startswith(lun + " commanderfailure") or message.content.startswith(mlun + " commanderfailure"):
        await message.channel.send(" is a nerd.")
    if message.content.startswith(lun + " yesorno ") or message.content.startswith(mlun + " yesorno "):
        await message.channel.send(Functions.magic_eight_ball())
    if message.content.startswith(lun + " chess"):
        test.in_game = True
        await message.channel.send("Tag me with 'quit' at any time (after white and black have been assigned) to quit.\n"
                                   + "White, tag me with 'white': \n")
    if message.content.startswith(lun + " white") and test.in_game:
        test.white_id = message.author.id
        await message.channel.send("White is: <@!" + str(message.author.id) + ">")
        await message.channel.send("Black, tag me with 'black': \n")
    if message.content.startswith(lun + " black") and test.white_id and test.in_game:
        test.black_id = message.author.id
        test.white_turn = True
        await message.channel.send("Black is: <@!" + str(message.author.id) + ">. Game on.")
        await print_formatted_board(test.format_board())
    if message.content.startswith(lun + " move ") and test.in_game:
        clean = message.content.replace(lun + " move ", '')
        cleaner = clean.replace(" ", '')
        position = cleaner.split(",")
        if message.author.id == test.white_id:
            if test.white_turn:
                if test.move(test.filerank_to_integer(position[0]), test.filerank_to_integer(position[1]), True):
                    test.white_turn = not test.white_turn
                    await print_formatted_board(test.format_board())
                else:
                    await message.channel.send("Have you... played chess before? Invalid move.")
            else:
                await message.channel.send("It's not your turn, dummy.")
        if message.author.id == test.black_id:
            if not test.white_turn:
                if test.move(test.filerank_to_integer(position[0]), test.filerank_to_integer(position[1]), True):
                    test.white_turn = not test.white_turn
                    await print_formatted_board(test.format_board())
                else:
                    await message.channel.send("Have you... played chess before? Invalid move.")
            else:
                await message.channel.send("It's not your turn, dummy.")
        if message.author.id != test.black_id and message.author.id != test.white_id:
            await message.channel.send("<@!" + str(message.author.id) + "> Stop backseat gaming!")
    if message.content.startswith(lun + " quit") and test.in_game:
        if message.author.id == test.white_id or message.author.id == test.black_id:
            await message.channel.send("GG.")
            test.board = ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook',
             'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
             'white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
            test.white_id = ''
            test.black_id = ''
            test.in_game = False
    print(message.content)
    # if message.content.startswith("<@!720307801091735623> emoji"):
        # await print_formatted_board(test.format_board(test.board))

    # if message.content.startswith("lun permutations")
    # if message.content.startswith("lun word_cloud")
    # if message.content.startswith("lun youtube")
    # hi key contributor bunnyhops


with open('lun_key.txt') as f:
    key = f.read()
client.run(key)
