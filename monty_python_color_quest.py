color = input('What is your favorite color: \n')
print()
# Variable describes what I want the user input to look like.
result = input('Are you sure? Enter: yes or no ')
print()
if result.lower() == "yes":
    grail = input(
        "Good! What is your quest? Enter exactly: 'To find the Holy Grail!' Or Enter: 'I don't know!' ")
    # Using .lower() will lowercase the user's input so that it meets the if condition exactly.
    if grail.lower() == "to find the holy grail!":
        african = input(
            "What is the average wingspeed of a flying swallow? Enter exactly: I don't know! Or: African or European? ")
        # = is assigning  == is comparing
        if african.lower() == ("african or european?") or ('african' or 'european'):
            input("Wait, what? I don't know! *fling*")
            print("Congratulations! You may now cross the bridge!")
        else:
            print("Begone, foul naive! *fling!*")
    else:
        print("Begone, foul naive! *fling!*")
else:
    print("Begone, foul naive! *fling!*")
# Alt + Shift + f will autopep (autoformat) my script
