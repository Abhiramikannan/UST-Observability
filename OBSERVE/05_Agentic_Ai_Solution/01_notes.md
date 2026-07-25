# Create a agentic Ai solution which can fetch the data of failed order id from all 3 tools (Observe,Newrelic,Logz) and Give RCA analysis Using LLM and ClaudeCode.
- shridhar have shared a folder , he created using copilot, rakesh integrated newrelic and logz and my task is to integrate observe also and implement agentic solution for all 3
- Approach is like creating a instructions file called rca_instructions.md  and sending the instructions file and the json file(output of all 3 tools of particular order id we searched) to llm and get the RCA(Root Cause) analysis based
   on the rules written in the instructions file.

# Test all 3 connections:
python3 validate.py --test-only 

# Run the command to get order id details from all 3 tools and in failed.json
python3 validate.py --transaction-id <orderid> --loopback 30 --json

# Creating Observe_connector.py to fetch the details of order id from Observe also.
- It contains query to search the particular order id in the whole body of logs.
- return logs which contains that order id.
