#!/usr/bin/python3
'''Milestone_A_who_and_what.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

Dustin Langner & Brian Yu
CSE 415, Winter 2019
Milestone A
03/01/2019

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES = ['Baroque Chess Agent', 'Feature-Based Reinforcement Learning for the Rubik Cube Puzzle', \
              'Hidden Markov Models: Algorithms and Applications']


class Partner():
    def __init__(self, lastname, firstname, uwnetid):
        self.uwnetid = uwnetid
        self.lastname = lastname
        self.firstname = firstname

    def __lt__(self, other):
        return (self.lastname + "," + self.firstname).__lt__(other.lastname + "," + other.firstname)

    def __str__(self):
        return self.lastname + ", " + self.firstname + " (" + self.uwnetid + ")"


class Who_and_what():
    def __init__(self, team, option, title, approach, workload_distribution, references):
        self.team = team
        self.option = option
        self.title = title
        self.approach = approach
        self.workload_distribution = workload_distribution
        self.references = references

    def report(self):
        rpt = 80 * "#" + "\n"
        rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Winter, 2019
Milestone A

Team: 
'''
        team_sorted = sorted(self.team)
        # Note that the partner whose name comes first alphabetically
        # must do the turn-in.
        # The other partner(s) should NOT turn anything in.
        rpt += "    " + str(team_sorted[0]) + " (the partner who must turn in all files in Catalyst)\n"
        for p in team_sorted[1:]:
            rpt += "    " + str(p) + " (partner who should NOT turn anything in)\n\n"

        rpt += "Option: " + str(self.option) + "\n\n"
        rpt += "Title: " + self.title + "\n\n"
        rpt += "Approach: " + self.approach + "\n\n"
        rpt += "Workload Distribution: " + self.workload_distribution + "\n\n"
        rpt += "References: \n"
        for i in range(len(self.references)):
            rpt += "  Ref. " + str(i + 1) + ": " + self.references[i] + "\n"

        rpt += "\n\nThe information here indicates that the following file will need\n" + \
               "to be submitted (in addition to code and possible data files):\n"
        rpt += "    " + \
               {'1': "Baroque_Chess_Agent_Report", '2': "Rubik_Cube_Solver_Report", \
                '3': "Hidden_Markov_Models_Report"} \
                   [self.option] + ".pdf\n"

        rpt += "\n" + 80 * "#" + "\n"
        return rpt


# END OF BOILERPLATE.

# Change the following to represent your own information:


brian = Partner("Yu", "Brian", "brianpyu")
dustin = Partner("Langner", "Dustin", "dlangner")
team = [brian, dustin]

OPTION = '2'
# Legal options are 1, 2, and 3.

title = "Rubik's Dude"

approach = '''Our approach will be to first understand the state space and 
all the legal Rubik\'s Cube moves, to understand conceptually how specific 
optimizations can be applied to exploring the Rubik\'s Cube state space, 
develop a basic solver, then add options for a variable number of optimizations 
(i.e. Feature-based state representations, 180-degree moves, heuristics, etc)'''

workload_distribution = '''Brian will work on the problem formulation file.
Dustin will work on the Markov Decision Process definition. They will each pick
one of value iteration or Q-learning for the MDP. Together, they will design
a GUI to make gameplay more aesthetically pleasing.'''

reference1 = '''"Artificial Intelligence: Foundations of computational agents" 
by David Poole & Alan Mackworth. Can be found at: https://artint.info/html/ArtInt.html'''

reference2 = '''"Finding Optimal Solutions to Rubik\'s Cube Using Pattern Databases," 
by Richard E. Korf. Provided on the CSE 415 website at: 
https://courses.cs.washington.edu/courses/cse415/19wi/uwnetid/proj/korfrubik.pdf'''

our_submission = Who_and_what(team, OPTION, title, approach, workload_distribution, [reference1, reference2])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
    print(our_submission.report())
