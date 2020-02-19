bossfight
=========

Link: https://backdoor.sdslabs.co/challenges/bossfight \
Tags: [n00b19CTF] [pwn]

Description:
------------

Some sort of Pokémon game. I know next to nothing about Pokémon.

Solution:
---------

The executable file for this game is available to download if you want it. But you don't need it. Just play the game.

You'll notice that your health points decrease rapidly when you attack. You can get a few back by using the Aguav berries, whatever they are. But somehow, if you choose to attack when your health points are in the low 50s, you will occasionally find that instead of falling below zero, they shoot up to somewhere in the region of 2<sup>32</sup>. I guess this is due to an integer underflow error.
