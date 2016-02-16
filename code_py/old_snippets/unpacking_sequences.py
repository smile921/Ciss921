# Unpacking Sequences

# * can be used to denote that all items in a sequences that are not assigned
# already should be assigned

# Create a sequence of candidates
candidatesRankedByVote = ['Julia Powers', 'Jenna Middle', 'Jake Average', 'Molly Hitler']

# Unpack the sequence, seperating the four values of candidatesRankedByVote into
# four variables.
winner, runnerUp, thirdPlace, fourthPlace = candidatesRankedByVote

# View those four variables.
print('Winner:', winner,
      'Runner Up:', runnerUp,
      '3rd Place:', thirdPlace,
      '4th Place:',  fourthPlace
      )

# Unpack the sequence, create two variables, one with the winner, and one with
# all the non-winners.

electedCandidate, *nonElectedCandidate = candidatesRankedByVote

print('Victor:', electedCandidate, ', Losers:', nonElectedCandidate)

# Create three variables, one for the candidate with the most votes, one for
# the candidate with the least votes, and one for the middle candidates.
# Specifically, the * takes everything between the first and last variable assignment.

mostVotes, *middleVotes, leastVotes = candidatesRankedByVote

# View those three variables.
print('Most Votes:', mostVotes,
      'Middle Pack:', middleVotes,
      'Least Votes:', leastVotes,
      )

# Create three variables, one for the winner, one the runner up, and one for the rest.
winningCandidate, runnerUpCandidates, *theRest = candidatesRankedByVote

# View those four variables.
print('Winner:', winningCandidate,
      'Runner Up:', runnerUpCandidates,
      'The Rest:', theRest,
      )

