'''
File: bio.py
Author: Seemya Mohamed & Christopher Payne
Date: 2024-04-13

Description: This file was made for project 1 in CSCI 687 - Advanced Software Development. It contains a class to initialize an array of 
DNA and RNA seqeuences. This Sequence Array class contains 9 operations and 4 attributes. The 9 operations deal with the creation of the 
sequence array, the altering of the sequence array, and the display of the sequence array. The 4 attributes contian important information
about the sequence array. The program also contains a logic tree for reading commands from a file and output a text file summarizing the
actions of the program.
'''
# sys library is used to read arguements from the cmd line
import sys

# class for all of the Sequence Array functions and attributes
class SEQUENCE_ARRAY:
    # function to initialize the sequence array object
    def __init__(self, size:int = 100) -> None:
        self.size = size # size default is 100
        self.seq_arr = self.initSeqArr(self.size) # create an array of length self.size full of empty tuples
        self.types = {"DNA":['A', 'C', 'G', 'T'], "RNA": ['A', 'C', 'G', 'U']} # the types and associated letters for the sequences
        self.history = [] # empty array to hold the history of the commands and messages that occur during the program
    
    # function to create the sequence array of empty tuples (None, None)
    def initSeqArr(self, size:int = 100):
        seq = (None,None)
        seq_arr =[]
        # create an array of tuples (None,None) of length of 'size'
        [seq_arr.append(seq) for i in range(0,size)]
        return seq_arr
    
    # function to check if a sequence of letters match the sequence type. See self.types
    def checkSequence(self, type:str, sequence:str) -> bool:
        result = False
        # Check if the type is DNA
        if type.upper() == "DNA":
            # check every letter in the sequence and see if the letter is in the list of valid letters for DNA
            for letter in sequence:
                try:
                    assert(letter.upper() in self.types["DNA"]) # assert the letter is in the list of valid letters for DNA
                    result = True
                # if the assertion is false print the error message, add it to the history, set the result to false, and break the loop
                except AssertionError:
                    err_msg = f"ERROR: {letter} is not a valid element of {type.upper()}. Valid letters are {self.types['DNA']}."
                    print(err_msg)
                    self.history.append(err_msg)
                    result = False
                    break
        # if the type is not DNA, check if it is RNA
        elif type.upper() == "RNA":
            # for every letter in the sequence, see if the letter is in the list of valid letters for RNA
            for letter in sequence:
                try:
                    assert(letter.upper() in self.types["RNA"]) # assert the letter is in the list of valid letters for RNA
                    result = True
                # if the assertion is false print the error message, add it to the history, set the result to false, and break the loop
                except AssertionError:
                    err_msg = f"ERROR: {letter} is not a valid element of {type.upper()}. Valid letters are {self.types['RNA']}."
                    print(err_msg)
                    self.history.append(err_msg)
                    result = False
                    break
        # if the type is not DNA or RNA, the print the following error and add it to history.
        else:
            err_msg = f"ERROR: {type.upper()} is not a valid sequence type. Valid types are {list(self.types.keys())}."
            print(err_msg)
            self.history.append(err_msg)
        # return the state of result (bool)
        return result

    def insert(self, pos:int, type:str, sequence:str):
        '''
        Insert sequence (sequence) to position (pos) in the sequence array.
        Type whether it is DNA or RNA. CHECK that the sequence contains
        only appropriate letters for its type (DNA: A,C,G,T & RNA: A,C,G,U).
        If not the appropirate letters, the operation is an error and no
        change is made to the sequence array. If ther is already a sequence
        at position (pos) and if the sequence (sequence) is syntactically
        correct, then the new sequence overwrites the old one at that 
        position (pos). It is safe to assume that sequence (sequence) is 
        NOT null (containing no characters).
        '''
        try:
            # check if the sequence to be inserted is valid for its type (DNA/RNA)
            assert(self.checkSequence(type, sequence))
            pos = int(pos)
            self.seq_arr[pos] = (type, sequence) # add the tuple of (type, sequence) to the position of pos in the sequence array.
        # if the position cannot be cast as an integer, print the error message and add it to history
        except ValueError:
            err_msg = f"ERROR: the position must be an integer. {pos} is {type(pos)}"
            print(err_msg)
            self.history.append(err_msg)
        # if the sequence is not valid for the type, then print the error message and add it to history
        except AssertionError:
            err_msg = f"ERROR: the type or sequence are not valid. type: {type}, seq: {sequence}"
            print(err_msg)
            self.history.append(err_msg)


    def print(self, pos:int = None):
        '''
        print():
        Print out all sequences in the sequence array. Indicate for each 
        sequence its position within the sequence array and the type of 
        sequence it is (DNA/RNA). Do NOT print anything for slots in the 
        sequence array that are empty.
        
        print(pos)
        Print the sequence and type at the position (pos) in the sequence
        array. If there is no sequence in that position, print a suitable
        message.
        '''
        # check if an arguement for pos was passed.
        # if no arguement was passed, print the every non-empty sequence in the sequence array with it's position in the array
        if pos == None:
            for i,seq in enumerate(self.seq_arr): # i is the position, and seq is the tuple of the type and sequence
                if seq != (None,None): # (None, None) is a empty position
                    print(f"[{i}]: {seq}") # print in the format '[pos]: (type, sequence)', e.g. '[0]: (DNA, AGCT)'
        # if an arguement is given then print the position type and sequence at just that arguement.
        else:
            try:
                pos = int(pos) # ensure the position is an integer, if not print and error and add it to history
            except ValueError:
                err_msg = f"ERROR: the position must be an integer. {pos} is {type(pos)}"
                print(err_msg)
                self.history.append(err_msg)
            # if the position in the seq_arr is not empty print the position, type, and sequence from the array
            if self.seq_arr[pos] != (None,None):
                print(f"[{pos}]: {self.seq_arr[pos]}")
            # if the position in the seq_arr is empty, print the note and add it to history
            else:
                err_msg = f"NOTE: Sequence Array is empty at [{pos}]."
                print(err_msg)
                self.history.append(err_msg)

    def remove(self, pos:int):
        '''
        Remove the sequence and type at position (pos) in the sequence 
        array. Be sure to set the type field to indicate that this position
        is now empty. If ther is no sequence at position (pos), output a 
        suitable message.
        '''
        try:
            pos = int(pos) # ensure the position is an integer, if not print and error and add it to history
        except ValueError:
            err_msg = f"ERROR: the position must be an integer. {pos} is {type(pos)}"
            print(err_msg)
            self.history.append(err_msg)
        # if the position in the seq_arr is not empty, set that position to be equal to an empty tuple (None, None)
        if self.seq_arr[pos] != (None,None):
            self.seq_arr[pos] = (None, None)
        # if the position in the seq_arr is empty, print the note and add it to history
        else:
            err_msg = f"NOTE: Sequence Array is empty at [{pos}]. Nothing was removed."
            print(err_msg)
            self.history.append(err_msg)
        

    def copy(self, pos1:int, pos2:int):
        '''
        Copy the sequence in position pos1 to pos2. If there is no sequence 
        at pos1, output a suitable message and do not modify the sequence at
        pos2.
        '''
        try:
            pos1 = int(pos1) # ensure the position is an integer, if not print and error and add it to history
            pos2 = int(pos2) # ensure the position is an integer, if not print and error and add it to history
        except ValueError:
            err_msg = f"ERROR: the positions must be integers. {pos1} is {type(pos1)}. {pos2} is {type(pos2)}"
            print(err_msg)
            self.history.append(err_msg)
        # if pos1 in the seq_arr is not empty, set pos2 to be equal to pos1
        if self.seq_arr[pos1] != (None,None):
            self.seq_arr[pos2] = self.seq_arr[pos1]
        # if pos1 in the seq_arr is empty, print the note and add it to history
        else:
            err_msg = f"NOTE: Sequence Array is empty at [{pos1}]. No change was made at [{pos2}]."
            print(err_msg)
            self.history.append(err_msg)

    def swap(self, pos1:int, start1:int, pos2:int, start2:int):
        '''
        Swap the tails of the sequences at positions pos1 and pos2. The
        tail for pos1 begins at character start1, and the tail for pos2
        begins at character start2. It is an error if the value of the 
        start position is greater than  the length of the sequence or
        is less than zero. If the length of the sequence is n, the 
        start position may be n, meaning that the tail of the other 
        sequence is appended (i.e. a tail of null length is being swapped).
        The swap operation should be reported as an error if the two 
        sequences are not the same type (DNA/RNA), or if one of the slots
        does not contain a sequence. In either case, no change should be 
        made to the sequences.
        '''
        try:
            try:
                # ensure the positions and starts are integers, if not print an error and add it to history
                pos1 = int(pos1)
                pos2 = int(pos2)
                start1 = int(start1)
                start2 = int(start2)
            except ValueError:
                err_msg = f"ERROR: the positions must be integers. {pos1} is {type(pos1)}. {pos2} is {type(pos2)}. {start1} is {type(start1)}. {start2} is {type(start2)}."
                print(err_msg)
                self.history.append(err_msg)
            # assert that each start is between 0 and the length of the sequence at that position
            assert(start1 > -1 and start1 <= len(self.seq_arr[pos1][1]))
            assert(start2 > -1 and start2 <= len(self.seq_arr[pos2][1]))
            # if pos1 and pos2 are both not empty, then swap.
            if self.seq_arr[pos1] != (None,None) and self.seq_arr[pos2] != (None,None):
                try:
                    assert(self.seq_arr[pos1][0] == self.seq_arr[pos2][0]) # Assert the sequences have the same type
                    swap_buffer = self.seq_arr[pos1][1] # store the sequence for pos1 for later
                    # if start1 is the length of sequence at pos1, then append the sub-array of the sequence at pos2
                    if start1 == len(self.seq_arr[pos1][1]):
                        seq_list = list(self.seq_arr[pos1][1]) # make the sequence string a list of characters, so it can be indexed
                        seq_tup_list = list(self.seq_arr[pos1]) # make the tuple of type and sequence a list, so it can be indexed
                        seq_list.append(self.seq_arr[pos2][1][start2:]) # append the sub-array of sequence at pos2 to the sequence at pos1
                        seq_tup_list[1] = "".join(seq_list) # re-join the sequecnce list at pos1 as a string and add it to the pos1 tuple list
                        self.seq_arr[pos1] = tuple(seq_tup_list) # re-tuple the tuple list for pos1 and place that in pos1 in the sequence array
                    # if start1 is not the length of sequence at pos1, then insert the sub-array of the sequence at pos2
                    else:
                        seq_list = list(self.seq_arr[pos1][1]) # make the sequence string a list of characters, so it can be indexed
                        seq_tup_list = list(self.seq_arr[pos1]) # make the tuple of type and sequence a list, so it can be indexed
                        seq_list[start1:] = self.seq_arr[pos2][1][start2:] # insert the sub-array of sequence at pos2 to the sequence at pos1
                        seq_tup_list[1] = "".join(seq_list) # re-join the sequecnce list at pos1 as a string and add it to the pos1 tuple list
                        self.seq_arr[pos1] = tuple(seq_tup_list) # re-tuple the tuple list for pos1 and place that in pos1 in the sequence array
                    # if start2 is the length of sequence at pos2, then append the sub-array of the sequence at pos1 from the swap_buffer
                    if start2 == len(self.seq_arr[pos2][1]):
                        seq_list = list(self.seq_arr[pos2][1]) # make the sequence string a list of characters, so it can be indexed
                        seq_tup_list = list(self.seq_arr[pos2]) # make the tuple of type and sequence a list, so it can be indexed
                        seq_list.append(swap_buffer[start1:]) # append the sub-array of sequence at pos1 to the sequence at pos2
                        seq_tup_list[1] = "".join(seq_list) # re-join the sequecnce list at pos2 as a string and add it to the pos2 tuple list
                        self.seq_arr[pos2] = tuple(seq_tup_list) # re-tuple the tuple list for pos2 and place that in pos2 in the sequence array
                        
                    else:
                        seq_list = list(self.seq_arr[pos2][1]) # make the sequence string a list of characters, so it can be indexed
                        seq_tup_list = list(self.seq_arr[pos2]) # make the tuple of type and sequence a list, so it can be indexed
                        seq_list[start2:] = swap_buffer[start1:] # insert the sub-array of sequence at pos1 to the sequence at pos2
                        seq_tup_list[1] = "".join(seq_list) # re-join the sequecnce list at pos2 as a string and add it to the pos2 tuple list
                        self.seq_arr[pos2] = tuple(seq_tup_list) # re-tuple the tuple list for pos2 and place that in pos2 in the sequence array
                # if the types of the two positions are not the same, print an error and add it to history
                except AssertionError:
                    err_msg = f"ERROR: [{pos1}] and [{pos2}] do NOT have the same type. {self.seq_arr[pos1][0]} != {self.seq_arr[pos2][0]}"
                    print(err_msg)
                    self.history.append(err_msg)
        # if the two positions are not valid positions, print an error and add it to history
        except AssertionError:
            err_msg = f"ERROR: {pos1} or {pos2} are not valid inputs."
            print(err_msg)
            self.history.append(err_msg)
        
    def transcribe(self, pos1:int):
        '''
        Transcription converts a DNA sequence to an RNA sequence. It is an
        error to perform the transcribe operation on an RNA sequence. To
        transcribe a DNA sequence, change its type field to RNA, convert
        any occurences of T to U, complement all the letters in the 
        sequence, and reverse the sequence. Letters A and U are complements
        of each other, and letters C and G are complements of each other.
        If the slot is empty, then print a suitable message.
        '''

        try:
            # ensure the position is an integer, if not print an error and add it to history
            pos1 = int(pos1)
        except:
            err_msg = f"ERROR: the position must be an integer. {pos1} is {type(pos1)}"
            print(err_msg)
            self.history.append(err_msg)
        try:
            assert(self.seq_arr[pos1][0]=="DNA") # transcription only works on DNA
            seq_tup_list = list(self.seq_arr[pos1]) # make the tuple of type and sequence a list, so it can be indexed
            seq_list = list(seq_tup_list[1]) # make the sequence string a list of characters, so it can be indexed
            seq_tup_list[0] = "RNA" # set the type as RNA
            # for every letter in the sequence, replace it with it's complementary letter
            for i,letter in enumerate(seq_tup_list[1]):
                if letter == 'T':
                    seq_list[i] = 'U'
                elif letter == 'A':
                    seq_list[i] = 'U'
                elif letter == 'C':
                    seq_list[i] = 'G'
                elif letter == 'G':
                    seq_list[i] = 'C'
            # create a sequence of letters that is the reverse of the complemented sequence
            reversed_seq = [seq_list[-i] for i in range(1, len(seq_list)+1)]
            seq_tup_list[1] = "".join(reversed_seq) # join the reveresed sequence as a string and place in the sequence section of the tuple
            self.seq_arr[pos1] = tuple(seq_tup_list) # re-tuple the tuple list and place it in the sequence array as pos1.
        # if the sequence is not a DNA, it cannot be transcribed. Print error and add it to history
        except AssertionError:
            err_msg = f"ERROR: [{pos1}] is not DNA. Transcription only works on DNA."
            print(err_msg)
            self.history.append(err_msg)

# Main logic tree for interpeting and calling commands from the sequence array class
def main_logic_tree(line:list, seq_arr:SEQUENCE_ARRAY, line_count:int, filename:str):
    
    # dictionary of valid commands. A dictionary was chosen for legiblity purposes.
    commands = {"insert": "insert", "print": 'print',
                 "remove": 'remove', "copy": 'copy',
                 "swap":'swap', "transcribe":'transcribe'}
    # Note: The first element in the line from the file is the cmd. Every other element is a arguement for the cmd.
    
    # if the command is a valid command, then run the command.
    if line[0].lower() in commands.keys():
        # if the command is insert, run insert and add to history
        if line[0].lower() == commands["insert"]:
            cmd_msg = f"Inserting ({line[2]}, {line[3]}) at {line[1]}."
            seq_arr.history.append(cmd_msg)
            print(cmd_msg)
            seq_arr.insert(line[1], line[2], line[3])
        # if the command is copy, run copy and add to history
        elif line[0].lower() == commands["copy"]:
            cmd_msg = f"Copying {line[1]} to {line[2]}"
            seq_arr.history.append(cmd_msg)
            print(cmd_msg)
            seq_arr.copy(line[1], line[2])
        # if the command is print, run print and add to history
        elif line[0].lower() == commands["print"]:
            # if there is an arguement, run print(pos) and add to history
            if len(line) > 1:
                cmd_msg = f"Printing sequence at position {line[1]}"
                seq_arr.history.append(cmd_msg)
                print(cmd_msg)
                seq_arr.print(line[1])
            # if there is no arguement, run print() and add to history
            else:
                cmd_msg = f"Printing Sequence Array"
                seq_arr.history.append(cmd_msg)
                print(cmd_msg)
                seq_arr.print()
        # if the command is remove, run remove and add to history
        elif line[0].lower() == commands["remove"]:
            cmd_msg = f"Removing {line[1]} from Sequence Array"
            seq_arr.history.append(cmd_msg)
            print(cmd_msg)
            seq_arr.remove(line[1])
        # if the command is swap, run swap and add to history
        elif line[0].lower() == commands["swap"]:
            cmd_msg = f"Swapping {line[1]} starting at {line[2]} with {line[3]} starting at {line[4]}"
            seq_arr.history.append(cmd_msg)
            print(cmd_msg)
            seq_arr.swap(line[1], line[2], line[3], line[4])
        # if the command is transcribe, run transcribe and add to history
        elif line[0].lower() == commands["transcribe"]:
            cmd_msg = f"Transcribing {line[1]}"
            seq_arr.history.append(cmd_msg)
            print(cmd_msg)
            seq_arr.transcribe(line[1])
    # if the command is not valid, print the error message and add to history
    else:
        err_msg = f"ERROR: {line[0]} is an invalid command - line {line_count} in {filename}."
        print(err_msg)
        seq_arr.history.append(err_msg)


def main():
    
    # Get the cmd line inputs as a array
    cmd_inputs = sys.argv[1:] # The first element of the array is the file's own name, so we skip it here.

    # Check if the first arguement is an integer.
    # If it is, then that will be the array size 
    # and the second command will be the command
    # file string. Otherwise, the first command
    # is the command file string.
    try:
        size = int(cmd_inputs[0])
        filename = str(cmd_inputs[1])
    except ValueError:
        size = 100
        filename = str(cmd_inputs[0])
    
    # Create the SEQUENCE_ARRAY object with the appropriate size
    seq_arr = SEQUENCE_ARRAY(size)

    # Make the filename a raw string
    filename = r"{0}".format(filename)

    # Make an output file
    output_filename = r"{0}".format("output_file.txt")

    # with the cmd_file open as readable, run the main logic tree
    with open(filename,'r') as cmd_file:
        count = 0 # create a line count variable to track which line is being read from the input file
        for line in cmd_file:
            print("")
            count += 1
            print(f"Running: {line} from file {cmd_file.name}") # print the line that is being ran from the input file
            line = line.split() # split the line into an array, seperating the elements at each space.
            main_logic_tree(line, seq_arr, count, cmd_file.name)
    
    # with the output file open a writetable, write the command history and final sequence array
    with open(output_filename, "w") as out_file:
        # create header for the output file
        header = f"\nCommand History:\n"
        out_file.writelines(header)
        out_file.writelines("-" * len(header) + "\n")
        # write each command in the history to the output file
        for cmd in seq_arr.history:
            out_file.writelines(f"{cmd}\n")

        # create header for the output file
        header = f"\nFinal Sequence Array (empty positions are not shown):\n"
        out_file.writelines(header)
        out_file.writelines("-" * len(header) + "\n")
        
        # create a list of the non-empty posistions in the sequence array
        final_seq_arr = [f"[{i}] {sequence}" for i,sequence in enumerate(seq_arr.seq_arr) if sequence != (None,None)]
        # write each non-empty position in the sequence array to the output file
        for seq in final_seq_arr:
            out_file.writelines(f"{seq}\n")
        # write the total length of the sequence array including empty locations
        out_file.writelines(f"Length of Sequence Array: {len(seq_arr.seq_arr)}")

    print("End")

# run the main function
if __name__ == '__main__':
    main()