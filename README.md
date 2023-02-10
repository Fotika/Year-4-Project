Decision Making Under Uncertainty 
  
Problem Description 
Managers deal with a number of decisions about processes, capacity, location, inventory, etc. 
The process of making a decision is complicated because of the uncertainties of the future. 
This implies that the future outcomes of alternatives that we consider today are in doubt.  
The aim of this project is to build a decision support system that allows the user to make 
decisions  under  uncertainty. I describe  a  systematic  approach  that  can  be  used  by 
managers in the process of making decisions.  
 
Solution approach 
Step 1: 
List the feasible alternatives. 
Step 2:   
List the events that have an impact on the outcome of each alternative but are not under 
managers’ control. 
Step 3: 
Estimate the payoff for each alternative in each event. 
Step 4: 
Estimate the likelihood of each event using past data, executive opinion, or other forecasting 
methods. 
Step 5: 
Select a decision rule to evaluate the alternatives, such as choosing the alternative with the 
lowest expected cost or choosing the alternative with the maximum expected profits.  
The following are decision rules to help the managers select an alternative.   
Maximin: Choose the alternative that is the “best of the worst.” This rule is for the pessimist 
who anticipates the “worst case” return for each alternative. 
Maximax: Choose the alternative that is the “best of the best.” This rule is for the optimist who 
anticipates the “best case” return for each alternative. 
Laplace:  Choose the alternative with the best-weighted payoff. To find the weighted payoff, 
give  equal  importance  to  each  event.  For  example,  if  there  are  n  events,  the 
probability assigned to each event is 1/n. This rule is for the realist. 
Minimax: Choose the alternative that gives the best “worst regret.” Calculate a table of regrets 
in which the rows represent the alternatives and the columns represent the events. 
A regret is the difference between a given payoff and the best payoff in the same 
column. For an event, it shows how much is lost by picking an alternative to the 
one that  is  best  for  this event.  The  regret  can  be  lost  profit  or  increased cost, 
depending on the situation.   
User Interface 
1.  Build a welcome form. 
 
Case Study        Decision Making Under Uncertainty 
 
2.  Build a data analysis menu. The following are suggestions to help you design this menu.  
a.  The user types in the total number of events (n) and the total number of alternatives 
(m).  Upon  submission  of  this  information  a  table-menu  appears.  This  table  has 
dimensions m by n. The user types in this table the payoff of each alternative in each 
event. Label the rows by the name of alternatives. Label the columns by the name of 
events. 
b.  Create an option on the menu titled “Enter the Likelihood of Events.” When the user 
selects this option, a table-menu with dimensions 1 by n appears. The user types in 
this table the likelihood of each event, if this information is available.        
c.  Create an additional menu named “Selection Rules.” The menu includes five options. 
The options enable the user to select one of the following decision rules: maximin, 
maximax, Laplace, minimax regret and expected payoff. When the user elects one 
of them, the decision rule chosen applies, and the user is prompted about the best 
alternative found. Note that the expected payoff decision rule applies in the case that 
the user has provided information about the likelihood of the events. 
3.  Build a menu that allows the user to access the reports created.   
 
Reports 
1.  Present the table of regrets for the proposed alternatives. 
2.  Report the best alternative found using the maximin, maximax, Laplace, minimax regret 
and expected payoff methods.   
 

