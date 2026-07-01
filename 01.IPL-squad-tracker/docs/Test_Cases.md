# Test Case Summary

| Test ID | Test Scenario | Expected Result | Status |
|----------|--------------|-----------------|--------|
| TC-001 | Create a new team | Team created successfully | ✅ Passed |
| TC-002 | Create duplicate team | Duplicate team warning | ✅ Passed |
| TC-003 | Add player successfully | Player added and purse updated | ✅ Passed |
| TC-004 | Add player to non-existing team | Error message displayed | ✅ Passed |
| TC-005 | Exceed purse limit | Player purchase rejected | ✅ Passed |
| TC-006 | View squad | Squad details displayed correctly | ✅ Passed |
| TC-007 | List all teams | All teams listed with purse and player count | ✅ Passed |
| TC-008 | Invalid price input | Validation error displayed | ✅ Passed |
| TC-009 | Invalid menu choice | Invalid choice warning displayed | ✅ Passed |
| TC-010 | Maximum squad size reached | Additional player rejected | ✅ Passed |

---

# Detailed Test Cases

---

## TC-001 — Create a New Team

**Objective**

Verify that a new IPL team can be created successfully.

| Parameter | Value |
|-----------|-------|
| Input | Chennai Super Kings |
| Expected Result | Team is created with ₹100.00 Cr purse |
| Actual Result | Team created successfully |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/create_team.png
```

---

## TC-002 — Duplicate Team Creation

**Objective**

Ensure duplicate team names are not allowed.

| Parameter | Value |
|-----------|-------|
| Input | Chennai Super Kings |
| Expected Result | "Team already exists." |
| Actual Result | Duplicate team prevented |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/duplicate_team.png
```

---

## TC-003 — Add Player Successfully

**Objective**

Verify that a player is added and the purse amount is updated correctly.

| Parameter | Value |
|-----------|-------|
| Team | Chennai Super Kings |
| Player | MS Dhoni |
| Role | Wicketkeeper |
| Price | ₹12 Cr |
| Expected Result | Player added, purse reduced to ₹88 Cr |
| Actual Result | Player added successfully |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/add_player.png
```

---

## TC-004 — Add Player to Non-Existing Team

**Objective**

Verify that players cannot be added to a team that does not exist.

| Parameter | Value |
|-----------|-------|
| Team | Delhi Capitals |
| Expected Result | "No such team." |
| Actual Result | Error displayed |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/no_team.png
```

---

## TC-005 — Purse Limit Validation

**Objective**

Verify that player purchases exceeding the remaining purse are rejected.

| Parameter | Value |
|-----------|-------|
| Remaining Purse | ₹5 Cr |
| Player Price | ₹15 Cr |
| Expected Result | Purchase rejected |
| Actual Result | Error displayed |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/purse_limit.png
```

---

## TC-006 — View Squad

**Objective**

Verify that squad details are displayed correctly.

| Parameter | Value |
|-----------|-------|
| Team | Chennai Super Kings |
| Expected Result | Squad list, total spent, average spending and remaining purse displayed |
| Actual Result | Displayed correctly |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/view_squad.png
```

---

## TC-007 — List All Teams

**Objective**

Verify that all created teams are displayed.

| Parameter | Value |
|-----------|-------|
| Input | List Teams |
| Expected Result | All teams with player count and purse shown |
| Actual Result | Displayed correctly |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/list_teams.png
```

---

## TC-008 — Invalid Price Input

**Objective**

Verify that invalid numeric input is handled correctly.

| Parameter | Value |
|-----------|-------|
| Input | abc |
| Expected Result | Invalid price warning |
| Actual Result | Validation successful |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/invalid_price.png
```

---

## TC-009 — Invalid Menu Option

**Objective**

Verify that invalid menu choices are handled.

| Parameter | Value |
|-----------|-------|
| Input | 8 |
| Expected Result | Invalid choice warning |
| Actual Result | Warning displayed |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/invalid_menu.png
```

---

## TC-010 — Maximum Squad Size

**Objective**

Verify that the application prevents adding more than 25 players.

| Parameter | Value |
|-----------|-------|
| Current Players | 25 |
| Attempt | Add Player 26 |
| Expected Result | Addition rejected |
| Actual Result | Validation successful |
| Status | ✅ Passed |

**Screenshot**

```
docs/Screenshots/max_squad.png
```

---

# Test Coverage

The testing process validated the following functional areas:

- ✅ Team creation
- ✅ Duplicate team validation
- ✅ Player registration
- ✅ Squad management
- ✅ Salary purse tracking
- ✅ Maximum squad size enforcement
- ✅ Input validation
- ✅ Error handling
- ✅ Squad summary generation
- ✅ Menu navigation

---

# Overall Test Result

| Metric | Value |
|--------|------:|
| Total Test Cases | 10 |
| Passed | 10 |
| Failed | 0 |
| Success Rate | **100%** |

---

# Conclusion

The **IPL Squad & Salary Tracker** successfully passed all planned functional test cases. The application correctly enforces IPL auction constraints, validates user inputs, manages team budgets, and generates accurate squad summaries. Testing confirms that the system is stable, reliable, and suitable for demonstrating core Python programming concepts such as functions, dictionaries, lists, loops, conditional statements, and exception handling.

---
