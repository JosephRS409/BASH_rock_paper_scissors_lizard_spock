#!/usr/bin/bash 

# computer function

computer_function () {

computer=$(( ( RANDOM % 5 ) + 1 )) 

if (( $computer == 1 ))
then
	echo "Computer chose #1 Rock"

elif (( $computer == 2 ))
then
	echo "Computer chose #2 Paper"

elif (( $computer == 3 ))
then
	echo "Computer chose #3 Scissors"

elif (( $computer == 4 ))
then
	echo "Computer chose #4 Lizard"

elif (( $computer == 5 ))
then
	echo "Computer chose #5 Spock"
fi

}

#Computer function must return what it generates!!!
#When comp called set var in while called comp = to func call
# computer=computer_function
#This should create var. called computer for other funcs.


# compare function

compare_function () {

# input="$1"
# computer=computer_function

if [[ $input == 3 && $computer == 2 ]]
then
	echo "Congratulations, you win!"

elif [[ $input == 2 && $computer == 1 ]]
then
	echo "Congratulations, you win!"

elif [[ $input == 1  &&  $computer == 4 ]]
then
	echo "Congratulations, you win!"
		 
elif [[ $input == 4  &&  $computer == 5 ]]
then
	echo "Congratulations, you win!"
		 
elif [[ $input == 5 && $computer == 3 ]]
then
	echo "Congratulations, you win!"
		 
elif [[ $input == 3 && $computer == 4 ]]
then
	echo "Congratulations, you win!"

elif [[ $input == 4 && $computer == 2 ]]
then
	echo "Congratulations, you win!"
		 
elif [[ $input == 2 && $computer == 5 ]]
then
	echo "Congratulations, you win!"

elif [[ $input == 5 && $computer == 1 ]]
then
	echo "Congratulations, you win!"
		 
elif [[ $input == 1 && $computer == 3 ]]
then
	echo "Congratulations, you win!"

elif [[ $input == $computer ]]
then
	echo "You tied! Try again."

else 
	echo "Too bad. You lose!"

fi

}



# human input variable

process_input () {

	if (( $input == 1 ))
	then
		echo "You chose #1 Rock"

	elif (( $input == 2 ))
	then
		echo "You chose #2 Paper"

	elif (( $input == 3 ))
	then
		echo "You chose #3 Scissors"

	elif (( $input == 4 ))
	then
		echo "You chose #4 Lizard"

	elif (( $input == 5 ))
	then
		echo "You chose #5 Spock"

	fi

}
		

# functions or loops

# one big loop - "game loop" a.k.a. framerate

# IN loop "Welcome"
# OUT loop "Goodbye"

# prompt user - process info

# prompt user
# process input
# generate result


echo "
Welcome to Rock, Paper,
Scissors, Lizard, Spock!

"

echo "A Simple Way to Remember
Who Wins:

Scissors cuts paper.
Paper covers rock.
Rock crushes lizard.
Lizard poisons Spock.
Spock smashes scissors.
Scissors decapitates lizard.
Lizard eats paper.
Paper disproves Spock.
Spock vaporizes rock.
Rock crushes scissors.

"

while true
do


	
	read -p "Enter any of the 
following numbers to
make a choice:
	
ROCK      = 1
PAPER     = 2
SCISSORS  = 3
LIZARD    = 4
SPOCK     = 5

EXIT GAME = 6

" input

	if (( $input == 6 ))
	then
		break

	elif [[ "$input" == 1 || "$input" == 2 || "$input" == 3 || "$input" == 4 || "$input" == 5 ]]

#(( $input == {1..5} ]]
# (( $input != 6 ]]

	then

		process_input
		computer_function 
		compare_function
	
	else
		echo "Invalid answer.
Please try again, or go away.

"

	fi

done
	echo "Goodbye for now!"

