import re
import math
from collections import deque

some_string = 'abcdef'

#create list of M stacks, for "from N chars, choose M chars"
N_str = len(some_string)
M_str = 2 #currently working for 2, 3 and 4 and maybe even more, yay!
list_of_stacks = []
char_index = 0

stack_width = int(math.floor(N_str/M_str))*M_str
stack_width_remainder = int(math.fmod(N_str,M_str))
print(f'stack_width = %d'%(stack_width) )
print(f'stack_width_remainder = %d'%(stack_width_remainder) )
for char_index in range(0,M_str):
    candidate_string = some_string[char_index:(stack_width+char_index)]
    if char_index == M_str-1 and candidate_string[-1:] != some_string[-1:] and \
        stack_width_remainder != 0:
        candidate_string += some_string[-stack_width_remainder:]
    list_of_stacks.append(deque(candidate_string)) #using (N_str-M_str)+char_index instead of N_str

#create a deep copy of the stacks
copy_list_of_stacks = []
for item in list_of_stacks:
    copy_list_of_stacks.append(item.copy())

#verify that this worked
print("INITIAL STACKS")
for item in list_of_stacks:
    print(item)

experiment = True

#now start the big loop
root_stack = list_of_stacks[0]
#first_char = root_stack.popleft()
num_combos = math.comb(N_str,M_str)
list_of_combos = ['']*num_combos
combo_index = 0
while (len(root_stack) > 0) and (combo_index < num_combos):
    if ( len(root_stack) == 0):
        break
    
    #loop down each stack, rebalancing at the end of a complete combination
    for child_stack_index in range(1,M_str):
        parent_stack_index = child_stack_index-1
        parent_char = list_of_stacks[parent_stack_index][0]
        if (len(list_of_combos[combo_index]) == parent_stack_index):
            list_of_combos[combo_index] += parent_char

        
        #get the next character and pop the child stack
        next_char = list_of_stacks[child_stack_index][0]
        
        #if it's not found in the current combination, then add it
        #o.w. skip it and move on the next one
        popped_duplicate = False
        while ( next_char in list_of_combos[combo_index]):
            next_char = list_of_stacks[child_stack_index].popleft()
            popped_duplicate = True
            if next_char in list_of_combos[combo_index] and \
                len(list_of_stacks[child_stack_index]) == 0: #new, unsuccessful combo
                next_char = '' #new, unsuccessful combo
                break #new, unsuccessful combo
        
        #add to list of combos if it's unique
        if (len(list_of_combos[combo_index]) == child_stack_index):# and \
               #len(list_of_stacks[child_stack_index]) > 0): #new "and" condition
            list_of_combos[combo_index]+=next_char

        #if list of combos is of full length or the child stack is empty
        #then there are some complicated operations needed.
        if (len(list_of_combos[combo_index]) == M_str or \
            len(list_of_stacks[child_stack_index]) == 0): #new "or" condition
            if ( len(list_of_stacks[child_stack_index]) > 0 and \
                 not popped_duplicate): #new in _v5.py
                list_of_stacks[child_stack_index].popleft()
            
            #else if len(list_of_stacks[child_stack_index]) == 0
                #no op
            
            if (len(list_of_combos[combo_index]) == M_str):
                #should be done with this combination
                print(f'added combo = %s'%(list_of_combos[combo_index]))
                combo_index+=1
            elif (len(list_of_combos[combo_index]) < M_str and \
                  child_stack_index == (M_str-1)): #new in _4.py
                #list_of_combos[combo_index] = list_of_combos[combo_index][:-1] #new in _4.py
                list_of_combos[combo_index] = '' #new
                print("preliminary combo CLEARED")

            if (len(list_of_stacks[child_stack_index]) == 0 ):

                #if necessary, pop stacks further up as well
                c_stack_ind = M_str-1
                p_stack_ind = c_stack_ind-1
                while (c_stack_ind >= 1 and \
                    len(list_of_stacks[c_stack_ind]) == 0 ):
                    if (len(list_of_stacks[p_stack_ind]) > 0):
                        list_of_stacks[p_stack_ind].popleft()
                    c_stack_ind -= 1
                    p_stack_ind = c_stack_ind-1

                print("AFTER PARENT POPS")
                #verify that this worked
                for item in list_of_stacks:
                    print(item)

                #repopulate empty stacks with full copy
                for stck_ind in range(0,M_str):
                    if ( len(list_of_stacks[stck_ind]) == 0 ):
                        list_of_stacks[stck_ind] = \
                            copy_list_of_stacks[stck_ind].copy()

                #rebalance the stacks based upon parent
                #such that child has equal number as parent
                for p_stck_ind in range(0,M_str-1):
                    while (len(list_of_stacks[p_stck_ind]) < \
                        len(list_of_stacks[p_stck_ind+1])):
                        list_of_stacks[p_stck_ind+1].popleft()


                #remove duplicates at the top of each stack
                for p_stck_ind in range(0,M_str-1):
                    if (list_of_stacks[p_stck_ind][0] == \
                        list_of_stacks[p_stck_ind+1][0] and \
                        len(list_of_stacks[p_stck_ind+1]) > 1): 
                        list_of_stacks[p_stck_ind+1].popleft()
            #end if case for empty stack 
        #end if case for empty stack or complete combination
    #end for loop
    


print(f'Final result is...%d combinations'%(num_combos))
for item in list_of_combos:
    print(item)

        #done with the current iteration of the root stack,
        #must repopulate child stack if it was emptied previously
"""     if len(list_of_stacks[child_stack_index]) == 0:
            first_char = list_of_stacks[parent_stack_index].popleft()
            list_of_combos[combo_index] = first_char
            list_of_stacks[child_stack_index] = copy_list_of_stacks[child_stack_index].copy() """

"""             if ( len(list_of_stacks[child_stack_index]) == 0 ):
                #should be done with this combination
                print(list_of_combos[combo_index])
                combo_index+=1
                #repopulate child stack
                list_of_stacks[child_stack_index] = \
                copy_list_of_stacks[child_stack_index].copy()
                list_of_stacks[parent_stack_index].popleft()
                #special case for when the parent stack is now smaller than child
                #must pop the parent of the parent stack
                if ( len(list_of_stacks[parent_stack_index]) < \
                    len(list_of_stacks[child_stack_index]) ):
                    list_of_stacks[parent_stack_index-1].popleft()
                    #repopulate parent stack if not root
                    if ( parent_stack_index != 0 ):
                        list_of_stacks[parent_stack_index] = \
                        copy_list_of_stacks[parent_stack_index].copy()
                if (experiment):
                    #going to try rebalancing all stacks
                    for p_stck_ind in range(0,M_str-1):
                        if (len(list_of_stacks[p_stck_ind+1]) >= \
                            len(list_of_stacks[p_stck_ind])):
                            list_of_stacks[p_stck_ind+1].popleft() """
""" 
                    if (experiment):
                        #going to try rebalancing all stacks
                        for p_stck_ind in range(0,M_str-1):
                            if (len(list_of_stacks[p_stck_ind+1]) >= \
                                len(list_of_stacks[p_stck_ind])):
                                list_of_stacks[p_stck_ind+1].popleft() """