# Chainshare
#### Video Demo:  <URL HERE>https://youtu.be/ij1bNaX5TmU
#### Description:
Everyone has files, and it is important to keep those files from getting leaked to other sources. Whether it is for your friends or your manager, people are scared to upload files in fear of them getting leaked. Chainshare is a blockchain-based file sharing project that can send, view, and download your files by adding them to the blockchain. Blockchain is a decentralized technology that ensures the safety of each file.


Since the files are stored in the blockchain, no one can change or edit the block, which contains the details of each file and who it belongs to. Each block is connected to another block by the hash of the previous block, so editing a block will cause the chain to crash.


The program operates after identifying the user with the help of login/signup and running operations around that user so that they can view their uploaded files without going through the whole set of files. The admin can use the username 'hello' and password 'world' to view the chain to find the invalid block and remove it to recover the chain.


Using chainshare:
 - A user can view or download files that belong to them by picking choice 1.
 - We can upload files to another user or yourself by picking choice 2.
 - If you want reassurance that your files have not changed? choice 3 will validate the blockchain for you.


This project consists of two Python files named project.py, d_blockchain.py. The file project.py deals with main operations and functions such as uploading files, downloading, validation, etc, and d_blockchain.py deals with the blockchain algorithm and classes for storing files into the blockchain.


The project would be more user-friendly if it were executed as a web application where multiple people could access it at the same time from different locations, but since I wanted to present this project as fully pythonic, I used match to separate the choices for the users.


To keep the files from disappearing after closing the program, sqlite database is used.

Database file name:
 - data.db

The tables used are:
 - login:
   - The login table stores data related to users, such as username and password.
 - blockchain:
   - blockchain table stores each block from the blockchain in a row. A column represents a particular detail of each block.

functions, classes and methods:

**project.py**

 - **main:** main function for the project
 - **load_to_chain:** loads data stored in the table to the blockchain.
 - **login_or_signup:** return username if login/signup is successful, returns None if unsuccessful
 - **input_validation:** checks whether the username and password are appropriate or not.
 - **login:** login if the user is already in the database.
 - **signup:** sign up if the username is not in the database.
 - **view_files:** view files available for the user
 - **upload:** upload a file to a user by mentioning their username. This function generates a block in the blockchain and inserts it into the table.
 - **validate_files:** return True if the blockchain is valid, and False if it is invalid.
 - **view_chain:** prints out the details of each block in the blockchain (does not print out the binary file).
 - **f_name:** returns filename when the entire path is given as an argument.
 - **dowload_file:** writes a file from the blockchain

**d_blockchain.py**

 - **Block:** Block is a class, The variables in it store the details of the file and block.

   - **\_\_init__:** the constructor takes in arguments, and those values are assigned to the object variables.
   - **generate_hash:** generates a hash from the block object variables.
   - **\_\_str__:** used for printing the variables from each block object

 - **Blockchain:** Blockchain is a class that stores each block object and helps run various functions for the blockchain.

   - **\_\_init__:** the constructor takes in arguments, and those values are assigned to the object variables.
   - **add_block:** adds a block to the chain
   - **is_valid:** used to check whether the chain is valid or not. returns True if valid, else False
   - **mine:** used to generate a hash that starts with "0" times difficulty by incrementing the nounce and to connect prev_hash with the hash of the previous block before adding to the chain.








