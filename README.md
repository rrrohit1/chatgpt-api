# chatgpt-api

## Typees of LLMs
1. **Base LLM**: Predicts the next word, based on text training data
2. **Instruction Tuned LLM**: Tries to follow instructions. Fine-tune on instructions and good attempts to follow those instructions. Start off with Base LLM and train with input-output training. (RLHF: Reinforcement Learning with Human Feedback) Less likely to output harmlful outputs.

## Guidelines
1. Principle 1: Write clear and specifc instructions:
    - Use delimiters to separate text, and allows prompt injections (any contradictory instruction in the text).
    - Ask for structure output: HTML, JSON
    - Check whether conditions/assumptions are satisfied by the output
    - Few-shots prompting: give good examples in prompts and then ask the model to perform a task
2. Principle 2: Give the model time to think
    - Specify the steps to complete a task
    - Instruct the model to work out its own solution, without rushing to a conclusion
  
  **Limitations**:  Hallucination: make statements which are plausible but not true. A way to reduce it is to first find relevant info and then answer the question based on the info.
