isolve
======

Link: https://backdoor.sdslabs.co/challenges/ISOLVE \
Tags: [backdoorctf16] [misc]

Description:
------------

Get a flag by scoring full marks in an online quiz.

Solution:
---------

Each question presents you with a regular expression, then asks you to provide a string that matches this pattern. Like this, for example:

```
################################
#######     ROUND 0        #####
################################


Your regex:
[^falkmeo,]+e[^ol]+


Pass your solution:
```

I'll assume you understand how regular expressions work, and that `Brexit is a stupid idea` is an example of a string that matches the regular expression `[^falkmeo,]+e[^ol]+` (surely that's something that doesn't need any explanation?). If not, you'll have to do a bit of studying elsewhere.

I suppose if you're a fast thinker and a quick typist, then you might be able to crack this challenge simply by typing in the answers at the command line console. However, you only get ten seconds for each question. As soon as you get a question wrong or take longer than 10 seconds to answer, the game ends.

Now you're probably thinking to yourself that it might be a bit of a pain to write a program that can parse regular expressions and generate strings that match them straight away. And you'd probably be right. The setter of this challenge apparently thought to too — the questions aren't randomly generated at all. There are only 48 of them, and the only thing that changes is the order in which they are presented.

So if you can't solve this challenge by typing away on the fly (I couldn't), then you'll need to write a program that connects to the server and fetches a response corresponding to each question as it comes. Python's `socket` module is perfect for this.

This is Python v2 code. It's a mess, but it sort-of works. Every time you answer a new question, add a matching case to the `make_regex()` function so you don't have to enter it again.

```python
def make_regex(s):
    s = s.strip()
    if s == r"[^falkmeo,]+e[^ol]+": return "Brexit is a stupid idea"
    # Insert more lines here!
    # Return empty string if nothing matches
    return ""


def run():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(("hack.bckdr.in", 7070)) # changed to 17007
    sock.connect(("hack.bckdr.in", 17007))
    done = False
    while True:
        solution = ""
        while True:
            try:
                # Fetch a chunk of text from the server
                s = sock.recv(1024).strip()
            except:
                print "(Connection closed)"
                return
            # The regular expression follows this line:
            p = s.find("Your regex:")
            if p>=0:
                # Extract the regular expression and return a
                # corresponding answer (if available)
                solution = make_regex(s[p+12:s.find('\n',p+13)])
            if len(s)>0:
                # Echo non-blank lines to the console as feedback
                print ":%s" % s
            if "your solution" in s:
                # break from this loop when the server ready for the answer
                break
            if "Dying, too much time" in s or "Failed regex" in s:
                # You failed the test :-(
                return
        if solution == "":
            # If you have no solution, type one in quickly!
            print '%' * 53
            print 'HELP! SOLUTION UNAVAILABLE. PLEASE TYPE IN AN ANSWER:'
            print '%' * 53
            r = raw_input()
            solution = r
        else:
            # Otherwise answer the question
            print solution
        sock.send(solution + "\n")
```
