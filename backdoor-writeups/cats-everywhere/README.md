cats-everywhere
===============

Link: https://backdoor.sdslabs.co/challenges/CATS-EVERYWHERE \
Tags: [backdoorctf18] [misc]

Description:
------------

Something about cats, and a mystery file for you to download.

Solution:
---------

The file appears to be plain ASCII text:

```
$ file challenge
challenge: ASCII text
```

It's rather large, though. Let's take a look at the first few lines:

```
$ head challenge
UEsDBBQAAAAAAIUgbkwAAAAAAAAAAAAAAAAFACAAbWlzYy9VVA0AB+NRqFrOI6laySOpWnV4CwAB
BOgDAAAE6AMAAFBLAwQUAAgACAB5H25MAAAAAAAAAABsuQAAIgAgAG1pc2MvMV8yNHoybHRESWNZ
dm5VT3J3bmxTV3BRLmpwZWdVVA0AB99QqFrxUahawCOpWnV4CwABBOgDAAAE6AMAALy7B1xT37Yu
Gpp0kCYdVJAiINJEakD+FEG69BIVEBABARGEkKAICAIRFJAiVaQb6Z1IR0A6RDqE3hNKCKRw497n
7rP3Ofec+979vXfXLwNW1pzJmmPOMcY3vjVmzn+fzwDeAKgoKf+8yAc1+UVDR0NDTU3DQEt7gY6J
gYmJkYGRkZmF/SIzCxsLI+PFSxfZODi5uLiYWLl5LnHysHNycVJQkftT09DT0NBzMjMyc/6/Ps5/
ANjoKJ0of1BRXAVQslFQsVGcd1LkAQAUNBR/OwD/dlBQksd3gZaOnoHxIoCSgoqKkprqz2jJLWHk
NgA1Gw37FTntCxzmD2mv+nHKv0rMpRO5U9HGZTGCFlV45P+anuESNw8v3zUxcQnJ64pKt5Rvq6jq
/KWrp29w19DyvpW1ja2dvYur22N3D88nAc8DXwQFvwyJeBMZFf02Jjbpw8fklNRPael5+V8KvhYW
FZdUVlXX1NbVNzS2d3R2dff0/uwbHRufmET+nppeQi2vrK6tb2xuYQ4Oj46xJ7jTMwoAFcX/PP6T
```

OK, this is clearly base64-encoded. We can undo that easily enough:

```
$ base64 -D <challenge >wtf
$ file wtf
wtf: Zip archive data, at least v2.0 to extract
```

Now we have a zip archive. Rename it, and then open it up:

```
$ mv wtf cats.zip
$ unzip cats.zip
Archive:  cats.zip
   creating: misc/
  inflating: misc/1_24z2ltDIcYvnUOrwnlSWpQ.jpeg  
  inflating: misc/walk-3.gif         
  inflating: misc/19ff057a44865be8b008edf35debe550.jpg  
  inflating: misc/411b043d2e9ec5ac5bb5d247363cdb1f.png  
  inflating: misc/images.png         
  inflating: misc/images.jpeg        
   creating: misc/.git/
   creating: misc/.git/branches/
  inflating: misc/.git/description   
  inflating: misc/.git/config        
  inflating: misc/.git/COMMIT_EDITMSG  
...etc...
```

Most of the files are part of a git repository, and the few image files outside it don't provide any clues. We need to delve inside the git repository to get this flag.

I find that a GUI makes this task much easier. (Try [SourceTree](https://www.sourcetreeapp.com/), for example.) Straight away you'll see a series of commits called "Welcome", "to", "Backdoor", "CTF", "2018" and ".". Each of them replaces an image fragment. Extract these fragments and stitch them together to retrieve the flag.
