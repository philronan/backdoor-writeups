john-cena
=========

Link: https://backdoor.sdslabs.co/challenges/John-Cena \
Tags: [steganography] [frontdoorctf]

Description:
------------

The challenge consists of a photo of wrestler John Cena, and a link to another image hosted at imgur.com showing a skeleton playing a trumpet (?).

Solution
--------

Adjusting the levels of the imgur file reveals a message at the bottom left saying "look at the top right corner". There also appears to be text hidden in the top right corner, but it's far too small to be legible.

I guess this is a clue to how the flag for this challenge can be found. Sure enough, applying a threshold filter to the John Cena image with a threshold level of about 15 or 16 clearly reveals the flag.

This challenge was far too easy.
