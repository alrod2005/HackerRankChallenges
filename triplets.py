#!/bin/python3

import os
import sys


def solve_a(a0, a1, a2, b0, b1, b2):
    
    alice_score = 0
    bob_score = 0
    
    if a0 > b0:
        alice_score += 1
        
    elif a0 < b0:
        bob_score += 1
        
    if a1 > b1:
        alice_score += 1
        
    elif a1 < b1:
        bob_score += 1
        
    if a2 > b2:
        alice_score += 1
        
    elif a2 < b2:
        bob_score += 1   
    
    return (alice_score, bob_score)


def solve_b(a0, a1, a2, b0, b1, b2):
	
	a_triplet =[a0, a1, a2]
	b_triplet = [b0, b1, b2]
	alice_points = 0
	bob_points = 0
    
	for a_val, b_val in zip(a_triplet, b_triplet):
		if a_val < b_val:
			bob_points += 1
		elif a_val > b_val:
			alice_points += 1
	print(alice_points, bob_points)
    
