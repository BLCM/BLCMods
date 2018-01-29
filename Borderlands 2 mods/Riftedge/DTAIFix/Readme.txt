I'm not good at English so the following description may looks strange LOL

How I make this mod:

DeathTrap's AI config is in GD_Tulip_DeathTrap.AI.WillowAIDef_DeathTrap. Dump it and you'll find that the AIDef is formed of several nodes. Actually, there are 4 kinds of node: NodeType_Priority, NodeType_Action, NodeType_Random and NodeType_Sequential. They all have an attribute called Children, and DeathTrap will execute nodes in their Children attribute by Priority, randomly or sequentially. This is the tree of DeathTrap's AI. It starts with node(0) called Tree.
Besides, most nodes have attribute CanRunIf and Action.
The problem here is that the priority of shock attack is too high and it's CanRunIf attribute is wired. It could be run when "target is flying or target is not phaselockable". So DeathTrap will always use shock attack against most bosses, which are not phaselockable.
Other modification are mostly easy to understand.

NodeType_Sequential will somewhat make DeathTrap stuck. So I extract shock ball, rampage, explosive clap and laser from their original sequences and put them into the main node "Prority" directly. This actually give them priority which does not exist in vanilla Borderlands 2. But this prevent DeathTrap from being stuck sometimes.

DeathTrap will try to go to the opposite side of Gaige when using any melee attack, including normal melee and rampage. This is because some enemies' hitboxes are strange. For example, DeathTrap is not able to deal damage to Wilhelm when facing his back because of the gaps. So this will give player some kind of ability to reposition DeathTrap.

After decrease the prority of shock attack, DeathTrap will stuck in the following situation:
Target runs away from DeathTrap, then DeathTrap run after it trying to use melee attack. Target stops suddenly and doesn't move, DeathTrap will hit the target and cannot move either. Then DeathTrap stops any movement and just stares at target.

This is the most difficult problem while writing this mod. I spent over 12 hours on this and finally came up with a solution. I add a TimedFail to all melee attack, so when DeathTrap trying to melee and get stuck on that situation, the present melee attack will fail after several seconds, then DeathTrap will countinue the Prority sequence. This may seems a little bit stupid but it works really well. DeathTrap now could perform attacks smoothly.
I think this is because of the function WillowGame.Action_FlyAnimAttack:MoveToTarget. This may be called automatically.

I also modify the CanRunIf attribut of some attacks so DeathTrap won't try to use melee attack, Explosive Clap or Shock Ball against flying target. This is not perfect because of Bunker and Bloodwing. 

I'm still new to modding so this mod is far from perfect. But it's already usable now.