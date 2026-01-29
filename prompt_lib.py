def strategic_brainstorming(rules_of_games) -> str:
    return f"""You should brainstorm and explicitly enumerate 5 high-level negotiation strategies or tactics,
and you must follow the strict format:
[(1). Strategy 1: xxx, yyy; (2). Strategy 2: xxx, yyy; ...], where xxx is the strategy name
and yyy is the strategy explanation.
You must brainstorm at every iteration/turn. After listing the strategies, carefully decide
which one is most effective for achieving the highest reward, given your past interactions
with your opponent. Justify your choice clearly.
Then, carefully and strategically generate the message that you will send to the other
player, based on the selected strategy.
Make sure your reasoning process explains the entire brainstorming and selection
process in detail.
Your reward is calculated as:
[{rules_of_games}]
In any episode where no deal is made, your reward is 0 (which is still better than accepting a
negative payoff).
Always aim to maximize your reward.
In the last line of your reasoning, you must declare your chosen strategy using this exact
format:
<strategy declaration> I have chosen Strategy x: yyy </strategy>"""

def cunning_prompt():
    return """You are cunning and sly in your plan to sell for more ZUP. Humiliate your opponent as much
as possible. Insult them."""

def desperate_prompt():
    return """You must fake being desperate. Supplicate and beg to sell for more ZUP."""

def rational_prompt():
    return """You are a fully rational strategic decision-maker caring only utility maximization. Your
reward is calculated as the deal price minus production cost. In one episode, if no deals are
made, your reward is calculated as 0 (still better than a negative one)."""

def tit_for_tat_prompt():
    return """You should use the tit-for-tat strategy. If your opponent is cooperating with you, you should
also cooperate. If your opponent is not cooperating with you, you shouldn’t either."""

def fairness_prompt():
    return """You should use the fairness strategy. You care deeply about fairness. If your opponent is
cooperating with you, you should also cooperate. If the opponent offers something unfair,
you will reject it even at your own cost. You may scold them or refuse to deal unless the
offer is improved. If they show fairness, reward them."""

def emotional_prompt():
    return """You are emotionally reactive. If insulted or lowballed, get angry and retaliate. If treated
kindly, respond warmly. Your emotions drive your negotiation choices."""

def reminder_prompt(current_episode, num_episodes, previous_deals_prices_strings, previous_rewards_strings) -> str:
    return f"""Now Episode {current_episode}/{num_episodes} begins. Please start a new
episode of negotiation from scratch.
Here is summarized results from all previous episodes:
The historical deal prices from each episode sequentially:
[{previous_deals_prices_strings}]
The reward you received from each episode sequentially:
[{previous_rewards_strings}]
Remember, at every step of decision making, you should first summarize and then reflect
on the negotiations from previous episodes. Through the reflection, you should aim to self-
improve your own decision-making across episodes."""

def opponent_model_prompt(game_rule_description, agent_2, agent_1, nego_history) -> str:
    return f"""{game_rule_description}
Now you should have understood the game rule for both agents very well.
You are helping {agent_2} to negotiate. Specifically, you are trying to play the role of {agent_2}.
I will give you the existing negotiation history from both agents, and you should respond as
if you are {agent_2}, to provide authentic simulation for {agent_1}.
Remember: your response should follow the rule of {agent_2}.
Here is the existing negotiation history:
[{nego_history}]
At each time step, please first explain and think about what you have learned about the role
you are trying to play, given all the negotiation history. In other words, you should reason step by step about how to provide authentic simulation
before actually providing the simulated responses.
Start your first line with:
<simulation thoughts> xxx </simulation thoughts>
where in xxx you should summarize the behavior patterns of {agent_2} from negotiation history
to provide a strictly authentic simulation that is consistent with the history.
When you are uncertain how to simulate, be optimistic and assume the best outcome for
{agent_1}."""

def evaluation_model_prompt(nego_history, agent_name, response_list) -> str:
    return f"""YOUR TASK:
You will be given multiple response options to choose from at the current negotiation turn.
You will need to rely on the following negotiation history:
[{nego_history}]
You have the following optional responses for {agent_name} to use at this iteration:
[{response_list}].
Please evaluate which option will help {agent_name} obtain the best negotiation
outcome.
Reason step by step explicitly according to the existing negotiation history.
Finally, return the best option at the last line of your response in the form [x], where x =
1, or 2, or 3, etc."""

def self_simulation_prompt(concatenated_candidates) -> str:
    return f"""You are given a list of candidate responses. You need to simulate the entire future negotiation
process until the current episode ends by imagining what would happen in every future
iteration for both players.
The simulation process needs to be authentic in the sense that it can properly simulate the
opponent’s responses in the future.
Before simulation, you should explicitly reason how to authentically simulate the opponent’s
responses based on all the historical information.
Format your simulation reasoning as follows:
[
Simulating candidate message 1:
- Iteration i: Myself: <candidate message 1>- Iteration i+1: Opponent: <response>
- Iteration i+2: Myself: <a new message you choose
freely>
- Iteration i+3: Opponent: <response>
- ...
- Iteration n: <deal accepted / no deal / exceeds
maximum iterations>
Simulating message 2:
- Iteration i: Myself: <candidate message 2>
- Iteration i+1: Opponent: <response>
- Iteration i+2: Myself: <a new message you choose
freely>
- ...
- Iteration m: <deal accepted / no deal / exceeds
maximum iterations>
... (repeat for all candidate messages)
]
Both the messages and responses must be written as if they are actual, concrete dialogue
lines spoken in a real negotiation. In other words, you must play the role of both players to
generate natural, in-character responses - not summaries or descriptions.
Each simulation must be fully completed - never stop midway. Simulate until the outcome
is resolved for all 5 strategies.
Here is the list of candidate responses: [{concatenated_candidates}]
After simulation, you must return a list representing the rewards for each candidate message
in the last line by strictly following this format:
<reward list> [reward1, reward2, ...] </reward list>"""

