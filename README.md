```markdown
# QA Analyst Technical Assessment

**Candidate:**  Nadia Aimandi
**Language Used:** Python
**Completion Date:** 10/15/2025

## Part 1: Functional Programming
- **Time Spent:** ~30 minutes
- **Approach:** 
The function `remove_duplicates` uses Python’s `filter` with a `lambda` expression to remove duplicates while preserving the original order of the given list. The `lambda` function returns True if an element has not been seen before, allowing `filter` to keep it in the output list. If the element has already been seen, the `lambda` returns False, so `filter` skips it. A set is used to track seen elements, making the lookup operation O(1) on average. This requires the elements of the list to be hashable. Overall, this approach achieves O(n) time complexity.


## Part 2: API Testing  
- **Time Spent:** ~30 minutes
- **Approach:** 
The `pytest` library was used for testing the target API's endpoints. Each test verifies the status code corresponding to the specific request (GET, POST, etc.) and checks the correctness of the response content. Error messsages were added to help pinpoint issues if a test fails.

## How to Run
### Part 1
python solution.py

### Part 2
1. Install dependencies:
       pip install pytest requests

2. To run all tests:
       pytest -v solution.py

