from cs50 import *
from d_blockchain import *


def main():
    global db, blockchain

    # object to run database queries
    db = SQL("sqlite:///data.db")

    # loading the blockchain
    blockchain = load_to_chain()

    if blockchain:
        choices = (
            "\n1.View files\n2.Upload files\n3.Validate the chain\n4.Log out\n5.Exit\n"
        )
        login = None

        while True:
            if login == None:
                login = login_or_signup()
            else:
                # return false if blockchain is invalid
                if not blockchain.is_valid():
                    print("not valid blockchain")
                    return False
                choice = get_int("\nEnter the choice: " + choices)
                match choice:
                    case 1:
                        view_files(login)
                    case 2:
                        upload()
                    case 3:
                        validate_files()
                    case 4:
                        login = None
                    case 5:
                        break
                    case _:
                        print("enter a valid choice\n")


# loads data from the table to the blockchain
def load_to_chain():
    temp_chain = []
    data = db.execute("SELECT * FROM blockchain")
    for row in data:
        temp_block = Block(
            row["file_name"],
            row["data"],
            row["reciever"],
            row["index"],
            row["nounce"],
            row["prev_hash"],
        )
        temp_chain.append(temp_block)
    return Blockchain(temp_chain)


def login_or_signup():
    choice = input("\nPress 1 to login\nPress 2 to signup\n")

    if choice != "1" and choice != "2":
        print("enter valid choice")
        return None
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # returns None if inputs are invalid
    if not input_validation(username, password):
        return None
    if username == "hello" and password == "world":
        view_chain()
        return None

    # query for logging in
    res = db.execute(
        "SELECT count(*) AS c FROM login WHERE username = ? AND password = ?",
        username,
        password,
    )

    # query to check if the user is already logged in
    res_1 = db.execute("SELECT count(*) AS c FROM login WHERE username = ?", username)
    match choice:
        case "1":
            return login(res[0]["c"], username)
        case "2":
            return signup(res_1[0]["c"], username, password)


def input_validation(username, password):
    # returns False if the username or password are short
    if len(username) < 3 or len(password) < 3:
        print("Enter atleast 3 letters for username and password")
        return False

    # returns False if the username or password are not alphanumeric
    if not (username.isalnum() and password.isalnum()):
        print("Only alowed to use Numbers and alphabets")
        return False

    return True


def login(res, username):
    if res == 1:
        print("Logged in successfully")
        return username
    else:
        return None


def signup(res, username, password):
    if res != 0:
        print("Username is already taken")
        print("Signup again to continue")
        return None
    else:
        if __name__ == "__main__":
            db.execute("INSERT INTO login VALUES(?, ?)", username, password)
        print("Signed up successfully")
        return username


# view files of the user and dowloads it if necessary
def view_files(username):
    if blockchain:
        # files of the user logged in
        res = db.execute(
            "SELECT file_name FROM blockchain WHERE reciever = ?", username
        )
        if res:
            for i in res:
                print("File name:", i["file_name"])
            while True:
                choice = input("\nDo you want to download files yes/no: ")
                if choice in ["no", "n"]:
                    break
                elif choice in ["yes", "y"]:
                    dowload_file(username, res)
        else:
            # if the user has no file
            print(f"No results for {username}")


# sends or upload user's files
def upload():
    # uploads to the given username
    reciever = input("Enter the username of the reciever: ")
    while not input_validation(reciever, "1234"):
        reciever = input("Enter the username of the reciever: ")

    path = input("Enter the file path: ")

    # returns filename from path
    file_name = f_name(path)

    # read the file in binary format
    try:
        with open(path, "rb") as file:
            data = file.read()
    except FileNotFoundError:
        print("invalid path")
        return

    # if mining is successfull, insert block into the database
    if blockchain.mine(Block(file_name, data, reciever)):
        l_block = blockchain.chain[-1]
        db.execute(
            "INSERT INTO blockchain VALUES(?, ?, ?, ?, ?, ?, ?)",
            l_block.file_name,
            l_block.data,
            l_block.reciever,
            l_block.nounce,
            l_block.index,
            l_block.hash,
            l_block.prev_hash,
        )
        print("Successfully added", file_name)
    else:
        print("invalid blockchain")


# validates the blockchain
def validate_files():
    if blockchain.is_valid():
        print("The block chain is valid")
        return True
    else:
        print("The block chain is not valid")
        return False


# view the block chain if logged in successfully
def view_chain():
    for i in blockchain.chain:
        print(i)
    print("")


# returns file name from path given
def f_name(path):
    if "/" in path:
        file_name = path.split("/")
    elif "\\" in path:
        file_name = path.split("\\")
    else:
        file_name = [path]
    return file_name[-1]


# dowloads selected files
def dowload_file(user, files):
    for i in files:
        print("File name:", i["file_name"])
    file_name = input("Enter the file name to download: ")
    block_data = db.execute(
        "SELECT * FROM blockchain WHERE file_name = ? AND reciever = ?", file_name, user
    )
    if block_data:
        for i in block_data:
            with open(i["file_name"], "wb") as file:
                file.write(i["data"])
        print("Successfully downloaded")
    else:
        print(f"No such files as {file_name}")


if __name__ == "__main__":
    main()
