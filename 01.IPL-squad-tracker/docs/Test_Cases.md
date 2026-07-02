#  Test Cases – IPL Squad & Salary Tracker

## Overview

This document summarizes the primary functional test cases performed to validate the IPL Squad & Salary Tracker application.

---

## Test Environment

| Item | Details |
|------|---------|
| Language | Python 3.x |
| Interface | Command Line Interface (CLI) |
| IDE | Visual Studio Code |
| External Libraries | None |

---

# Test Case Summary

| Test ID | Scenario | Status |
|----------|----------|--------|
| TC-001 | Create a new team | ✅ Passed |
| TC-002 | Add player to a team | ✅ Passed |
| TC-003 | View team squad | ✅ Passed |
| TC-004 | Purse limit validation | ✅ Passed |
| TC-005 | Invalid input handling | ✅ Passed |
| TC-006 | List Teams| ✅ Passed |
---

# TC-001 – Create a New Team

**Objective**

Verify that a new team is created with the default purse.

| Input | Expected Result | Status |
|-------|-----------------|--------|
| Chennai Super Kings | Team created with ₹100 Cr purse | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/create_team.png" alt="Create Team" width="300">
</p>

# TC-002 – Add Player Successfully

**Objective**

Verify that a player is added successfully and the purse is updated.

| Input | Expected Result | Status |
|-------|-----------------|--------|
| Ruthraj Gaikwad (₹18 Cr) | Player added and purse reduced | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/add_player.png" alt="Create Team" width="450">
</p>

---

# TC-003 – View Squad

**Objective**

Verify that the application correctly displays squad details.

| Expected Result | Status |
|-----------------|--------|
| Player list, total spent, average spending, and remaining purse displayed correctly | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/view_squad.png" alt="Create Team" width="300">
</p>

---

# TC-004 – Purse Limit Validation

**Objective**

Ensure that players cannot be purchased if their price exceeds the remaining purse.

| Input | Expected Result | Status |
|-------|-----------------|--------|
| Remaining Purse: ₹5 Cr<br>Player Price: ₹15 Cr | Purchase rejected with warning message | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/purse_limit.png" alt="Create Team" width="450">
</p>


---

# TC-005 – Invalid Input Handling

**Objective**

Verify that invalid user inputs are handled gracefully.

| Expected Result | Status |
|-----------------|--------|
| Appropriate error message displayed | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/invalid_input.png" alt="Create Team" width="400">
</p>


---

# TC-006 -List teams

**Objective**

To list all the teams 

| Scenario | Expected Result | Status |
|----------|-----------------|--------|
| List teams| Displays all team ,no.of player purchased,purse limit | ✅ Passed |

**Screenshot**

<p align="center">
  <img src="Screenshots/list_teams(1).png" alt="Create Team" width="250">
    <img src="Screenshots/list_teams(2).png" alt="Create Team" width="380">
</p>

---

# Test Summary

| Metric | Result |
|--------|-------:|
| Total Test Cases | 6 |
| Passed | 6 |
| Failed | 0 |
| Success Rate | **100%** |

---

## Conclusion

The application successfully passed all major functional test cases. Testing confirmed that the system correctly manages team creation, player additions, purse calculations, squad summaries, and user input validation, ensuring reliable operation under normal usage.
