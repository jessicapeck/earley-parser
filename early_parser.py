# define toy grammar
N = {"S", "NP", "VP", "PP", "N", "V", "P"}
words = {"can", "fish", "in", "rivers", "they", "december"}
S = "S"
P = {"S": [["NP", "VP"]],
     "NP": [["N", "PP"], ["N"]],
     "PP": [["P", "NP"]],
     "VP": [["VP", "PP"], ["V", "VP"], ["V", "NP"], ["V"]],
     "N": [["can"], ["fish"], ["rivers"], ["they"], ["december"]],
     "P": [["in"]],
     "V": [["can"], ["fish"]]}

def show_chart(chart):
    print(f"{'ID':<5} {'RULE':<20} {'[start,end]':<15} {'HIST':<8}")
    print("-"*40)

    for id, ((lhs, rhs), dot_index, (start, end), hist) in chart.items():
        formatted_rhs = ""
        for i, n in enumerate(rhs):
            if dot_index == i:
                formatted_rhs += ". "
            formatted_rhs += f"{n} "
        
        rule = f"{lhs} -> {formatted_rhs}"

        formatted_hist = ""
        if hist is not None:
            for h in hist:
                formatted_hist += f"{h} "

        print(f"{id:<5} {rule :<20} {f'[{start},{end}]':<15} {f'({formatted_hist})':<8}")


def predict(record, chart, index):
    ((_, rhs), dot_index, (start, end), _) = record
    N = rhs[dot_index]

    for new_rhs in P.get(N):
        chart[index] = ((N, new_rhs), 0, (start, end), None)
        index += 1

    return index

def scan(record, chart, index, sentence, word_index):
    ((lhs, rhs), dot_index, (start, end), _) = record
    current_word = sentence[word_index]

    if rhs[dot_index] == current_word:
        chart[index] = ((lhs, rhs), 1, (start, end + 1), None)
        index += 1
        return (index, True)
    
    return (index, False)

def complete(record, chart, index):
    ((lhs, rhs), dot_index, (start, end), hist) = record

        
        


    
    
def main():
    sentence = input("Sentence : ")
    sentence = sentence.lower().strip().split(" ")

    # define a queue of non-terminals that need to be predicted
    Q = [S]

    # create the chart which will be a dict of id:(rule, dot index, (start, end), hist)
    chart = {}

    record_index = 0
    word_index = 0

    show_chart(chart)


    # while len(Q) > 0:
    #     n = Q.pop(0)
    #     # PREDICT
    #     for rhs in P.get(n):
    #         # SCAN
    #         if sentence_ids.get(word_index) in rhs:
    #             chart[record_index] = ((n, rhs), 0, ())
    #             # COMPLETE


    #         chart[record_index] = ((n, rhs), index, (0,0), None)






if __name__ == '__main__':
    main()