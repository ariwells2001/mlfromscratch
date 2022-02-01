from itertools import count
from typing import List

from matplotlib.font_manager import win32FontDirectory
from collections import Counter


def raw_majority_vote(labels:List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    print (votes.most_common(1)[0])
    return winner


assert raw_majority_vote(['a','b','c','b']) == 'b'

def majority_vote(labels:List[str]) -> str:
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    print (vote_counts.most_common(1)[0])
    num_winners = len([count
                        for count in vote_counts.values() if count == winner_count])
    if num_winners ==1:
        return winner
    else:
        return majority_vote(labels[:-1])

assert majority_vote(['a','b','c','b']) == 'b'