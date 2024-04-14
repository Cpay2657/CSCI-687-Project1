import unittest
from bio import SEQUENCE_ARRAY

class TESTPROJECT1(unittest.TestCase):

    def test_initSeqArr(self):
        print("\nTESTING: initSeqArr")
        
        # run the function
        seq_arr = SEQUENCE_ARRAY(100)

        # The function should produce a list 100 entries
        self.assertEqual(len(seq_arr.seq_arr), 100)
        
        # Each entries in the list must be a tuple of 2 None values (None, None)
        for seq in seq_arr.seq_arr:
            self.assertEqual(type(seq), tuple)
            self.assertEqual(seq, (None,None))

    def test_checkSequence(self):
        print("\nTESTING: checkSequence")

        seq_arr = SEQUENCE_ARRAY()

        self.assertTrue(seq_arr.checkSequence("DNA", "ACGTACGT")) # Test perfect DNA sequence
        self.assertTrue(seq_arr.checkSequence("RNA", "ACGUACGU")) # Test perfect RNA sequence
        self.assertTrue(seq_arr.checkSequence("dna", "acgt")) # Test DNA lowercase sensetivity case
        self.assertTrue(seq_arr.checkSequence("rna", "acgu")) # Test RNA lowercase sensetivity case
        self.assertFalse(seq_arr.checkSequence("DNA", "ACGU")) # Test incorrect DNA sequence case
        self.assertFalse(seq_arr.checkSequence("DNA", "ACG1ACGU")) # Test incorrect DNA sequence case
        self.assertFalse(seq_arr.checkSequence("RNA", "ACGT")) # Test incorrect RNA sequence

        self.assertFalse(seq_arr.checkSequence("TNA", "ACGT")) # Test incorrect sequence type


    def test_insert(self):
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

        print("\nTESTING: insert")

        seq_arr = SEQUENCE_ARRAY()
        pos = 0
        good_test_tuple = ("DNA", "ACGTACGT")
        seq_arr.insert(pos, good_test_tuple[0], good_test_tuple[1]) # insert good tuple
        self.assertEqual(seq_arr.seq_arr[pos], good_test_tuple) # test perfect case

        no_change_tuple = seq_arr.seq_arr[pos] # get current tuple
        bad_test_tuple = ("DNA", "ACG1ACGT")
        seq_arr.insert(pos, bad_test_tuple[0], bad_test_tuple[1]) # insert bad tuple
        self.assertNotEqual(seq_arr.seq_arr[pos], bad_test_tuple) # test that the bad tuple is not inserted
        self.assertEqual(seq_arr.seq_arr[pos], no_change_tuple) # test the tuple has not been changed

    def test_print(self):
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
        print("\nTESTING: print")

        seq_arr = SEQUENCE_ARRAY()
        seq_arr.insert(0, "DNA", "ACGATACGT")
        seq_arr.insert(99, "RNA", "ACGAUACGU")
        seq_arr.print()
        self.assertEqual(input("Did any empty positions print i.e. (None, None)? (Y/N): ").lower(), 'n')
        
        seq_arr.print(0)
        self.assertEqual(input("Did position 0 print (DNA, ACGATACGT)? (Y/N): ").lower(), 'y')
        
        seq_arr.print(1)
        self.assertEqual(input("Did a message state [1] is empty? (Y/N): ").lower(), 'y')


    def test_remove(self):
        '''
        Remove the sequence and type at position (pos) in the sequence 
        array. Be sure to set the type field to indicate that this position
        is now empty. If ther is no sequence at position (pos), output a 
        suitable message.
        '''
        print("\nTESTING: remove")

        seq_arr = SEQUENCE_ARRAY()
        pos = 0

        seq_arr.remove(pos)
        self.assertEqual(input(f"Did a message state [{pos}] is empty and nothing was removed? (Y/N): ").lower(), 'y')


        seq_arr.insert(pos, "DNA", "ACGATACGT")
        seq_arr.remove(pos)
        self.assertEqual(seq_arr.seq_arr[pos], (None, None))
        

    def test_copy(self):
        '''
        Copy the sequence in position pos1 to pos2. If there is no sequence 
        at pos1, output a suitable message and do not modify the sequence at
        pos2.
        '''
        print("\nTESTING: copy")

        seq_arr = SEQUENCE_ARRAY()
        pos1 = 0
        pos2 = 99
        test_tuple = ("DNA", "ACGATACGT")

        seq_arr.copy(pos1, pos2)
        self.assertEqual(seq_arr.seq_arr[pos2], (None,None))

        seq_arr.insert(pos1, test_tuple[0], test_tuple[1])
        seq_arr.copy(pos1, pos2)
        self.assertEqual(seq_arr.seq_arr[pos1], seq_arr.seq_arr[pos2])


        

    def test_swap(self):
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
        print("\nTESTING: swap")
        seq_arr = SEQUENCE_ARRAY()
        sequence_0 = ("DNA", "AGCGGCG")
        sequence_1 = ("DNA", "AAA")
        swap_seq_0 = ("DNA", "AGCAAA")
        swap_seq_1 = ("DNA", "GGCG")
        sequence_98 = ("RNA", "AGUA")
        sequence_99 = ("RNA", "UU")
        swap_seq_98 = ("RNA", "AGUA")
        swap_seq_99 = ("RNA", "UU")
        
        pos1 = 0
        start1 = 3
        pos2 = 1
        start2 = 0
        pos98 = 98
        start98 = 4
        pos99 = 99
        start99 = 2

        seq_arr.insert(pos1, sequence_0[0], sequence_0[1])
        seq_arr.insert(pos2, sequence_1[0], sequence_1[1])
        seq_arr.insert(pos98, sequence_98[0], sequence_98[1])
        seq_arr.insert(pos99, sequence_99[0], sequence_99[1])

        seq_arr.swap(pos1, start1, pos2, start2)
        self.assertEqual(seq_arr.seq_arr[pos1], swap_seq_0)
        self.assertEqual(seq_arr.seq_arr[pos2], swap_seq_1)
        
        no_change_tuple_98 = seq_arr.seq_arr[pos98]
        seq_arr.swap(pos1, start1, pos98, start98)
        self.assertEqual(seq_arr.seq_arr[pos98], no_change_tuple_98)

        seq_arr.swap(pos98, start98, pos99, start99)
        self.assertEqual(seq_arr.seq_arr[pos98], swap_seq_98)
        self.assertEqual(seq_arr.seq_arr[pos99], swap_seq_99)



    def test_transcribe(self):
        '''
        Transcription converts a DNA sequence to an RNA sequence. It is an
        error to perform the transcribe operation on an RNA sequence. To
        transcribe a DNA sequence, change its type field to RNA, convert
        any occurences of T to U, complement all the letters in the 
        sequence, and reverse the sequence. Letters A and U are complements
        of each other, and letters C and G are complements of each other.
        If the slot is empty, then print a suitable message.
        '''
        print("\nTESTING: transcribe")

        seq_arr = SEQUENCE_ARRAY()

        pos = 0
        seq = ("DNA", "ACGT")
        transcribed_seq = ("RNA", "UCGU")
        seq_arr.insert(pos, seq[0], seq[1])
        seq_arr.transcribe(pos)
        self.assertEqual(seq_arr.seq_arr[pos], transcribed_seq)

        pos = 99
        seq = ("RNA", "ACGU")
        transcribed_seq = seq # Shoud not change
        seq_arr.insert(pos, seq[0], seq[1])
        seq_arr.transcribe(pos)
        self.assertEqual(seq_arr.seq_arr[pos], transcribed_seq)



# driver code
if __name__ == '__main__':
   
    unittest.main()