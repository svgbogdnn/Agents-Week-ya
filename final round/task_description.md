# Task Description

## Task A,B,C

### Agents Week Jupyter 1

In this homework you will build agents for a small online electronics store (headphones, earbuds, keyboards, mice, and e-readers). There are three tasks, each introducing a new architecture:

- Tool-Calling Agent (ReAct loop) — the model searches products and manages a shopping cart by calling tools in an iterative ReAct loop. You will write docstrings for the tool functions, generate a tool schema with convert_to_openai_tool, and implement run_shopping_agent — the ReAct loop that sends messages to the LLM, executes tool calls, and returns the final text response.
- Memory Agent — the agent gains long-term memory (a user profile saved to disk) and short-term memory (conversation history), so it remembers preferences across sessions and past search results within a session. You will implement load_profile / save_profile for reading and writing a JSON profile, define the update_profile tool schema, and implement run_memory_agent that injects the profile into the system prompt and carries conversation history between turns.
- Multi-Agent System — four specialized agents — Retriever, Pros Analyst, Cons Analyst, and Ranker — coordinated by an Orchestrator that delegates work, collects results, and produces a final recommendation with honest pros & cons. You will implement all four agent classes and the CoordinatorAgent that runs them in a chain, passing data through a shared AgentContext.

Detailed instructions, starter code, and open test cases are in the notebook.

Important: all submissions are graded using the gpt-oss-20b model. Use the same model when developing and testing your solutions — this way the agent's behavior during grading will match what you observe locally.

Look for problem statement and instructions inside the notebook. Notebook you can find inside Jupyter server in the first task.

## Task D

### Q1 Agent architecture

According to the definition used in this course, which of the following components may be part of an AI agent architecture?

**Please select all that apply**

- If you selected all the correct answers - 3 points
- If more than 2/3 of answers are correct - 2 point
- If more than 1/3 and less then 2/3 of answers are correct - 1 point
- If you selected one and more incorrect answers - zero points
- If the answer is completely incorrect - zero points

**Choose correct options**

- Training dataset
- Guardrails
- System prompt
- Model
- User interface
- Runtime
- Context window
- Tools
- Planning skills
- Reward model
- Memory

## Task E

### Q2 Strengths and weaknesses of LLMs

You are developing a system based on an LLM without access to external tools or memory. Which of the following tasks will the model most likely perform reliably?

**Please select all that apply**

- If you selected all the correct answers - 3 points
- If more than 2/3 of answers are correct - 2 point
- If more than 1/3 and less then 2/3 of answers are correct - 1 point
- If you selected one and more incorrect answers - zero points
- If the answer is completely incorrect - zero points

**Choose correct options**

- Paraphrase a text while preserving its meaning
- Count how many times the letter “r” appears in the word strawberry
- Generate a short summary of a long article
- Report the current EUR exchange rate
- Explain the difference between two programming concepts
- Sort a list of 200 random numbers

## Task F

### Q3 Special tokens and tool calling

A developer accidentally removes the special tokens that mark the start and end of tool calls from the tool-description prompt section, but keeps the tool description and the tool result text in the prompt. What is the most likely consequence?

**Choose correct option**

- The LLM will still reliably call the tool because the tool description and tool result text are present in the prompt
- The LLM may start treating tool outputs as normal conversation text and become less reliable at deciding when to call tools
- The model will fail to run because tool calling requires these tokens at the tokenizer level
- The runtime will automatically reconstruct the missing special tokens

## Task G

### Q4 Tool Calling

In an agent system, an LLM has access to a tool get_weather(city). A user asks: “What is the weather in Berlin right now?” How does the tool call actually occur?

**Choose correct option**

- The LLM directly executes the get_weather function in the runtime and receives the result
- The LLM outputs a structured tool call; the agent executes the tool and sends the result back to the model
- The runtime automatically calls the tool when it detects a weather-related question
- The LLM sends an API request to the weather service and then produces the final answer

## Task H

### Q5 Best Practices for Tools

An agent uses the following tool: book_flight(user_id, flight_id) Internally, the tool performs several actions:

- charges the user’s payment method
- reserves a seat on the flight
- creates a booking record
During execution, the system successfully charges the payment , but fails before creating the booking record.

The agent then retries the tool call. How should the tool be designed to prevent an inconsistent system state (for example, charging the user twice)?

**Choose correct option**

- The tool should check whether the booking or payment already exists before executing again
- The agent should lower the model temperature to reduce the probability of repeating the tool call
- The model should remember the previous tool call in the context window and avoid calling it again
- The runtime should forbid retrying tool calls after a failure

## Task I

### Q6 MCP Architecture

Which of the following statements correctly describe the roles in the MCP architecture?

**Please select all that apply**

- If you selected all the correct answers - 3 points
- If more than 2/3 of answers are correct - 2 point
- If more than 1/3 and less then 2/3 of answers are correct - 1 point
- If you selected one and more incorrect answers - zero points
- If the answer is completely incorrect - zero points

**Choose correct options**

- An MCP server creates MCP clients to connect to MCP hosts
- A host creates MCP clients to connect to MCP servers
- MCP servers execute tools and return structured results
- A single host can connect to multiple MCP servers using clients
- An MCP client is the user interface of the application
- A single client can connect to multiple MCP servers

## Task J

### Q7 Semantic gap

Users often phrase queries in colloquial language, while documents use formal/technical vocabulary. Which RAG query transformation technique from the lecture 2 is designed to bridge this semantic gap?

**Choose correct option**

- Query Rewriting (Contextualizing)
- Query Decomposition (Multi-Query Expansion)
- Two-Stage Retrieval with Cross-Encoder
- HyDE (Hypothetical Document Embeddings)

## Task K

### Q8 Continued Pretraining vs. SFT

According to the lecture 2, what is the primary purpose of Continued Pretraining vs. SFT (Supervised Fine-Tuning)?

**Choose correct option**

- Continued Pretraining = behavior; SFT = knowledge
- Continued Pretraining = knowledge; SFT = efficiency
- Continued Pretraining = knowledge; SFT = behavior
- Continued Pretraining = efficiency; SFT = knowledge

## Task L

### Q9 Practical strategy

The lecture 2 recommends a practical strategy for choosing between RAG and Training. What is it?

**Choose correct option**

- Always use Training — it gives better results
- Use RAG for factual questions and Training for creative tasks
- RAG first; Training when RAG hits its ceiling
- Use both simultaneously from the start

## Task M

### Q10 Key difference

According to the lecture 2, what is the key difference between Prompt Injection and Jailbreaking?

**Choose correct option**

- Injection uses social engineering; Jailbreaking uses code
- Injection overrides agent instructions; Jailbreaking overrides model safety
- Injection targets the output; Jailbreaking targets the input
- Injection is indirect; Jailbreaking is direct

## Task N

### Q11 Type of hallucination

An agent "decides" the user gave consent and skips a confirmation step, even though the user never actually consented. According to the lecture 2, which type of hallucination is this?

**Choose correct option**

- Action Hallucination
- Instruction Adherence Failure
- Factuality Hallucination
- Prompt Injection

## Task O

### Q12 ReAct vs Chain-of-Thought

ReAct = Reasoning + Acting. In the lecture 3 we compared ReAct with Chain-of-Thought. On which tasks is CoT better than ReAct?

**Choose correct option**

- Nowhere — ReAct is always better
- Arithmetic tasks
- Question answering
- Tasks with tools

## Task P

### Q13 External CoT prompt for reasoning models

If you add an external CoT prompt ("think step by step") to reasoning models (o1, DeepSeek-R1), the result:

**Choose correct option**

- Will improve
- Will not change
- May worsen
- The model will refuse to answer

## Task Q

### Q14 Function calling: content in AIMessage

In function calling, the content field in AIMessage before tool_call is usually:

**Choose correct option**

- Contains detailed reasoning
- Empty
- Contains a minimal plan of all steps
- Duplicates the parameters of tool_call

## Task R

### Q15 Agent with many tools

An agent with access to 50 tools performs worse than one with 10 tools on the same tasks. Why?

**Choose correct option**

- More tools = more tokens in context = less room for reasoning
- The model gets confused when choosing from many options
- Both factors + attention degradation on long tool descriptions
- This is a myth — more tools is always better

## Task S

### Q16 Decentralized MAS: main unsolved problem

In decentralized Multi-Agent Systems (MAS), the main unsolved problem is:

**Choose correct option**

- Speed — too slow
- How to achieve consensus / avoid infinite communication loops
- Tools cannot be used
- All agents must use the same model

## Task T

### Q17 Next step

You run your LLM-as-Judge on 50 test cases and get Cohen's κ = 0.2 for the "efficiency" dimension. What is the right next step?

**Choose correct option**

- Increase the number of test cases to 500 — κ is too noisy on small samples
- Look at the specific cases where judge and human disagree, find a pattern, fix the prompt
- Switch to a stronger model — GPT-4 will give higher κ automatically
- Accept the result — κ = 0.2 is above zero, the judge is working

## Task U

### Q18 Problem with this evaluation

A team built an agent that cancels flight bookings. To test it, they wrote: "test passes if the word 'cancelled' appears in the agent's final message." After 100 runs, the pass rate is 87%. The product manager is happy. What is the problem with this evaluation?

**Choose correct option**

- 100 runs is too few — you need at least 1000
- The test checks the agent's text, not the actual state of the booking in the database
- The agent should be tested by humans, not automatically
- There is no problem — 87% is a good result

## Task V

### Q19 Sequential steps

You have an agent that completes a task in 10 sequential steps. Each step succeeds independently with probability 0.9. Approximately what fraction of tasks does the agent complete end-to-end without a single failure?

*(Enter a number in percent, rounded to the nearest 5%)*

## Task W

### Q20 Cut costs and switch

Your team spent two weeks writing a detailed, carefully calibrated prompt for a GPT-4o mini judge — and achieved κ = 0.81. Management asks you to cut costs and switch to GPT-3.5. What will most likely happen?

**Choose correct option**

- κ will stay the same — the prompt is the same, only the model changes
- κ will improve — a simpler model follows instructions more literally
- κ may drop significantly — the prompt was co-tuned with the stronger model and may not transfer
- κ will drop slightly, within measurement error

## Task X

### Q21 Chain-of-thought reasoning

A team wants to find out whether adding chain-of-thought reasoning to their judge prompt improves agreement with human labels. In the same experiment, they also switch from GPT-4o mini to GPT-4o. After the experiment, κ goes up from 0.41 to 0.67. What conclusion can they draw?

**Choose correct option**

- Chain-of-thought improved the judge
- The stronger model improved the judge
- Both changes together improved the judge, but it is impossible to say which one caused the gain
- The result is unreliable — both changes must always be tested together

## Task Y

### Q22 Agent tools

Your agent has 28 tools. It consistently picks the wrong tool for simple queries and spends 10x more tokens than needed. What do you fix?

**Choose correct option**

- Switch to a bigger model with better reasoning
- Add more detailed instructions in the system prompt
- Semantic tool filtering. Give the agent only 3–5 relevant tools per request
- Remove all tools except the 5 most used ones
- Add a retry loop until the agent picks the right tool

## Task Z

### Q23 What should you do?

Your agent solves tasks with 90% success rate, but average latency is 25 seconds. Users abandon after ~8 seconds. What should you do?

**Choose correct option**

- Switch to a smaller, faster model even if accuracy drops
- Add caching for repeated queries
- Break task into multi-step pipeline with fast routing + slow reasoning only when needed
- Add loading indicator so users wait longer
- Increase timeout threshold

## Task AA

### Q24 Refund

Your agent uses an LLM to decide whether to refund a customer. It sometimes approves clearly invalid refunds. What is the best fix?

**Choose correct option**

- Add more examples to the prompt
- Switch to a more powerful model
- Add a retry loop
- Move refund decision logic to deterministic rules and use LLM only for interpretation
- Lower temperature to 0

## Task BA

### Q25 Support agent

Support agent worked great for 3 months, then CSAT dropped sharply. Prompt didn't change, model wasn't updated. Most likely cause?

**Choose correct option**

- Users are sending more complex queries than before
- Server infrastructure degraded
- LLM provider secretly changed the model
- Prompt was too short from the beginning
- Data in RAG became outdated (knowledge rot)

