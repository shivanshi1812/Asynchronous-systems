Name - SHIVANSHI GUPTA
SBU ID - 11207392
ASSIGNMENT 3

FOR SPEC 1: 

1. The parameters of the algorithm are: number of processes, and maxClock. The input is taken by varying the 2 paramteres. eg. N - 2 , maxclock -5
2. The ClockConstraint was added everytime during running of spec.
3. Also the liveness property was added in the code.
3. Mutex(invariant) and Liveness(temporal property) were checked separately, ie while checking each one, I unchecked the checkbox for the other one.
4. Time taken to execute was calculated from the MS_TE.out file evrytime after running the spec. During this, all(deadlock, mutex, liveness) were unchecked.
5. Off heap memory and Heap memory was taken from progress output.
6. Number of states searched was taken up from states found in the Statistics under model checking results.
7. For checking deadlock condition : uncheck mutex, liveness and run the spec with Clock constraint and parameters.


For SPEC 2: 
 
1. The parameters of the algorithm are: processes, and maxClock. The input is taken by varying the 2 paramteres.The process needs to be a set of process e.g {1,2} and the operator needs to be written like p<q
2. The Mutex(invariant) and Acquiring eventually(temporal property) property was added in the code for safety and liveness respectively.
3. Mutex and Liveness were checked separately, ie while checking each one, I unchecked the checkbox for the other one.
4. Time taken to execute was calculated from the MS_TE.out file evrytime after running the spec. During this, all(deadlock, mutex, liveness) were unchecked.
5. Off heap memory and Heap memory was taken from progress output.
6. Number of states searched was taken up from states found in the Statistics under model checking results.
7. For checking deadlock condition : uncheck mutex, liveness and run the spec with Clock constraint and parameters.

For SPEC 3:

1. The parameters of the algorithm are: processes, and maxClock. The input is taken by varying the 2 paramteres.The process needs to be like 
2. Mutex(invariant) and Liveness(temporal property) were checked separately, i.e while checking each one, I unchecked the checkbox for the other one.
3. Time taken to execute was calculated from the MS_TE.out file evrytime after running the spec. During this, all(deadlock, mutex, liveness) were unchecked.
4. Off heap memory and Heap memory was taken from progress output.
5. Number of states searched was taken up from states found in the Statistics under model checking results.
6. For checking deadlock condition : uncheck mutex, liveness and run the spec with Clock constraint and parameters.
7. ClockConstraint was added for every run of spec.

For Spec4:
1. The parameters of the algorithm are: processes, maxClock, and default init value in Model_RAToken.
2. Specified the ClockConstraint in the state constraints.
3. Tried just for mutex(invariant) - it was getting violated. Added it in invariants.
4. For Deadlock and Safety , it was throwing errors, which I could not resolve.