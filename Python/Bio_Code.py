import random as rand

#II) Algorithms
#global_alignment algorithm to compare 2 sequences:
def global_align(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    #takes list gives string
    len1 = len(seq1)
    len2 = len(seq2)

    score_table = [[0 for j in range(len1+1)] for i in range(len2+1)]
    trace_table = [[[-1,-1] for j in range(len1+1)] for i in range(len2+1)]
    
    #Fill tables
    for i in range(1, len1+1):
        score_table[0][i] = i * gap_penalty
    for j in range(1,  len2+1):
        score_table[j][0] = j * gap_penalty
    for i in range(1, len1+1):
        for j in range(1,  len2+1):
            if seq1[i-1] == seq2[j-1]:
                diagonal = score_table[j-1][i-1] + match_score
            else:
                diagonal = score_table[j-1][i-1] + mismatch_penalty
            left = score_table[j][i-1] + gap_penalty
            up = score_table[j-1][i] + gap_penalty 
            score_table[j][i] = max(diagonal, left, up)
            if (score_table[j][i] == diagonal):
                trace_table[j][i] = [j-1,i-1]
            elif (score_table[j][i] == left):
                trace_table[j][i] = [j,i-1]
            elif(score_table[j][i] == up):
                trace_table[j][i] = [j-1,i]
            else:
                trace_table[j][i] = [-1,-1]#useless?
                
    #Find alignment and score
    alignment1 = ""
    alignment2 = ""
    i = len1
    j = len2 
    final_score = score_table[j][i]
    while i > 0 and j > 0:
        y,x = trace_table[j][i]
        if (x != i and y != j):
            alignment1 = seq1[x] + alignment1
            alignment2 = seq2[y] + alignment2
            i -= 1
            j -= 1
        elif (x != i and y == j):
            alignment1 = seq1[x] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = seq2[y] + alignment2
            j -= 1
    final_score += score_table[j][i]
    while i > 0:
        alignment1 = seq1[i-1] + alignment1
        alignment2 = "-" + alignment2
        i -= 1
    while j > 0:
        alignment1 = "-" + alignment1
        alignment2 = seq2[j-1] + alignment2
        j -= 1
    return alignment1, alignment2, final_score

# algorithm to assist the multiple sequence alignment
def create_template(sequences):
    # takes list, gives string
    template = ''
    index_list = [0] * len(sequences)

    while True:
        # make a temp_list with the first unused element
        temp_list = []
        for i in range(len(index_list)):
            if (index_list[i] < len(sequences[i])):
                temp_list.append(sequences[i][index_list[i]])

        #find the most common element and save it
        best_char = max( set(temp_list), key = temp_list.count )
        template += best_char

        # prepare for the next element selection
        for i in range(len(sequences)):
            if( index_list[i] < len(sequences[i])): 
               if (sequences[i][index_list[i]] == best_char):
                    index_list[i] += 1

        # check if we're done
        done = True
        for i in range(len(index_list)):
            if (index_list[i] < len(sequences[i])):
                done = False
                break 
        if done:
            break
    return template

# multiple_sequence_alignment algorithm 
def multiple_sequence_align(sequences, template):
    #takes lists and gives list
    aligned_sequences = []
    for x in range(0, len(sequences)):
        not_done = True
        seq_index = 0
        template_index = 0
        next_seq = []
        while not_done:
            # align all sequences in the form of the template
            if (sequences[x][seq_index] == template[template_index]):#match
                next_seq.append(sequences[x][seq_index])
                seq_index += 1
                """
                #code from previous version, saved for inspiration
                elif (template[template_index] == "-"): #update template
                    template[template_index] = sequences[x][seq_index]
                    next_seq.append(sequences[x][seq_index])
                    seq_index += 1
                """
            else:#skip
                next_seq.append("-")
            template_index += 1
            if (template_index == len(template)): #if template = empty
                not_done = False 
                if (seq_index != len(sequences[x])):#if template = empty && sequence = NOT empty 
                    #update template
                    next_seq += sequences[x][seq_index:]
                    template += sequences[x][seq_index:] 
                    #update already created sequences 
                    for align_index in range(len(aligned_sequences)):
                        while (len(aligned_sequences[align_index]) != len(template)):
                            aligned_sequences[align_index] += "-"
            elif (seq_index == len(sequences[x])): #if sequence = empty && template = NOT empty
                not_done = False
                while (len(next_seq) != len(template)):
                    next_seq.append("-")
        aligned_sequences.append(next_seq)
    
    #cut off the extra "-"s
    while True:
        delete = True
        for x in range(len(aligned_sequences)):
            if (aligned_sequences[x][-1] != "-"):
                delete = False
        if delete:
            for x in range(len(aligned_sequences)):
                aligned_sequences[x].pop()
        else:
            break
    return aligned_sequences

"___Start of Main___"
genes = ['A', 'C', 'G', 'T']
pattern1 = ['A', 'A', 'T', 'T', 'G', 'A']
pattern2 = ['C', 'G', 'C', 'T', 'T', 'A', 'T']
pattern3 = ['G', 'G', 'A', 'C', 'T', 'C', 'A', 'T']
pattern4 = ['T', 'T', 'A', 'T', 'T', 'C', 'G', 'T', 'A']

"I)"
dataset = []
new_genes = list(genes)
new_genes.append("-")
sequence_total = [pattern1, pattern2, pattern3, pattern4]
for repeats in range(50):
    "a) create start of sequence"
    final = []
    for i in range(rand.randint(1, 3)):
        final.append( genes[rand.randint(0, 3)] )

    "b) create middle of sequence"
    #add the patterns 
    # νομίζω κατάλαβα λάθος την εκφώνση αν ναι, 
    # σας παρακαλώ εποικοινωνήστε και θα σας στείλω την διόρθωση σε 15 λεπτά το πολύ, 
    # δεν είναι έλειψη γνώσεων, απλά λάθος ερμηνεία 
    for patt in sequence_total:
        for gn in patt:
            final.append(gn)

    #replace 1-2 elements
    for i in range(rand.randint(1,2)):
        ng =  new_genes[rand.randint(0, len(new_genes) - 1)]
        final_index = rand.randint(0, len(final) - 1)
        if (final[final_index] != ng):
            final[final_index] = ng
        else:
            i -= 1

    "c) create end of sequence"
    for i in range(rand.randint(1, 3)):
        final.append( genes[rand.randint(0, 3)] )
    dataset.append(final)

#create databases
datasetA = []
datasetB = []
for i in range(15):
    datasetA.append( dataset.pop( rand.randint(0, len(dataset) - 1) ) )
for i in dataset:
    datasetB.append(i)

"II) Algorithm"
#use global_align to find the most probable sequence and create a template on that 
data_for_temp = []
for i in range(len(datasetA)):
    for j in range(i+1, len(datasetA)):
        s1, s2, _ = global_align(datasetA[i], datasetA[j], match_score= 1, mismatch_penalty= -1, gap_penalty=-2)
        data_for_temp.append(list(s1))
        data_for_temp.append(list(s2))
template = list(create_template(data_for_temp))

#align DatabaseA
aligned_datasetA = multiple_sequence_align(datasetA, template)
for x in aligned_datasetA:
    print("".join(x))


"III) Hardest part"
data_for_temp = []
for i in range(len(datasetB)):
    for j in range(i+1, len(datasetB)):
        s1, s2, score = global_align(datasetB[i], datasetB[j], match_score= 1, mismatch_penalty= -1, gap_penalty=-2)
        print("\nsequence[", i, "]:", "".join(datasetB[i]))
        print("sequence[", j, "]:","".join(datasetB[j]))
        print("alignment score: ", score)
        print("alignment paths: ", s1)
        print("                 ", s2)



