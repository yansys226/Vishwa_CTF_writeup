# **Bet Game**

We are provided with a binary and running it and playing with it, we found the flag.

```bash
$ ./game

HOW TO PLAY

1. You are given 500 coins
2. You need to place your bet
3. Next you have to guess a number between 0 to 9
4. You have 5 chances to guess the correct number
5. For a correct guess you ll win the bet amount
6. 5 consecutive incorrect guesses will result in deduction of bet amount from your account
7. To buy the flag you need to win 100000 coins
BEST OF LUCK!! (if you find it difficult to get the flag, take help from the Sage)


Press 1 to Play
Press 2 to buy the flag
Press 3 to exit
1
Place your bet: -100000
Enter your Guess: 0
Wrong guess
Enter your Guess: 0
Wrong guess
Enter your Guess: 0
Wrong guess
Enter your Guess: 0
Wrong guess
Enter your Guess: 0
Wrong guess
You have lost your bet. Random number was:  5  Try again
Account balance =  100500

Press 1 to Play
Press 2 to buy the flag
Press 3 to exit
2
Your account balance =  100500
Flag price =  100000
🎉🎉🎉
$tr!k3_!t_lu<ky
🎉🎉🎉
```

The vulnerability here is that they didn't check for negative bet, so you could just get "free" money by betting a negative value and losing. With this you can easily by the flag.

The flag we entered was: **VishwaCTF{$tr!k3_!t_lu<ky}**

---


