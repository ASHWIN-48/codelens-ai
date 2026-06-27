from dotenv import load_dotenv
load_dotenv()

import json
from app.agents.graph import graph
from app.services.retrieval_service import retriever_service
from app.utils.repo_manager import repo_manager
from pathlib import Path
from app.core.config import settings
from langchain_core.messages import AIMessage, ToolMessage
from app.eval.testset import testset

import time

def run_with_retry(question, max_retries=2):
    for attempt in range(max_retries):
        try:
            result = graph.invoke({
                "question": question,
                "messages": []
            })
            return result
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)
    return None

repo_manager.current_repo_path = Path(settings.REPO_STORAGE_PATH)
retriever_service.load_index()

def extract_answer(messages):
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
            return msg.content
    return ""

def extract_contexts(messages):
    contexts = []
    for msg in messages:
        if isinstance(msg, ToolMessage):
            contexts.append(str(msg.content))
    return contexts

results = []

for item in testset:
    print(f"Running: {item['question']}")
    
    result = run_with_retry(item["question"])
    time.sleep(60)
    
    if result is None:
        print(f"Skipped after retries: {item['question']}")
        continue
    
    answer = extract_answer(result["messages"])
    context = extract_contexts(result["messages"])
    
    results.append({
        "question": item["question"],
        "answer": answer,
        "contexts": context,
        "ground_truth": item["ground_truth"]
    })
    
    print(f"Answer: {answer[:100]}...")
    print("---")
    
    print(f"Answer: {answer[:100]}...")
    print("---")

with open("eval_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved {len(results)} results to eval_results.json")