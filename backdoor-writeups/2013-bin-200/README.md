2013-bin-200
============

Link: https://backdoor.sdslabs.co/challenges/2013-BIN-200 \
Tags: [reversing]

Description:
------------

Extract a flag from a Windows executable file.

Solution:
---------

Use `strings` to look for clues inside the file. The output is surprisingly short:

```
$ strings project1.exe
!This program cannot be run in DOS mode.
Rich
.text
`.data
.rsrc
MSVBVM60.DLL
h(6@
Project1
zs:O
Form1
Form1
Form1
Picture1
BMF#
Command1
Submit
Text1
8P8&k
Label3
Label2
Enter Registration Key to Unlock
Label1
Protected Software
MS Sans Serif
VB5!
Project1
Project1
Project1
Form1
Project1
zsfn
Form
C:\Program Files (x86)\Microsoft Visual Studio\VB98\VB6.OLB
Command1
Label1
Label2
Text1
Label3
Picture1
MSVBVM60.DLL
MethCallEngine
EVENT_SINK_AddRef
EVENT_SINK_Release
EVENT_SINK_QueryInterface
__vbaExceptHandler
1u  
```

The label `Picture1` followed by `BM` (a TIFF signature) suggests that there is an image lurking inside this file. Sure enough, if you delete the first 0x114e bytes of this file and save it as a TIFF image, then you'll get the flag.
