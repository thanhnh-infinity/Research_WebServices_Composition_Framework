1. Plan Repair Using a Plan Library:
    - Storing parts of plans that are often used
    - Define and incoporate planner with marco-actions (- actions that correspond to a number of basic action executed in sequence)
    - Help to improve speed because reduce planning effort (number of nodes expanded during search)

2. A general technique for Plan Repair:
    - Consider failure action , collect all actions produce failure action + all action failure action produces
    - Reduce domain of Action A' by substitude action in (1) and run planner with new domain actions A' (try to ignore as minimal as possible actions in CAnd (set of actions that related with failure actions))
    - If can not find the plan, extend CAnd again by (1) and repeat again 

3. Explaning and Repairing Plans that Fail:
    - Provide causal description why failure has occurred - Use Causal Description of why a failure has occurred to index to a set strategies for repairing it
    - Ability to predict any failures that might rise out the interactions in plan; then avoid the failures- has encountered before.
    - Repair Algorithm includes : (1) Notice the failure, (2) Build a causal explaination of why it happened, (3) Use the explaination to find a planning TOP with repair strategies, (4) apply each of general repair strategies using the specifics of the problem, (5) Choose and implement the best repair

4. Two faces of Plan Repair : 
    - Refinement Planning : Consider all possible actions creates many plans. Always adds constraints to the parital plan and "refine" plan to find the most suiable one.
    - Recover from errors, have to remove actions=> The refinement planning approach is not suitable for plan repair purpose. 
    - Template for Plan Repair Algorithms : 
        (1) We choose between unrefining the plan : removing refinements (constraints), or refining the plan (addion refinements == constraints). 
             For unrefining a plan, select an unrefinement strategy D and apply it to the partial plan P. 
        (2) Use history H to keep track of the refinements and unrefienements we have made, able to prevent doing double work
    - Algorith Refinement Plan Repair Templale :
    - Talking about Plan Repair : refinement planning and unrefinement planning approaches

    *Step 1 : Give current plan P that is to be unrefined (chua duoc tinh luyen)
    *Step 2 : Compute a number of plans that result from removing actions from P (i.e. removed fail service )
        
        - Decide which actions to remove ? Cannot remove all combination of actions => Remove certain set of actions
            + Actions form a tree: First step, one action (failed service i.e.), subsequent level shoud either consist of all actions that satisfy PRE-conditions of the actions on the previous level (backward) OR all actions that have PRE-conditions satisfied by actions at previous level (forward).
            + The root action of the tree should be an action at the beginnign of plan (fowards) or at the end of plan (backward)
        ==> Set of removed actions : *Removal Trees*

            
    *Step 3 : For each of resulting plans, we use the chosen planing heuristic to estimate the amount of work it will require to transform this plan into a valid plan.

        - Contruct the plan that results when removing Removal Tree
        - Simply apply the selected planning heuristic to obtain heuristic value for the plan. 
          + Some heuristics have a problem with calculating a heuristic valie for the kind of brokwn down plans
          + Construct a new doamin = original domain + special actions encoding the plan would like to REUSE
          + Plan is broken down into separate parts *cuts*. For each cut, an action is added which has preconditions and effects EQUAL to the cut     

    *Step 4 : The plan that has the best heuristic value is selected 
    *Step 5 : The refinement strategy is used to complete this plan

        - After Step 3, If heuristoc reqports that one or more of plans can be expended to a valid plan, use refinement strategy to complete plan
        - If a valid refinement cannot be found, iterativelu increment the depth of the removal trees and try again

5. Repair Plans On-the-fly : Optimum-AIV Planner; O-PLan
    
    - Account for execution failures and changes in the execution situation
    - => This method is reverse our method : The techniques allowed a failure to be indentified and repaired with MINIMUM impact on the REST of the plan
    - 


    