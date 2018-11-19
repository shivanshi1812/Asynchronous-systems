CSE535 Asynchronous Systems  Assignment 4
Name: Shivanshi Gupta        
ID: 112079392


QUESTION 1 and QUESTION 2 in separate word file.

QUESTION 3:

1. For PREEMPT version, we add the preempt to the code in acceptors receive event. If the acceptor gets the proposal, and the proposal number is greater than the existing proposal number, it would send “ACCEPT” to the proposer.
        In PREEMPT : If the proposer sends the proposal with a number lesser than the previous value that acceptor promised to, the acceptor will send a preempt to the proposer, stating that this was the maximum value that I have. On receiving PREEMPT, the proposer would return nothing.

        CORRECTNESS : 
        
1. AGREEMENT : The learners on learning the value, send (“learned”) to the monitor and monitor on receiving (“learned”) from each of the learner, verifies if all the learners learned the same value. If yes then returns “agreement not violated”.
2. VALIDATION : The learners should learn the values which are proposed by the processes. This is checked by monitor by looking for values in “proposed”, if yes, then validity exists is returned.
3. TERMINATION : Termination can happen in 2 ways (i) When learners learn a value.
(ii) When the timeout happens.
Both of these cases are checked by monitor to identify whether the termination occurred due to timeout of learners learning a value


THE CORRECTNESS IS VERIFIED FOR BOTH “PREEMPT VERSION” AND “BASIC VERSION” OF PAXOS

RUNNING TIMES can be calculated by : CPU time and ELAPSED times of the process. The graphs are plotted with CPU times and ELAPSED times with varying range of mesage delay (d), mesage loss rate(r), message wait around time(w). 

The only input that needs to be given is :

python -m da.compiler main.da     .
Python -m da main.da 3 2 1 
{rest all args can be explicitly given or even left}
Minimum values that needs to be given for each are given in the program. 

print(CPULossRate)
        print(ElapsedLossRate)


Are used to print the elapsed time and CPU time while keeping ‘r’ fixed and varying all other factors. Same is for other two parameters (d and w). We are using same print statement to display the times by keeping one parameter constant at a time and changing other factors.


RANGES OF INPUTS : 
Range of “Message Loss Rate” = varies over a range of 0 to 1 for input 0.3 it goes 0.06, 0.12,0.18,0.24,0.30 
Range of “Message Delay Rate” = varies over a range of 1 to 5 i.e for input 5 it goes 1,2,3,4,5
Range of “Wait time” = varies over a range of  1 to 5 i.e for input i.e for input 5 it goes 1,2,3,4,5


Standard Deviation  : 
I am using stdev function (from statistics import stdev) and then printing stdev averaged over the runs for both elapsed time and cpu time.

ANALYSIS:

CPU time for basic paxos and paxos with preemption is almost same.

1. MESSAGE LOSS RATE
 (when high)
1.1 For basic paxos: Elapsed time is greater than CPU time.
1.2 For Preemption paxos :  Elapsed time is almost equal to CPU time.
Result: Preemption paxos performs better.

(when Low)
        Preempt paxos elapsed time is greater than basic paxos.
Result: Basic paxos performed better

      2. MESSAGE DELAY RATE 
        (when high)
1.1 For basic paxos: Elapsed time is greater than CPU time.
1.2 For Preemption paxos :  Elapsed time is almost equal to CPU time.
Result: Preemption paxos performs better.


(when Low)
        Preempt paxos elapsed time is greater than basic paxos.
Result: Basic paxos performed better


3. Wait Around Time
 (when high)
1.1 For basic paxos: Elapsed time is greater than CPU time.
1.2 For Preemption paxos :  Elapsed time is almost equal to CPU time.
Result: Preemption paxos performs better.


(when Low)
Preempt paxos elapsed time is equal to basic paxos:

ALSO PLEASE REFER "Graphs for reference" folder for any more information.















Reference: Collaborated with Shivsagar boraiah(112077826), ishika agarwal(111971057), akanksha mahajan(112074564)