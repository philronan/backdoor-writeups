detroit-become-human
====================

Link: https://backdoor.sdslabs.co/challenges/Detroit-Become-Human \
Tags: [forensics] [frontdoorctf]

Description:
------------

Investigate unusual behaviour in a pcap file

Solution:
---------

The challenge text refers to two servers on the same PC that are behaving strangely. There seems to be a lot of traffic where the source and destination are both ports on [127.0.0.1](https://en.wikipedia.org/wiki/Localhost), so perhaps that's worth investigating.

If you're using [Wireshark](https://www.wireshark.org), you can block out all the other traffic by typing this into the filter toolbar:

```
(ip.src_host == 127.0.0.1) && (ip.dst_host == 127.0.0.1)
```

A lot of packets contain JSON data like this:

```
{"type": "event", "seq": 10, "event": "output", "body": {"output": "f", "category": "stdout", "source": {}}}
```

This looks like it's requesting a single character to be printed on `stdout`, which is rather odd. If you look at a few more of them, you'll notice that they're mostly the same, except that the `output` value changes to a different character each time. Let's filter out only the packets that contain the word "stdout". You can do this in Wireshark by changing the filter string to

```
(ip.src_host == 127.0.0.1) && (ip.dst_host == 127.0.0.1) && (data.text contains "stdout")
```

(If you don't see anything, you'll need to tell Wireshark it's OK to display packet data as text: Preferences &gt; Advanced &gt; data.show_as_text = TRUE.)

Can you see anything that looks like a flag yet?
