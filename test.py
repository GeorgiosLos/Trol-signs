def display_message(messagelines): 

    left_spacer = 0 

    right_spacer = 0 

 

    longestline = max(len(x) for x in messagelines) 

    if longestline > 13: 

        left_spacer = int((longestline - 13) / 2) 

        right_spacer = left_spacer + (longestline % 2 == 0) 

 

    lines = [(" " * 7) + (" " * left_spacer) + "\\|||/\n", 

             (" " * 6) + (" " * left_spacer) + "(o o)\n", 

             "|~" + ("~" * left_spacer) + "ooO~~(_)~~~~~" + ("~" * right_spacer) + "~|\n"] 

          

    for x in messagelines: 

        extra_space = max(longestline - len(x), 13 - len(x)) 

        lines += ["| " + x + (" " * extra_space) + " |\n"] 

 

    lines += ["'~" + ("~" * left_spacer) + ("~" * 10) + "Ooo" + ("~" * right_spacer) + "~'\n", 

              (" " * 5) + (" " * left_spacer) + "|__|__|\n", 

              (" " * 5) + (" " * left_spacer) + " || ||\n", 

              (" " * 5) + (" " * left_spacer) + "ooO Ooo"] 

    print(*lines) 

 

mlines = ["I WANT", "TO LEARN", "PYTHON !"] 

display_message(mlines) 

print() 

 

mlines = ["You need a bigger sign", "because this message is so", "long that it doesn't fit", "on the smaller ones !"] 

display_message(mlines) 

print() 

 

mlines = ["Python is the best language", "for beginner !", "Is easy to understand !"] 

display_message(mlines) 

print() 

 

mlines = ["See how easy it is", "to make any size message", "you want to appear", "on these TROLL signs !"] 

display_message(mlines) 

print() 