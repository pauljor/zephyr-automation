# Automation Coverage Report

> How many test cases in the Zephyr Google Sheet already have an automated test in `teacher-student-automation` and `admin-staff-automation`.

*Generated 2026-10-09 · Sheet gid 490497427 · 2 automation projects · 781 test cases*

## 1. At a glance

| Automated | Not yet automated | Total | Coverage |
|--:|--:|--:|--:|
| **778** | **3** | **781** | **99.6%** |

`████████████████████████████████████████` 99.6%

```mermaid
pie showData title Test cases
    "Automated" : 778
    "Not automated" : 3
```

### Contribution by project

| Project | Cases matched | Matched only here |
|---|--:|--:|
| teacher-student-automation | 778 | 778 |
| admin-staff-automation | 0 | 0 |

> **admin-staff-automation** is a separate admin/staff-portal suite. It names its tests with its own ids (`EI-TC-###`, `EI-####`, `STAF-...`), not the sheet's Zephyr `EI-T###` keys, so it matches almost nothing. Its tests were not mapped by title, which would be guesswork. See Method & limits.

## 2. Coverage by test type

| Type | Automated | Total | Coverage |  |
|---|--:|--:|--:|---|
| Negative | 297 | 297 | 100% | `████████████████████` |
| Edge | 360 | 363 | 99% | `████████████████████` |
| Positive | 121 | 121 | 100% | `████████████████████` |

```mermaid
xychart-beta
    title "Coverage % by test type"
    x-axis [Negative, Edge, Positive]
    y-axis "%" 0 --> 100
    bar [100, 99, 100]
```

## 3. Coverage by area

| Area | Automated | Total | Coverage |  |
|---|--:|--:|--:|---|
| Auth | 34 | 34 | 100% | `████████████████████` |
| Teacher | 492 | 492 | 100% | `████████████████████` |
| Student | 219 | 220 | 100% | `████████████████████` |
| System | 6 | 8 | 75% | `███████████████░░░░░` |
| Shared | 27 | 27 | 100% | `████████████████████` |

```mermaid
xychart-beta
    title "Coverage % by area"
    x-axis [Auth, Teacher, Student, System, Shared]
    y-axis "%" 0 --> 100
    bar [100, 100, 100, 75, 100]
```

## 4. Where the gaps are

Top 2 test cycles by number of cases still **not automated**.

| # | Cycle | Missing | Automated | Total |  |
|--:|---|--:|--:|--:|---|
| 1 | Edge_System_Webhooks | **2** | 2 | 4 | `████████████████████` |
| 2 | Edge_Student_Accounts | **1** | 22 | 23 | `██████████░░░░░░░░░░` |

These 2 cycles hold **3 of the 3** missing cases (100%).

```mermaid
xychart-beta
    title "Missing automation - top cycles"
    x-axis ["Edge System Webhooks", "Edge Student Accounts"]
    y-axis "cases"
    bar [2, 1]
```

### Cycles with no automation at all

None.

### Fully automated cycles

Negative_Auth_Login, Negative_Auth_Session, Negative_Auth_Profile, Negative_Auth_Password Reset, Negative_Teacher_Account, Negative_Teacher_Dashboard, Negative_Teacher_Classes, Negative_Teacher_Question, Negative_Teacher_Question Import, Negative_Teacher_Assignments, Negative_Teacher_Theme, Negative_Teacher_Features, Negative_Student_Accounts, Negative_Student_Dashboard, Negative_Student_Classes, Negative_Student_Assignments, Negative_Student_Theme, Negative_Student_Features, Edge_System_Health, Edge_Auth_Authentication, Edge_Teacher_Accounts, Edge_Teacher_Dashboard, Edge_Teacher_Classes, Edge_Teacher_Question, Edge_Teacher_Question-Import, Edge_Teacher_Assignments, Edge_Teacher_Theme, Edge_Teacher_Students, Edge_Teacher_Features, Edge_Student_Dashboard, Edge_Student_Classes, Edge_Student_Assignments, Edge_Student_Theme, Edge_Student_Features, Edge_Shared_Assignments, Positive_Auth_Login, Positive_Auth_Session, Positive_Auth_Profile, Positive_Auth_Password Reset, Positive_Teacher_Accounts, Positive_Teacher_Dashboard, Positive_Teacher_Classes, Positive_Teacher_Question, Positive_Teacher_Question Impact, Positive_Teacher_Theme, Positive_Teacher_Features, Positive_Teacher_Assignments, Positive_Student_Accounts, Positive_Student_Dashboard, Positive_Student_Classes, Positive_Student_Assignments, Positive_Student_Theme, Positive_Student_Features

## 5. Coverage by owner

| Owner | Automated | Total | Coverage |  |
|---|--:|--:|--:|---|
| (unassigned) | 1 | 1 | 100% | `████████████████████` |
| Dr. Uzaka | 7 | 7 | 100% | `████████████████████` |
| Jim | 109 | 109 | 100% | `████████████████████` |
| Khyne | 101 | 101 | 100% | `████████████████████` |
| Paul | 260 | 260 | 100% | `████████████████████` |
| Trishia | 36 | 36 | 100% | `████████████████████` |
| Gelo | 160 | 161 | 99% | `████████████████████` |
| Allan | 104 | 106 | 98% | `████████████████████` |

## 6. All test cycles

Sorted from lowest to highest coverage.

| Cycle | Automated | Total | Coverage |  |
|---|--:|--:|--:|---|
| Edge_System_Webhooks | 2 | 4 | 50% | `██████████░░░░░░░░░░` |
| Edge_Student_Accounts | 22 | 23 | 96% | `███████████████████░` |
| Negative_Teacher_Assignments | 75 | 75 | 100% | `████████████████████` |
| Negative_Teacher_Classes | 57 | 57 | 100% | `████████████████████` |
| Edge_Teacher_Assignments | 54 | 54 | 100% | `████████████████████` |
| Edge_Teacher_Classes | 54 | 54 | 100% | `████████████████████` |
| Negative_Student_Assignments | 32 | 32 | 100% | `████████████████████` |
| Edge_Shared_Assignments | 27 | 27 | 100% | `████████████████████` |
| Edge_Teacher_Question | 25 | 25 | 100% | `████████████████████` |
| Positive_Teacher_Assignments | 25 | 25 | 100% | `████████████████████` |
| Edge_Student_Assignments | 22 | 22 | 100% | `████████████████████` |
| Edge_Teacher_Accounts | 21 | 21 | 100% | `████████████████████` |
| Edge_Auth_Authentication | 20 | 20 | 100% | `████████████████████` |
| Negative_Teacher_Question | 20 | 20 | 100% | `████████████████████` |
| Negative_Teacher_Question Import | 18 | 18 | 100% | `████████████████████` |
| Positive_Teacher_Classes | 18 | 18 | 100% | `████████████████████` |
| Edge_Teacher_Question-Import | 16 | 16 | 100% | `████████████████████` |
| Negative_Student_Classes | 16 | 16 | 100% | `████████████████████` |
| Edge_Student_Classes | 15 | 15 | 100% | `████████████████████` |
| Negative_Student_Accounts | 15 | 15 | 100% | `████████████████████` |
| Negative_Teacher_Account | 15 | 15 | 100% | `████████████████████` |
| Edge_Student_Dashboard | 14 | 14 | 100% | `████████████████████` |
| Edge_Student_Theme | 13 | 13 | 100% | `████████████████████` |
| Edge_Teacher_Theme | 13 | 13 | 100% | `████████████████████` |
| Edge_Teacher_Features | 12 | 12 | 100% | `████████████████████` |
| Edge_Student_Features | 10 | 10 | 100% | `████████████████████` |
| Positive_Student_Assignments | 10 | 10 | 100% | `████████████████████` |
| Positive_Teacher_Question | 9 | 9 | 100% | `████████████████████` |
| Edge_Teacher_Dashboard | 8 | 8 | 100% | `████████████████████` |
| Edge_Teacher_Students | 8 | 8 | 100% | `████████████████████` |
| Negative_Teacher_Features | 8 | 8 | 100% | `████████████████████` |
| Negative_Student_Dashboard | 7 | 7 | 100% | `████████████████████` |
| Negative_Student_Features | 7 | 7 | 100% | `████████████████████` |
| Negative_Student_Theme | 7 | 7 | 100% | `████████████████████` |
| Negative_Teacher_Theme | 7 | 7 | 100% | `████████████████████` |
| Positive_Student_Accounts | 7 | 7 | 100% | `████████████████████` |
| Positive_Student_Dashboard | 7 | 7 | 100% | `████████████████████` |
| Positive_Student_Classes | 6 | 6 | 100% | `████████████████████` |
| Positive_Teacher_Accounts | 6 | 6 | 100% | `████████████████████` |
| Positive_Teacher_Features | 6 | 6 | 100% | `████████████████████` |
| Positive_Student_Features | 5 | 5 | 100% | `████████████████████` |
| Positive_Teacher_Question Impact | 5 | 5 | 100% | `████████████████████` |
| Edge_System_Health | 4 | 4 | 100% | `████████████████████` |
| Negative_Teacher_Dashboard | 4 | 4 | 100% | `████████████████████` |
| Positive_Student_Theme | 4 | 4 | 100% | `████████████████████` |
| Positive_Teacher_Dashboard | 4 | 4 | 100% | `████████████████████` |
| Positive_Teacher_Theme | 4 | 4 | 100% | `████████████████████` |
| Negative_Auth_Login | 3 | 3 | 100% | `████████████████████` |
| Negative_Auth_Password Reset | 3 | 3 | 100% | `████████████████████` |
| Negative_Auth_Session | 2 | 2 | 100% | `████████████████████` |
| Positive_Auth_Session | 2 | 2 | 100% | `████████████████████` |
| Negative_Auth_Profile | 1 | 1 | 100% | `████████████████████` |
| Positive_Auth_Login | 1 | 1 | 100% | `████████████████████` |
| Positive_Auth_Password Reset | 1 | 1 | 100% | `████████████████████` |
| Positive_Auth_Profile | 1 | 1 | 100% | `████████████████████` |

## 7. Automation layers and latest results

From `automation_logs.txt` (one line per case and layer; the last line for a case and layer wins). A case can have an API test, a UI test, or both.

| Layer | Passed | Failed | API-only | Deferred | Existing test |
|---|--:|--:|--:|--:|--:|
| API (service suite) | 304 | 7 | 0 | 0 | 5 |
| UI (client suite, Positive cases) | 76 | 0 | 19 | 0 | 0 |
| Not automated (deferred) | 0 | 0 | 0 | 3 | 0 |

### Automated cases that currently fail (7)

Each fails because the application does not do what the Zephyr case expects. They stay red on purpose; no ticket has been raised.

- EI-T117 (api) - defect:400-review-of-a-valid-submitted-submission-answers-field-required
- EI-T130 (api) - defect:200-over-length-email-accepted
- EI-T262 (api) - defect:200-passing_grade-outside-0-100-accepted-on-update
- EI-T265 (api) - defect:200-boolean-points-accepted-as-1
- EI-T298 (api) - defect:200-empty-or-blank-reject-reason-accepted
- EI-T374 (api) - defect:200-empty-violation-type-accepted
- EI-T415 (api) - defect:200-passing_grade-outside-0-100-accepted-on-shared-update

### Deferred (3)

- EI-T672 - the student API has no account-removal route (staff-admin only); nothing to call from this suite
- EI-T778 - needs real AUTH0_WEBHOOK_SECRET to pass authentication; not in .env
- EI-T779 - needs real AUTH0_WEBHOOK_SECRET to pass authentication; not in .env

<details><summary><b>Positive cases with no screen - API-only (19)</b></summary>

- EI-T19 - no screen: the SPA never calls the class messages routes (no announcements UI)
- EI-T20 - no screen: the SPA never calls the class messages routes (no announcements UI)
- EI-T21 - no screen: the SPA never calls the class messages routes (no announcements UI)
- EI-T29 - no screen: there is no restore control for a soft-deleted class
- EI-T35 - no screen: the question bank lists only the teacher's own questions; the staff catalogue is fetched only by the item-bank picker in the new-assignment wizard
- EI-T52 - no screen: effective feature flags only lock or open other screens; no page lists them
- EI-T53 - no screen: a single district feature status only locks or opens other screens; no page lists it
- EI-T78 - no screen: the SPA has no contact-person form
- EI-T94 - no screen: the SPA never calls the cancel-join route
- EI-T95 - no screen: the SPA never calls the class messages routes (no announcements UI)
- EI-T108 - no screen: effective feature flags only lock or open other screens; no page lists them
- EI-T109 - no screen: a single district feature status only locks or opens other screens; no page lists it
- EI-T113 - no screen: shared assignments service (create)
- EI-T114 - no screen: shared assignments service (view by id)
- EI-T117 - no screen: shared assignments service (submission review by submission id); the API test also fails on a real defect
- EI-T118 - no screen: shared assignments service (share with another user); the SPA share control is commented out
- EI-T119 - no screen: shared assignments service (show_analytics); the SPA uses the teacher analytics routes
- EI-T120 - no screen: shared assignments service (update)
- EI-T121 - no screen: shared assignments service (delete)

</details>

## 8. Detail lists

Click to expand.

<details><summary><b>Not automated (3)</b> - grouped by cycle</summary>

**Edge_System_Webhooks** (2)

- EI-T778 - [Webhooks] Malformed Auth0 event payload is rejected without partial profile writes
- EI-T779 - [Webhooks] Replayed Auth0 user-sync event is processed idempotently

**Edge_Student_Accounts** (1)

- EI-T672 - [Accounts] Removing an account with dependent records leaves no orphaned data

</details>

<details><summary><b>Automated (778)</b> - test case to file</summary>

| Test case | Name | File(s) |
|---|---|---|
| EI-T124 | Authenticating with credentials with an empty or over-length email value is rejected | `teacher-student-automation/service/tests/account/test_EI_R2_negative_auth_login.py` |
| EI-T123 | Authenticating with credentials with password supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/account/test_EI_R2_negative_auth_login.py` |
| EI-T122 | Authenticating with credentials without the required email field is rejected | `teacher-student-automation/service/tests/account/test_EI_R2_negative_auth_login.py` |
| EI-T126 | Logging out with malformed request parameters returns no server error | `teacher-student-automation/service/tests/account/test_EI_R3_negative_auth_session.py` |
| EI-T125 | Rotating the session with malformed request parameters returns no server error | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T127 | Fetching the current user profile with malformed request parameters returns no server error | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_profile_malformed_params.py` |
| EI-T130 | Requesting a password reset with an empty or over-length email value is rejected | `teacher-student-automation/service/tests/password/test_EI_R5_negative_auth_password_reset.py` |
| EI-T129 | Requesting a password reset with email supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/password/test_EI_R5_negative_auth_password_reset.py` |
| EI-T128 | Requesting a password reset without the required email field is rejected | `teacher-student-automation/service/tests/password/test_EI_R5_negative_auth_password_reset.py` |
| EI-T134 | Adding a teacher profile picture with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T133 | Adding a teacher profile picture with an unsupported file type is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T132 | Adding a teacher profile picture with no file attached is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T145 | Changing a teacher password with an empty or over-length new_password value is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T144 | Changing a teacher password with new_password supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T143 | Changing a teacher password without the required current_password field is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T138 | Deleting a teacher profile picture with a malformed teacherId value is rejected | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T131 | Searching for users with a malformed search value is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T137 | Updating a teacher profile picture with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T136 | Updating a teacher profile picture with an unsupported file type is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T135 | Updating a teacher profile picture with no file attached is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T142 | Updating teacher account information with a malformed teacher identifier is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T141 | Updating teacher account information with an empty payload and with an oversized payload is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T140 | Updating teacher account information with the email supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T139 | Updating teacher account information without the required first_name is rejected | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py` |
| EI-T148 | Fetching assignment statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R7_negative_teacher_dashboard.py` |
| EI-T146 | Fetching class statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R7_negative_teacher_dashboard.py` |
| EI-T147 | Fetching student statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R7_negative_teacher_dashboard.py` |
| EI-T149 | Fetching submission statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R7_negative_teacher_dashboard.py` |
| EI-T194 | Accepting a student join request with a malformed student identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T196 | Accepting a student join request with an excessively long or unknown student identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T195 | Accepting a student join request with the student identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T183 | Adding a class cover photo with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T182 | Adding a class cover photo with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T181 | Adding a class cover photo with an unsupported file type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T180 | Adding a class cover photo with no file attached is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py`<br>`teacher-student-automation/service/tests/classes/test_EI_T500_missing_file_upload_cover_photo.py` |
| EI-T203 | Approving a student leave request with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T202 | Approving a student leave request with a non-boolean is_granted value is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T201 | Approving a student leave request with is_granted supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T200 | Approving a student leave request without the required is_granted field is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py`<br>`teacher-student-automation/service/tests/classes/test_EI_T520_missing_is_granted_accept_leave_request.py` |
| EI-T152 | Creating a class with an unsupported semester value is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T151 | Creating a class with schedules supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T150 | Creating a class without the required title field is rejected | `teacher-student-automation/service/tests/classes/test_EI_656_teacher_create_class_description_optional.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes.py` |
| EI-T164 | Deleting a class announcement with a malformed message identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T166 | Deleting a class announcement with an excessively long or unknown message identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T165 | Deleting a class announcement with the message identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T188 | Deleting a class cover photo with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T190 | Deleting a class cover photo with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T189 | Deleting a class cover photo with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T177 | Deleting a class with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T179 | Deleting a class with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T178 | Deleting a class with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T154 | Fetching a class by code with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T156 | Fetching a class by code with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T155 | Fetching a class by code with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T167 | Fetching a class gradebook with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T169 | Fetching a class gradebook with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T168 | Fetching a class gradebook with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T170 | Fetching a class roster with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T172 | Fetching a class roster with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_delete_fetch.py` |
| EI-T171 | Fetching a class roster with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T153 | Fetching all classes with non-numeric and out-of-range pagination values is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T157 | Fetching class announcements with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T159 | Fetching class announcements with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T158 | Fetching class announcements with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T204 | Fetching class assignments with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T206 | Fetching class assignments with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T205 | Fetching class assignments with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T163 | Posting a class announcement with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T162 | Posting a class announcement with an empty or over-length content value is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T161 | Posting a class announcement with content supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T160 | Posting a class announcement without the required content field is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T197 | EI-T197 | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T199 | Removing a student from a class with an excessively long or unknown student identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T198 | Removing a student from a class with the student identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T191 | Restoring a soft-deleted class with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T193 | Restoring a soft-deleted class with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T192 | Restoring a soft-deleted class with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T187 | Updating a class cover photo with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T186 | Updating a class cover photo with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T185 | Updating a class cover photo with an unsupported file type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T184 | Updating a class cover photo with no file attached is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T176 | Updating class details with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T175 | Updating class details with an unsupported semester value is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T174 | Updating class details with section supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T173 | Updating class details without the required title field is rejected | `teacher-student-automation/service/tests/classes/test_EI_R8_negative_teacher_classes_part3.py` |
| EI-T223 | Clearing question filters with malformed request parameters returns no server error | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T211 | Creating a question with an empty payload and with an oversized payload is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T210 | Creating a question with the answer options supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T209 | Creating a question without the required question stem is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T219 | Deleting a question with a malformed question identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T221 | Deleting a question with an excessively long or unknown question identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T220 | Deleting a question with the question identifier omitted is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T212 | Fetching a question by identifier with a malformed question identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T214 | Fetching a question by identifier with an excessively long or unknown question identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T213 | Fetching a question by identifier with the question identifier omitted is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T207 | Fetching all questions with malformed filter values is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T222 | Fetching question filter options with malformed request parameters returns no server error | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T208 | Fetching staff questions with malformed filter values is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T218 | Updating a question with a malformed question identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T217 | Updating a question with an empty payload and with an oversized payload is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T216 | Updating a question with the answer options supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T215 | Updating a question without the required question stem is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T226 | Uploading a question image with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T225 | Uploading a question image with an unsupported file type is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T224 | Uploading a question image with no file attached is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py` |
| EI-T244 | Committing a question import with a malformed import job identifier is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T243 | Committing a question import with an empty payload and with an oversized payload is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T242 | Committing a question import with the question stem supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T241 | Committing a question import without the required question payload list is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T238 | Fetching proposed import questions with a malformed import job identifier is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T240 | Fetching proposed import questions with an excessively long or unknown import job identifier is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T239 | Fetching proposed import questions with the import job identifier omitted is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T234 | Importing a pasted question with an empty or over-length text value is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T233 | Importing a pasted question with question_type supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T232 | Importing a pasted question without the required text field is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T235 | Polling an import job status with a malformed import job identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T237 | Polling an import job status with an excessively long or unknown import job identifier is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T236 | Polling an import job status with the import job identifier omitted is rejected | `teacher-student-automation/service/tests/question/test_zephyr_negative_question_bank.py` |
| EI-T229 | Uploading a question import file with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T231 | Uploading a question import file with an unrecognised question_type value is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T228 | Uploading a question import file with an unsupported file type is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T227 | Uploading a question import file with no file attached is rejected | `teacher-student-automation/service/tests/account/test_zephyr_negative_password_image_session.py`<br>`teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T230 | Uploading a question import file with question_type omitted is rejected | `teacher-student-automation/service/tests/question-import/test_zephyr_negative_question_import.py` |
| EI-T283 | Adding a comment on a student answer with a malformed question identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T282 | Adding a comment on a student answer with an empty or over-length comment value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T281 | Adding a comment on a student answer with comment supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T280 | Adding a comment on a student answer without the required comment field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T296 | Approving a late submission with a malformed submission identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_late_submission_approve.py` |
| EI-T295 | Approving a late submission with late_penalty outside its accepted range is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_late_submission_approve.py` |
| EI-T294 | Approving a late submission with late_penalty supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_late_submission_approve.py` |
| EI-T253 | Creating a staff assignment with an unsupported type value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T252 | Creating a staff assignment with questions supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T251 | Creating a staff assignment without the required description field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T395 | Creating an assignment through the shared service with an unsupported type value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T394 | Creating an assignment through the shared service with questions supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T393 | Creating an assignment through the shared service without the required questions field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T247 | Creating an assignment with an unsupported type value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T246 | Creating an assignment with questions supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T245 | Creating an assignment without the required title field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T288 | Deleting a comment on a student answer with a malformed question identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments.py` |
| EI-T290 | Deleting a comment on a student answer with an excessively long or unknown question identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments.py` |
| EI-T289 | Deleting a comment on a student answer with the question identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments.py` |
| EI-T418 | Deleting an assignment through the shared service with a malformed assignment_uuid value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T417 | Deleting an assignment through the shared service without the required assignment_uuid parameter is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T268 | Deleting an assignment with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T270 | Deleting an assignment with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T269 | Deleting an assignment with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T255 | Fetching a staff assignment with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T257 | Fetching a staff assignment with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T256 | Fetching a staff assignment with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T277 | Fetching a student submission with a malformed student identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T279 | Fetching a student submission with an excessively long or unknown student identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T278 | Fetching a student submission with the student identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T258 | Fetching a teacher assignment with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T260 | Fetching a teacher assignment with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T259 | Fetching a teacher assignment with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T254 | Fetching all staff assignments with malformed request parameters returns no server error | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T271 | Fetching assignment analytics summary with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T273 | Fetching assignment analytics summary with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T272 | Fetching assignment analytics summary with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T274 | Fetching assignment item analysis with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T276 | Fetching assignment item analysis with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T275 | Fetching assignment item analysis with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T248 | Fetching class assignments for a teacher with a malformed class code is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T250 | Fetching class assignments for a teacher with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T249 | Fetching class assignments for a teacher with the class code omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T411 | Fetching shared assignment analytics with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T413 | Fetching shared assignment analytics with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T412 | Fetching shared assignment analytics with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T291 | Listing pending late submissions with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T293 | Listing pending late submissions with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T292 | Listing pending late submissions with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T267 | Overriding a question point value with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T266 | Overriding a question point value with points outside its accepted range is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T265 | Overriding a question point value with points supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T264 | Overriding a question point value without the required points field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T299 | Rejecting a late submission with a malformed submission identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T298 | Rejecting a late submission with an empty or over-length reason value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T297 | Rejecting a late submission with reason supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T405 | Retrieving a submission for review with a malformed submission identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T407 | Retrieving a submission for review with an excessively long or unknown submission identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T406 | Retrieving a submission for review with the submission identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T396 | Retrieving an assignment through the shared service with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T398 | Retrieving an assignment through the shared service with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T397 | Retrieving an assignment through the shared service with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T410 | Sharing an assignment with an empty or over-length description value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T409 | Sharing an assignment with object_id supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T408 | Sharing an assignment without the required recipient_id field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T287 | Updating a comment on a student answer with a malformed question identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T286 | Updating a comment on a student answer with an empty or over-length comment value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T285 | Updating a comment on a student answer with comment supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T284 | Updating a comment on a student answer without the required comment field is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T416 | Updating an assignment through the shared service with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T415 | Updating an assignment through the shared service with passing_grade outside its accepted range is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T414 | Updating an assignment through the shared service with questions supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T263 | Updating an assignment with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_identifier.py` |
| EI-T262 | Updating an assignment with passing_grade outside its accepted range is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T261 | Updating an assignment with questions supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R11_negative_teacher_assignments_payload.py` |
| EI-T303 | Applying a teacher theme with an empty or over-length theme_id value is rejected | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T302 | Applying a teacher theme with color_mode supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T301 | Applying a teacher theme without the required theme_id field is rejected | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T306 | Deleting a teacher theme with malformed request parameters returns no server error | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T300 | Fetching a teacher theme with malformed request parameters returns no server error | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T305 | Updating teacher theme settings with an empty or over-length theme_name value is rejected | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T304 | Updating teacher theme settings with colors supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/theme/test_EI_R12_negative_teacher_theme.py` |
| EI-T308 | Fetching a single feature status for a teacher with a malformed feature name is rejected | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T310 | Fetching a single feature status for a teacher with an excessively long or unknown feature name is rejected | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T309 | Fetching a single feature status for a teacher with the feature name omitted is rejected | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T314 | Fetching a teacher assignment quota with a malformed class_code value is rejected | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T313 | Fetching a teacher district plan with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T307 | Fetching teacher feature flags with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T311 | Fetching teacher organisation details with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T312 | Fetching teacher school details with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_EI_R13_negative_teacher_features.py` |
| EI-T322 | Adding a student profile picture with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/account/test_EI_T322_empty_and_oversized_file_add_profile_picture.py` |
| EI-T321 | Adding a student profile picture with an unsupported file type is rejected | `teacher-student-automation/service/tests/account/test_EI_T321_unsupported_file_type_add_profile_picture.py` |
| EI-T320 | Adding a student profile picture with no file attached is rejected | `teacher-student-automation/service/tests/account/test_EI_T320_missing_file_add_profile_picture.py`<br>`teacher-student-automation/service/utils/image_factory.py` |
| EI-T329 | Changing a student password with an empty or over-length new_password value is rejected | `teacher-student-automation/service/tests/account/test_EI_T329_empty_and_overlength_new_password_update_password.py`<br>`teacher-student-automation/service/utils/data_factory.py`<br>`teacher-student-automation/service/utils/student_password.py` |
| EI-T328 | Changing a student password with new_password supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/account/test_EI_T328_wrong_type_new_password_update_password.py`<br>`teacher-student-automation/service/utils/data_factory.py` |
| EI-T327 | Changing a student password without the required current_password field is rejected | `teacher-student-automation/service/tests/account/test_EI_T327_missing_current_password_update_password.py`<br>`teacher-student-automation/service/utils/data_factory.py`<br>`teacher-student-automation/service/utils/student_password.py` |
| EI-T326 | Deleting a student profile picture with malformed request parameters returns no server error | `teacher-student-automation/service/tests/account/test_EI_T326_malformed_params_delete_profile_picture.py` |
| EI-T315 | Fetching a student account with a malformed id value is rejected | `teacher-student-automation/service/tests/account/test_EI_T315_malformed_id_fetch_account.py`<br>`teacher-student-automation/service/utils/data_factory.py` |
| EI-T316 | Searching for teachers with non-numeric and out-of-range pagination values is rejected | `teacher-student-automation/service/tests/account/test_EI_T316_pagination_bounds_teacher_search.py` |
| EI-T325 | Updating a student profile picture with an empty file and with an oversized file is rejected | `teacher-student-automation/service/tests/account/test_EI_T325_empty_and_oversized_file_update_profile_picture.py`<br>`teacher-student-automation/service/utils/image_factory.py` |
| EI-T324 | Updating a student profile picture with an unsupported file type is rejected | `teacher-student-automation/service/tests/account/test_EI_T324_unsupported_file_type_update_profile_picture.py` |
| EI-T323 | Updating a student profile picture with no file attached is rejected | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py` |
| EI-T319 | Updating student contact person details with an empty or over-length first_name value is rejected | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py` |
| EI-T318 | Updating student contact person details with phone_number supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py` |
| EI-T317 | Updating student contact person details without the required relationship field is rejected | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py` |
| EI-T331 | Fetching a grade distribution with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T332 | Fetching a student GPA with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T330 | Fetching achievement badges with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T335 | Fetching student assignment statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T334 | Fetching student class statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T336 | Fetching student submission statistics with malformed request parameters returns no server error | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T333 | Fetching upcoming assignments with an out-of-range limit value is rejected | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T347 | Cancelling a pending join request with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T349 | Cancelling a pending join request with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T348 | Cancelling a pending join request with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T338 | Fetching an enrolled class by code with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T340 | Fetching an enrolled class by code with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T339 | Fetching an enrolled class by code with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T350 | Fetching class announcements as a student with a malformed class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T352 | Fetching class announcements as a student with an excessively long or unknown class identifier is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T351 | Fetching class announcements as a student with the class identifier omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T337 | Fetching enrolled classes with non-numeric and out-of-range pagination values is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py`<br>`teacher-student-automation/service/tests/classes/test_zephyr_edge_student_classes_pagination.py` |
| EI-T341 | Joining a class with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T343 | Joining a class with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T342 | Joining a class with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T344 | Requesting to leave a class with a malformed class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T346 | Requesting to leave a class with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T345 | Requesting to leave a class with the class code omitted is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T356 | Fetching a class average grade with a malformed class code is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T358 | Fetching a class average grade with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/classes/test_EI_R16_negative_student_classes.py` |
| EI-T357 | Fetching a class average grade with the class code omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T376 | Fetching a student submission for review with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T378 | Fetching a student submission for review with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T377 | Fetching a student submission for review with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T359 | Fetching an assignment as a student with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T361 | Fetching an assignment as a student with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T360 | Fetching an assignment as a student with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T362 | Fetching assignment questions with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T364 | Fetching assignment questions with an excessively long or unknown assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T363 | Fetching assignment questions with the assignment identifier omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T353 | Fetching class assignments as a student with a malformed class code is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T355 | Fetching class assignments as a student with an excessively long or unknown class code is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T354 | Fetching class assignments as a student with the class code omitted is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T375 | Reporting a lockdown violation with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T374 | Reporting a lockdown violation with an empty or over-length type value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T373 | Reporting a lockdown violation with type supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T401 | Requesting the next adaptive item with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T400 | Requesting the next adaptive item with a malformed question_classification value is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T399 | Requesting the next adaptive item without the required prev_difficulty parameter is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T368 | Saving assignment answers with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T367 | Saving assignment answers with an empty answers array is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T366 | Saving assignment answers with answers supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T365 | Saving assignment answers without the required answers field is rejected | `teacher-student-automation/service/tests/assignment/test_take_assignment_student_flow.py` |
| EI-T404 | Submitting an answer through the shared service with an empty answers array is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T403 | Submitting an answer through the shared service with answers supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T402 | Submitting an answer through the shared service without the required assignment_id field is rejected | `teacher-student-automation/service/tests/assignment/test_shared_answer_service_records_submission.py` |
| EI-T372 | Submitting assignment answers with a malformed assignment identifier is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T371 | Submitting assignment answers with an empty answers array is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T370 | Submitting assignment answers with answers supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/assignment/test_EI_R17_negative_student_assignments.py` |
| EI-T369 | Submitting assignment answers without the required answers field is rejected | `teacher-student-automation/service/tests/assignment/test_take_assignment_submit_flow.py` |
| EI-T382 | Applying a student theme with an empty or over-length theme_id value is rejected | `teacher-student-automation/service/tests/theme/test_student_theme_lifecycle.py` |
| EI-T381 | Applying a student theme with color_mode supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/theme/test_student_theme_lifecycle.py` |
| EI-T380 | Applying a student theme without the required theme_id field is rejected | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T385 | Deleting a student theme with malformed request parameters returns no server error | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T379 | Fetching a student theme with malformed request parameters returns no server error | `teacher-student-automation/service/tests/theme/test_student_theme_lifecycle.py` |
| EI-T384 | Updating student theme settings with an empty or over-length theme_name value is rejected | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T383 | Updating student theme settings with colors supplied as the wrong data type is rejected | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T387 | Fetching a single feature status for a student with a malformed feature name is rejected | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T389 | Fetching a single feature status for a student with an excessively long or unknown feature name is rejected | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T388 | Fetching a single feature status for a student with the feature name omitted is rejected | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T392 | Fetching a student district plan with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T386 | Fetching student feature flags with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_student_features.py` |
| EI-T390 | Fetching student organisation details with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_student_features.py` |
| EI-T391 | Fetching student school details with malformed request parameters returns no server error | `teacher-student-automation/service/tests/features/test_student_features.py` |
| EI-T419 | [Health] Health probe reflects a downstream dependency outage | `teacher-student-automation/service/tests/health/test_zephyr_edge_health_readiness.py` |
| EI-T421 | [Health] Health probe reflects a downstream dependency outage (2) | `teacher-student-automation/service/tests/health/test_zephyr_edge_health_readiness.py` |
| EI-T420 | [Health] Health probe responds without credentials and discloses no environment detail | `teacher-student-automation/service/tests/health/test_zephyr_edge_health_disclosure.py` |
| EI-T422 | [Health] Health probe responds without credentials and discloses no environment detail (2) | `teacher-student-automation/service/tests/health/test_zephyr_edge_health_disclosure.py` |
| EI-T781 | [Webhooks] Auth0 user-sync event with an incorrect shared secret is rejected | `teacher-student-automation/service/tests/security/test_EI_R21_edge_system_webhooks.py` |
| EI-T780 | [Webhooks] Auth0 user-sync event without a shared secret header is rejected | `teacher-student-automation/service/tests/security/test_EI_R21_edge_system_webhooks.py` |
| EI-T434 | [Authentication] Cleared session cookies carry the correct security attributes | `teacher-student-automation/service/tests/account/test_zephyr_edge_cookies_and_uploads.py` |
| EI-T436 | [Authentication] Empty result set is returned correctly when attempting to get current user profile | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_me_envelope.py` |
| EI-T435 | [Authentication] Expired bearer token is rejected when attempting to get current user profile | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T427 | [Authentication] Expired or tampered refresh token is rejected during rotation | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T431 | [Authentication] Expired or tampered refresh token is rejected during rotation (2) | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T438 | [Authentication] High-volume result set stays complete and performant when attempting to get current user profile | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_me_envelope.py` |
| EI-T437 | [Authentication] Missing Authorization header is rejected when attempting to get current user profile | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T423 | [Authentication] Omitting the required field 'email' is rejected when attempting to login with email and password | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T439 | [Authentication] Omitting the required field 'email' is rejected when attempting to request a password reset email | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T426 | [Authentication] Oversized 'email' value is handled safely when attempting to login with email and password | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py` |
| EI-T442 | [Authentication] Oversized 'email' value is handled safely when attempting to request a password reset email | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py` |
| EI-T440 | [Authentication] Password reset request for an unknown email does not enumerate accounts | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T424 | [Authentication] Repeated failed sign-in attempts are throttled without account enumeration | `teacher-student-automation/service/tests/account/test_zephyr_edge_login_throttle.py` |
| EI-T428 | [Authentication] Reusing an already rotated refresh token is rejected | `teacher-student-automation/service/tests/account/test_zephyr_edge_refresh_rotation.py` |
| EI-T432 | [Authentication] Reusing an already rotated refresh token is rejected (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_refresh_rotation.py` |
| EI-T425 | [Authentication] Script payload in 'email' is neutralised when attempting to login with email and password | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T441 | [Authentication] Script payload in 'email' is neutralised when attempting to request a password reset email | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T429 | [Authentication] Session rotation without a refresh-token cookie is rejected | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T433 | [Authentication] Session rotation without a refresh-token cookie is rejected (2) | `teacher-student-automation/service/tests/account/test_EI_R22_edge_auth_authentication.py` |
| EI-T430 | [Authentication] Simultaneous rotation requests issue only one valid session | `teacher-student-automation/service/tests/account/test_zephyr_edge_refresh_race.py` |
| EI-T461 | [Accounts] Duplicate submission does not create a duplicate account | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T459 | [Accounts] Empty update payload is handled correctly when attempting to update my account information | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_identifiers.py`<br>`teacher-student-automation/service/tests/features/test_zephyr_edge_student_feature_identifiers.py` |
| EI-T447 | [Accounts] Expired bearer token is rejected when attempting to add a profile picture if I don't have one already | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T462 | [Accounts] Expired bearer token is rejected when attempting to change my password by providing my current password | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T455 | [Accounts] Expired bearer token is rejected when attempting to delete my profile picture | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T444 | [Accounts] Expired bearer token is rejected when attempting to search for users by name/email and role, or return current user account | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T458 | [Accounts] Expired bearer token is rejected when attempting to update my account information | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T451 | [Accounts] Expired bearer token is rejected when attempting to update my profile picture | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T446 | [Accounts] Interrupted upload leaves no orphaned asset when attempting to add a profile picture if I don't have one already | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T450 | [Accounts] Interrupted upload leaves no orphaned asset when attempting to update my profile picture | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T456 | [Accounts] Malformed teacher identifier is rejected when attempting to update my account information | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T453 | [Accounts] Malformed teacherId identifier is rejected when attempting to delete my profile picture | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T460 | [Accounts] Omitting the required field 'current_password' is rejected when attempting to change my password by providing my current password | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T445 | [Accounts] Omitting the required field 'file' is rejected when attempting to add a profile picture if I don't have one already | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T449 | [Accounts] Omitting the required field 'file' is rejected when attempting to update my profile picture | `teacher-student-automation/service/tests/account/test_EI_R6_negative_teacher_accounts.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T463 | [Accounts] Script payload in 'current_password' is neutralised when attempting to change my password by providing my current password | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T448 | [Accounts] Script payload in 'file' is neutralised when attempting to add a profile picture if I don't have one already | `teacher-student-automation/service/tests/account/test_zephyr_edge_cookies_and_uploads.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T452 | [Accounts] Script payload in 'file' is neutralised when attempting to update my profile picture | `teacher-student-automation/service/tests/account/test_zephyr_edge_cookies_and_uploads.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T443 | [Accounts] Unknown 'search' filter value returns no matches when attempting to search for users by name/email and role, or return current user account | `teacher-student-automation/service/tests/account/test_EI_R23_edge_teacher_accounts.py` |
| EI-T457 | [Accounts] Unknown teacher identifier returns not found when attempting to update my account information | `teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_identifiers.py`<br>`teacher-student-automation/service/tests/features/test_zephyr_edge_student_feature_identifiers.py` |
| EI-T454 | [Accounts] Unknown teacherId identifier returns not found when attempting to delete my profile picture | `teacher-student-automation/service/services/teacher/account_service.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_auth_account_coverage.py` |
| EI-T469 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for assignments | `teacher-student-automation/service/tests/dashboard/test_EI_edge_teacher_dashboard.py` |
| EI-T465 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for classes | `teacher-student-automation/service/tests/dashboard/test_EI_R24_edge_teacher_dashboard_empty.py` |
| EI-T467 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for students | `teacher-student-automation/service/tests/dashboard/test_EI_R24_edge_teacher_dashboard_empty.py` |
| EI-T471 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for submissions | `teacher-student-automation/service/tests/dashboard/test_EI_R24_edge_teacher_dashboard_empty.py` |
| EI-T468 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for assignments | `teacher-student-automation/service/tests/dashboard/test_EI_edge_teacher_dashboard.py` |
| EI-T464 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for classes | `teacher-student-automation/service/tests/dashboard/test_EI_edge_teacher_dashboard.py` |
| EI-T466 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for students | `teacher-student-automation/service/tests/dashboard/test_EI_edge_teacher_dashboard.py` |
| EI-T470 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for submissions | `teacher-student-automation/service/tests/dashboard/test_EI_edge_teacher_dashboard.py` |
| EI-T473 | [Classes] Duplicate submission does not create a duplicate classe | `teacher-student-automation/service/tests/classes/test_EI_T473_duplicate_class_submission.py` |
| EI-T516 | [Classes] Expired bearer token is rejected when attempting to accept a student's request to join a class | `teacher-student-automation/service/tests/classes/test_EI_T516_expired_token_accept_join_request.py` |
| EI-T522 | [Classes] Expired bearer token is rejected when attempting to accept a student's request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_T522_expired_token_accept_leave_request.py` |
| EI-T484 | [Classes] Expired bearer token is rejected when attempting to create a class announcement | `teacher-student-automation/service/tests/classes/test_EI_T484_expired_token_create_announcement.py` |
| EI-T474 | [Classes] Expired bearer token is rejected when attempting to create a new class | `teacher-student-automation/service/tests/classes/test_EI_T474_expired_token_create_class.py` |
| EI-T499 | [Classes] Expired bearer token is rejected when attempting to delete a class | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T488 | [Classes] Expired bearer token is rejected when attempting to delete a class announcement | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T510 | [Classes] Expired bearer token is rejected when attempting to delete a class cover photo | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T477 | [Classes] Expired bearer token is rejected when attempting to fetch all classes | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T519 | [Classes] Expired bearer token is rejected when attempting to remove a student from a class | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T513 | [Classes] Expired bearer token is rejected when attempting to restore a soft-deleted class | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T506 | [Classes] Expired bearer token is rejected when attempting to update a class cover photo | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T495 | [Classes] Expired bearer token is rejected when attempting to update a class details | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T502 | [Classes] Expired bearer token is rejected when attempting to upload a class cover photo | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T505 | [Classes] Interrupted upload leaves no orphaned asset when attempting to update a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_T501_interrupted_cover_photo_upload.py`<br>`teacher-student-automation/service/tests/classes/test_EI_T505_interrupted_cover_photo_update.py` |
| EI-T501 | [Classes] Interrupted upload leaves no orphaned asset when attempting to upload a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_T501_interrupted_cover_photo_upload.py` |
| EI-T478 | [Classes] Malformed class code identifier is rejected when attempting to fetch a class by its code | `teacher-student-automation/service/tests/classes/test_EI_T478_malformed_class_code_find.py`<br>`teacher-student-automation/service/tests/classes/test_EI_T489_malformed_class_code_gradebook.py` |
| EI-T489 | [Classes] Malformed class code identifier is rejected when attempting to fetch the gradebook for a specific class | `teacher-student-automation/service/tests/classes/test_EI_T489_malformed_class_code_gradebook.py` |
| EI-T514 | [Classes] Malformed class identifier is rejected when attempting to accept a student's request to join a class | `teacher-student-automation/service/tests/classes/test_EI_T514_malformed_class_uuid_accept_join_request.py` |
| EI-T497 | [Classes] Malformed class identifier is rejected when attempting to delete a class | `teacher-student-automation/service/tests/classes/test_EI_T497_malformed_class_uuid_delete_class.py` |
| EI-T486 | [Classes] Malformed class identifier is rejected when attempting to delete a class announcement | `teacher-student-automation/service/tests/classes/test_EI_T486_malformed_class_uuid_delete_announcement.py` |
| EI-T508 | [Classes] Malformed class identifier is rejected when attempting to delete a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_T508_malformed_class_uuid_delete_cover_photo.py` |
| EI-T524 | [Classes] Malformed class identifier is rejected when attempting to fetch the assignments for a specific class | `teacher-student-automation/service/tests/classes/test_EI_T524_malformed_class_uuid_fetch_assignments.py`<br>`teacher-student-automation/service/utils/rejections.py` |
| EI-T480 | [Classes] Malformed class identifier is rejected when attempting to fetch the messages for a specific class | `teacher-student-automation/service/tests/classes/test_EI_T480_malformed_class_uuid_fetch_messages.py` |
| EI-T491 | [Classes] Malformed class identifier is rejected when attempting to fetch the roster of students for a specific class | `teacher-student-automation/service/tests/classes/test_EI_T491_malformed_class_uuid_fetch_roster.py` |
| EI-T517 | [Classes] Malformed class identifier is rejected when attempting to remove a student from a class | `teacher-student-automation/service/tests/classes/test_EI_T517_malformed_class_uuid_remove_student.py` |
| EI-T511 | [Classes] Malformed class identifier is rejected when attempting to restore a soft-deleted class | `teacher-student-automation/service/tests/classes/test_EI_T511_malformed_class_uuid_restore_class.py` |
| EI-T482 | [Classes] Omitting the required field 'content' is rejected when attempting to create a class announcement | `teacher-student-automation/service/tests/classes/test_EI_T482_missing_content_create_announcement.py` |
| EI-T504 | [Classes] Omitting the required field 'file' is rejected when attempting to update a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_T504_missing_file_update_cover_photo.py` |
| EI-T500 | [Classes] Omitting the required field 'file' is rejected when attempting to upload a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_T500_missing_file_upload_cover_photo.py` |
| EI-T520 | [Classes] Omitting the required field 'is_granted' is rejected when attempting to accept a student's request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_T520_missing_is_granted_accept_leave_request.py` |
| EI-T472 | [Classes] Omitting the required field 'title' is rejected when attempting to create a new class | `teacher-student-automation/service/tests/classes/test_EI_T472_missing_title_create_class.py`<br>`teacher-student-automation/service/utils/rejections.py` |
| EI-T493 | [Classes] Omitting the required field 'title' is rejected when attempting to update a class details | `teacher-student-automation/service/tests/classes/test_EI_T493_missing_title_update_class.py` |
| EI-T476 | [Classes] Out-of-range 'page_num' value is handled safely when attempting to fetch all classes | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T485 | [Classes] Script payload in 'content' is neutralised when attempting to create a class announcement | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T507 | [Classes] Script payload in 'file' is neutralised when attempting to update a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T503 | [Classes] Script payload in 'file' is neutralised when attempting to upload a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T523 | [Classes] Script payload in 'is_granted' is neutralised when attempting to accept a student's request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T475 | [Classes] Script payload in 'title' is neutralised when attempting to create a new class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T496 | [Classes] Script payload in 'title' is neutralised when attempting to update a class details | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T479 | [Classes] Unknown class code identifier returns not found when attempting to fetch a class by its code | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T490 | [Classes] Unknown class code identifier returns not found when attempting to fetch the gradebook for a specific class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T515 | [Classes] Unknown class identifier returns not found when attempting to accept a student's request to join a class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T521 | [Classes] Unknown class identifier returns not found when attempting to accept a student's request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T483 | [Classes] Unknown class identifier returns not found when attempting to create a class announcement | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T498 | [Classes] Unknown class identifier returns not found when attempting to delete a class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T487 | [Classes] Unknown class identifier returns not found when attempting to delete a class announcement | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T509 | [Classes] Unknown class identifier returns not found when attempting to delete a class cover photo | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T525 | [Classes] Unknown class identifier returns not found when attempting to fetch the assignments for a specific class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T481 | [Classes] Unknown class identifier returns not found when attempting to fetch the messages for a specific class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T492 | [Classes] Unknown class identifier returns not found when attempting to fetch the roster of students for a specific class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T518 | [Classes] Unknown class identifier returns not found when attempting to remove a student from a class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T512 | [Classes] Unknown class identifier returns not found when attempting to restore a soft-deleted class | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T494 | [Classes] Unknown class identifier returns not found when attempting to update a class details | `teacher-student-automation/service/tests/classes/test_EI_R25_edge_teacher_classes.py` |
| EI-T530 | [Question] Duplicate submission does not create a duplicate question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T546 | [Question] Empty result set is returned correctly when attempting to clear all filters | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T544 | [Question] Empty result set is returned correctly when attempting to get filter options with counts | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T539 | [Question] Empty update payload is handled correctly when attempting to update a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T545 | [Question] Expired bearer token is rejected when attempting to clear all filters | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T531 | [Question] Expired bearer token is rejected when attempting to create a new question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T542 | [Question] Expired bearer token is rejected when attempting to delete a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T529 | [Question] Expired bearer token is rejected when attempting to fetch all staff questions accessible to me | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T543 | [Question] Expired bearer token is rejected when attempting to get filter options with counts | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T538 | [Question] Expired bearer token is rejected when attempting to update a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T549 | [Question] Expired bearer token is rejected when attempting to upload an image to embed in a question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T548 | [Question] Interrupted upload leaves no orphaned asset when attempting to upload an image to embed in a question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T540 | [Question] Malformed question identifier is rejected when attempting to delete a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T534 | [Question] Malformed question identifier is rejected when attempting to fetch a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T536 | [Question] Malformed question identifier is rejected when attempting to update a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T526 | [Question] Malformed teacher identifier is rejected when attempting to fetch all questions accessible to me | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T533 | [Question] Missing Authorization header is rejected when attempting to create a new question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T547 | [Question] Omitting the required field 'file' is rejected when attempting to upload an image to embed in a question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T532 | [Question] Parallel creation requests are handled without data corruption | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T550 | [Question] Script payload in 'file' is neutralised when attempting to upload an image to embed in a question | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T528 | [Question] Unknown 'assignment_types' filter value returns no matches when attempting to fetch all staff questions accessible to me | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T541 | [Question] Unknown question identifier returns not found when attempting to delete a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T535 | [Question] Unknown question identifier returns not found when attempting to fetch a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T537 | [Question] Unknown question identifier returns not found when attempting to update a specific question by its ID | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T527 | [Question] Unknown teacher identifier returns not found when attempting to fetch all questions accessible to me | `teacher-student-automation/service/tests/question/test_EI_R26_edge_teacher_question.py` |
| EI-T566 | [Question-Import] Another account's job cannot be reached when attempting to approve a reviewed import and create the questions | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T556 | [Question-Import] Duplicate submission does not create a duplicate question import | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T557 | [Question-Import] Expired bearer token is rejected when attempting to add a single question by pasting it, and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T565 | [Question-Import] Expired bearer token is rejected when attempting to approve a reviewed import and create the questions | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T553 | [Question-Import] Expired bearer token is rejected when attempting to upload a question file and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T552 | [Question-Import] Interrupted upload leaves no orphaned asset when attempting to upload a question file and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T563 | [Question-Import] Malformed job identifier is rejected when attempting to approve a reviewed import and create the questions | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T559 | [Question-Import] Malformed job identifier is rejected when attempting to retrieve progress and per-row errors for an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T561 | [Question-Import] Malformed job identifier is rejected when attempting to retrieve proposed questions for review | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T551 | [Question-Import] Omitting the required field 'question_type' is rejected when attempting to upload a question file and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T555 | [Question-Import] Omitting the required field 'text' is rejected when attempting to add a single question by pasting it, and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_R27_edge_question_import.py` |
| EI-T554 | [Question-Import] Script payload in 'question_type' is neutralised when attempting to upload a question file and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T558 | [Question-Import] Script payload in 'text' is neutralised when attempting to add a single question by pasting it, and start an import job | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T564 | [Question-Import] Unknown job identifier returns not found when attempting to approve a reviewed import and create the questions | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T560 | [Question-Import] Unknown job identifier returns not found when attempting to retrieve progress and per-row errors for an import job | `teacher-student-automation/service/tests/question-import/test_EI_R27_edge_question_import.py` |
| EI-T562 | [Question-Import] Unknown job identifier returns not found when attempting to retrieve proposed questions for review | `teacher-student-automation/service/tests/question-import/test_EI_edge_question_import.py` |
| EI-T616 | [Assignments] Another account's submission cannot be reached when attempting to approve a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T568 | [Assignments] Duplicate submission does not create a duplicate assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T574 | [Assignments] Duplicate submission does not create a duplicate assignment (2) | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T578 | [Assignments] Empty result set is returned correctly when attempting to fetch all staff created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T602 | [Assignments] Expired bearer token is rejected when attempting to add a new comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T615 | [Assignments] Expired bearer token is rejected when attempting to approve a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T569 | [Assignments] Expired bearer token is rejected when attempting to create a new assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T575 | [Assignments] Expired bearer token is rejected when attempting to create a new assignment on behalf of staff | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T593 | [Assignments] Expired bearer token is rejected when attempting to delete a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T610 | [Assignments] Expired bearer token is rejected when attempting to delete my comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T577 | [Assignments] Expired bearer token is rejected when attempting to fetch all staff created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T589 | [Assignments] Expired bearer token is rejected when attempting to override a question's point value for this assignment only | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T619 | [Assignments] Expired bearer token is rejected when attempting to reject a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T585 | [Assignments] Expired bearer token is rejected when attempting to update an existing assignment's details | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T606 | [Assignments] Expired bearer token is rejected when attempting to update my existing comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T591 | [Assignments] Malformed assignment identifier is rejected when attempting to delete a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T579 | [Assignments] Malformed assignment identifier is rejected when attempting to fetch all staff created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T581 | [Assignments] Malformed assignment identifier is rejected when attempting to fetch my created assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T611 | [Assignments] Malformed assignment identifier is rejected when attempting to list pending late submissions for a given assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T608 | [Assignments] Malformed class code identifier is rejected when attempting to delete my comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T598 | [Assignments] Malformed class code identifier is rejected when attempting to fetch a specific student's submission for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T571 | [Assignments] Malformed class code identifier is rejected when attempting to fetch all my created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T594 | [Assignments] Malformed class code identifier is rejected when attempting to get analytics for a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T596 | [Assignments] Malformed class code identifier is rejected when attempting to get item analysis analytics for a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T613 | [Assignments] Malformed submission identifier is rejected when attempting to approve a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T600 | [Assignments] Omitting the required field 'comment' is rejected when attempting to add a new comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T604 | [Assignments] Omitting the required field 'comment' is rejected when attempting to update my existing comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T587 | [Assignments] Omitting the required field 'points' is rejected when attempting to override a question's point value for this assignment only | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T617 | [Assignments] Omitting the required field 'reason' is rejected when attempting to reject a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T567 | [Assignments] Omitting the required field 'semester' is rejected when attempting to create a new assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T573 | [Assignments] Omitting the required field 'semester' is rejected when attempting to create a new assignment on behalf of staff | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T583 | [Assignments] Omitting the required field 'semester' is rejected when attempting to update an existing assignment's details | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py`<br>`teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T603 | [Assignments] Script payload in 'comment' is neutralised when attempting to add a new comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T607 | [Assignments] Script payload in 'comment' is neutralised when attempting to update my existing comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T590 | [Assignments] Script payload in 'points' is neutralised when attempting to override a question's point value for this assignment only | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T620 | [Assignments] Script payload in 'reason' is neutralised when attempting to reject a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T570 | [Assignments] Script payload in 'semester' is neutralised when attempting to create a new assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T576 | [Assignments] Script payload in 'semester' is neutralised when attempting to create a new assignment on behalf of staff | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T586 | [Assignments] Script payload in 'semester' is neutralised when attempting to update an existing assignment's details | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T592 | [Assignments] Unknown assignment identifier returns not found when attempting to delete a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T580 | [Assignments] Unknown assignment identifier returns not found when attempting to fetch all staff created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T582 | [Assignments] Unknown assignment identifier returns not found when attempting to fetch my created assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T612 | [Assignments] Unknown assignment identifier returns not found when attempting to list pending late submissions for a given assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T588 | [Assignments] Unknown assignment identifier returns not found when attempting to override a question's point value for this assignment only | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T584 | [Assignments] Unknown assignment identifier returns not found when attempting to update an existing assignment's details | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T601 | [Assignments] Unknown class code identifier returns not found when attempting to add a new comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T609 | [Assignments] Unknown class code identifier returns not found when attempting to delete my comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T599 | [Assignments] Unknown class code identifier returns not found when attempting to fetch a specific student's submission for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T572 | [Assignments] Unknown class code identifier returns not found when attempting to fetch all my created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T595 | [Assignments] Unknown class code identifier returns not found when attempting to get analytics for a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T597 | [Assignments] Unknown class code identifier returns not found when attempting to get item analysis analytics for a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T605 | [Assignments] Unknown class code identifier returns not found when attempting to update my existing comment on a student's answer to a specific question | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T614 | [Assignments] Unknown submission identifier returns not found when attempting to approve a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T618 | [Assignments] Unknown submission identifier returns not found when attempting to reject a pending late submission | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py` |
| EI-T624 | [Theme] Duplicate submission does not create a duplicate theme | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T622 | [Theme] Empty result set is returned correctly when attempting to get current profile theme information | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T625 | [Theme] Expired bearer token is rejected when attempting to apply a new theme to profile | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T632 | [Theme] Expired bearer token is rejected when attempting to delete theme and revert to default | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T621 | [Theme] Expired bearer token is rejected when attempting to get current profile theme information | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T629 | [Theme] Expired bearer token is rejected when attempting to update current theme settings | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py` |
| EI-T623 | [Theme] Omitting the required field 'theme_id' is rejected when attempting to apply a new theme to profile | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T627 | [Theme] Omitting the required field 'theme_name' is rejected when attempting to update current theme settings | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T633 | [Theme] Removing a theme with dependent records leaves no orphaned data | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T631 | [Theme] Repeating the removal of an already deleted theme is handled safely | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T626 | [Theme] Script payload in 'theme_id' is neutralised when attempting to apply a new theme to profile | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T630 | [Theme] Script payload in 'theme_name' is neutralised when attempting to update current theme settings | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T628 | [Theme] Simultaneous updates to one theme resolve deterministically | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py` |
| EI-T639 | [Students] Deprecated operation to bulk student creation moved to Staff-Admin API no longer mutates data | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T634 | [Students] Deprecated operation to submit student creation moved to Staff-Admin API no longer mutates data | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T636 | [Students] Duplicate submission does not create a duplicate student | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T640 | [Students] Expired bearer token is rejected when attempting to bulk student creation moved to Staff-Admin API | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T635 | [Students] Expired bearer token is rejected when attempting to submit student creation moved to Staff-Admin API | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T637 | [Students] Missing Authorization header is rejected when attempting to submit student creation moved to Staff-Admin API | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T638 | [Students] Omitting the required field 'file' is rejected when attempting to bulk student creation moved to Staff-Admin API | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T641 | [Students] Script payload in 'file' is neutralised when attempting to bulk student creation moved to Staff-Admin API | `teacher-student-automation/service/tests/backup/test_EI_edge_students_deprecated.py` |
| EI-T651 | [Features] Empty result set is returned correctly when attempting to retrieve district subscription plan for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_R32_edge_teacher_features_empty.py` |
| EI-T643 | [Features] Empty result set is returned correctly when attempting to retrieve effective feature flags for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_R32_edge_teacher_features_empty.py` |
| EI-T647 | [Features] Empty result set is returned correctly when attempting to retrieve school and district plan for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_R32_edge_teacher_features_empty.py` |
| EI-T649 | [Features] Empty result set is returned correctly when attempting to retrieve school details for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_R32_edge_teacher_features_empty.py` |
| EI-T650 | [Features] Expired bearer token is rejected when attempting to retrieve district subscription plan for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T642 | [Features] Expired bearer token is rejected when attempting to retrieve effective feature flags for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T646 | [Features] Expired bearer token is rejected when attempting to retrieve school and district plan for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T648 | [Features] Expired bearer token is rejected when attempting to retrieve school details for the authenticated teacher | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T652 | [Features] Malformed class code identifier is rejected when attempting to retrieve teacher-made assignment creation quota per class | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T644 | [Features] Malformed feature name identifier is rejected when attempting to get effective status for a single feature | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T653 | [Features] Unknown class code identifier returns not found when attempting to retrieve teacher-made assignment creation quota per class | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T645 | [Features] Unknown feature name identifier returns not found when attempting to get effective status for a single feature | `teacher-student-automation/service/tests/features/test_EI_edge_teacher_features.py` |
| EI-T674 | [Accounts] Duplicate submission does not create a duplicate account (2) | `teacher-student-automation/service/tests/account/test_EI_R33_edge_student_accounts.py` |
| EI-T664 | [Accounts] Expired bearer token is rejected when attempting to add a profile picture if I don't have one already (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py`<br>`teacher-student-automation/service/tests/unit/test_token_renewal_on_401.py` |
| EI-T675 | [Accounts] Expired bearer token is rejected when attempting to change my password by providing my current password (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py` |
| EI-T671 | [Accounts] Expired bearer token is rejected when attempting to delete my profile picture (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py` |
| EI-T657 | [Accounts] Expired bearer token is rejected when attempting to search for teachers | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py`<br>`teacher-student-automation/service/tests/unit/test_token_renewal_on_401.py`<br>`teacher-student-automation/service/utils/renewable_token.py` |
| EI-T660 | [Accounts] Expired bearer token is rejected when attempting to update my contact person information | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py` |
| EI-T668 | [Accounts] Expired bearer token is rejected when attempting to update my profile picture (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_expired_bearer.py` |
| EI-T663 | [Accounts] Interrupted upload leaves no orphaned asset when attempting to add a profile picture if I don't have one already (2) | `teacher-student-automation/service/tests/account/test_EI_R33_edge_student_accounts.py` |
| EI-T667 | [Accounts] Interrupted upload leaves no orphaned asset when attempting to update my profile picture (2) | `teacher-student-automation/service/tests/account/test_EI_R33_edge_student_accounts.py` |
| EI-T654 | [Accounts] Malformed account identifier is rejected when attempting to fetch my account data | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_identifiers.py`<br>`teacher-student-automation/service/tests/features/test_zephyr_edge_student_feature_identifiers.py` |
| EI-T673 | [Accounts] Omitting the required field 'current_password' is rejected when attempting to change my password by providing my current password (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T662 | [Accounts] Omitting the required field 'file' is rejected when attempting to add a profile picture if I don't have one already (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T666 | [Accounts] Omitting the required field 'file' is rejected when attempting to update my profile picture (2) | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T658 | [Accounts] Omitting the required field 'first_name' is rejected when attempting to update my contact person information | `teacher-student-automation/service/tests/account/test_EI_R14_negative_student_accounts.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_missing_fields.py` |
| EI-T656 | [Accounts] Out-of-range 'page' value is handled safely when attempting to search for teachers | `teacher-student-automation/service/tests/account/test_EI_T316_pagination_bounds_teacher_search.py`<br>`teacher-student-automation/service/tests/account/test_zephyr_edge_student_pagination.py`<br>`teacher-student-automation/service/tests/classes/test_zephyr_edge_student_classes_pagination.py` |
| EI-T670 | [Accounts] Repeating the removal of an already deleted account is handled safely | `teacher-student-automation/service/tests/theme/test_zephyr_edge_student_repeat_removal.py` |
| EI-T676 | [Accounts] Script payload in 'current_password' is neutralised when attempting to change my password by providing my current password (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T665 | [Accounts] Script payload in 'file' is neutralised when attempting to add a profile picture if I don't have one already (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T669 | [Accounts] Script payload in 'file' is neutralised when attempting to update my profile picture (2) | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T661 | [Accounts] Script payload in 'first_name' is neutralised when attempting to update my contact person information | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_script_payloads.py` |
| EI-T655 | [Accounts] Unknown account identifier returns not found when attempting to fetch my account data | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_identifiers.py` |
| EI-T659 | [Accounts] Unknown account identifier returns not found when attempting to update my contact person information | `teacher-student-automation/service/tests/account/test_zephyr_edge_student_identifiers.py` |
| EI-T678 | [Dashboard] Empty result set is returned correctly when attempting to fetch my achievement badges | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T682 | [Dashboard] Empty result set is returned correctly when attempting to fetch my GPA (overall + per-class) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T680 | [Dashboard] Empty result set is returned correctly when attempting to fetch my grade distribution (histogram buckets) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T688 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for assignments (2) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T686 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for classes (2) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T690 | [Dashboard] Empty result set is returned correctly when attempting to fetch statistics for classes (3) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T677 | [Dashboard] Expired bearer token is rejected when attempting to fetch my achievement badges | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T681 | [Dashboard] Expired bearer token is rejected when attempting to fetch my GPA (overall + per-class) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T679 | [Dashboard] Expired bearer token is rejected when attempting to fetch my grade distribution (histogram buckets) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T687 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for assignments (2) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T685 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for classes (2) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T689 | [Dashboard] Expired bearer token is rejected when attempting to fetch statistics for classes (3) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T684 | [Dashboard] Expired bearer token is rejected when attempting to fetch upcoming assignments by due date | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T683 | [Dashboard] Out-of-range 'limit' value is handled safely when attempting to fetch upcoming assignments by due date | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py` |
| EI-T703 | [Classes] Expired bearer token is rejected when attempting to cancel a pending request to join a class | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T692 | [Classes] Expired bearer token is rejected when attempting to fetch all classes I am enrolled in | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T697 | [Classes] Expired bearer token is rejected when attempting to join a class using its code | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T700 | [Classes] Expired bearer token is rejected when attempting to request to leave a class | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T701 | [Classes] Malformed class code identifier is rejected when attempting to cancel a pending request to join a class | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T693 | [Classes] Malformed class code identifier is rejected when attempting to fetch a class by its code (2) | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T695 | [Classes] Malformed class code identifier is rejected when attempting to join a class using its code | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T698 | [Classes] Malformed class code identifier is rejected when attempting to request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T704 | [Classes] Malformed class identifier is rejected when attempting to fetch class announcements | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T691 | [Classes] Out-of-range 'page_num' value is handled safely when attempting to fetch all classes I am enrolled in | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T702 | [Classes] Unknown class code identifier returns not found when attempting to cancel a pending request to join a class | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T694 | [Classes] Unknown class code identifier returns not found when attempting to fetch a class by its code (2) | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T696 | [Classes] Unknown class code identifier returns not found when attempting to join a class using its code | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T699 | [Classes] Unknown class code identifier returns not found when attempting to request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T705 | [Classes] Unknown class identifier returns not found when attempting to fetch class announcements | `teacher-student-automation/service/tests/classes/test_EI_R35_edge_student_classes.py` |
| EI-T724 | [Assignments] Expired bearer token is rejected when attempting to report a browser-lockdown violation for an assignment attempt | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T716 | [Assignments] Expired bearer token is rejected when attempting to save all my answers for an assignment | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/assignment/test_take_assignment_student_flow.py` |
| EI-T720 | [Assignments] Expired bearer token is rejected when attempting to submit an answer for an assignment | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep.py`<br>`teacher-student-automation/service/tests/assignment/test_take_assignment_submit_flow.py` |
| EI-T712 | [Assignments] Malformed assignment identifier is rejected when attempting to answer a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T710 | [Assignments] Malformed assignment identifier is rejected when attempting to fetch a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T726 | [Assignments] Malformed assignment identifier is rejected when attempting to fetch a specific submission for review | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T706 | [Assignments] Malformed class code identifier is rejected when attempting to fetch all assignments | `teacher-student-automation/service/tests/assignment/test_EI_1114_student_assignments_fetch_all_class_code.py` |
| EI-T708 | [Assignments] Malformed class code identifier is rejected when attempting to fetch my total average grade for a class | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T714 | [Assignments] Omitting the required field 'answers' is rejected when attempting to save all my answers for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T718 | [Assignments] Omitting the required field 'answers' is rejected when attempting to submit an answer for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T722 | [Assignments] Omitting the required field 'type' is rejected when attempting to report a browser-lockdown violation for an assignment attempt | `teacher-student-automation/service/tests/assignment/test_student_assignment_violations.py` |
| EI-T717 | [Assignments] Script payload in 'answers' is neutralised when attempting to save all my answers for an assignment | `teacher-student-automation/service/tests/assignment/test_take_assignment_student_flow.py` |
| EI-T721 | [Assignments] Script payload in 'answers' is neutralised when attempting to submit an answer for an assignment | `teacher-student-automation/service/tests/assignment/test_take_assignment_submit_flow.py` |
| EI-T725 | [Assignments] Script payload in 'type' is neutralised when attempting to report a browser-lockdown violation for an assignment attempt | `teacher-student-automation/service/tests/assignment/test_student_assignment_violations.py` |
| EI-T713 | [Assignments] Unknown assignment identifier returns not found when attempting to answer a specific assignment | `teacher-student-automation/service/tests/assignment/test_take_assignment_submit_flow.py` |
| EI-T711 | [Assignments] Unknown assignment identifier returns not found when attempting to fetch a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T727 | [Assignments] Unknown assignment identifier returns not found when attempting to fetch a specific submission for review | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T723 | [Assignments] Unknown assignment identifier returns not found when attempting to report a browser-lockdown violation for an assignment attempt | `teacher-student-automation/service/tests/assignment/test_student_assignment_violations.py` |
| EI-T715 | [Assignments] Unknown assignment identifier returns not found when attempting to save all my answers for an assignment | `teacher-student-automation/service/tests/assignment/test_take_assignment_student_flow.py` |
| EI-T719 | [Assignments] Unknown assignment identifier returns not found when attempting to submit an answer for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R36_edge_student_assignments.py` |
| EI-T707 | [Assignments] Unknown class code identifier returns not found when attempting to fetch all assignments | `teacher-student-automation/service/tests/assignment/test_EI_1114_student_assignments_fetch_all_class_code.py` |
| EI-T709 | [Assignments] Unknown class code identifier returns not found when attempting to fetch my total average grade for a class | `teacher-student-automation/service/tests/assignment/test_student_grade_average.py` |
| EI-T731 | [Theme] Duplicate submission does not create a duplicate theme (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T729 | [Theme] Empty result set is returned correctly when attempting to get current profile theme information (2) | `teacher-student-automation/service/tests/dashboard/test_EI_R34_edge_student_dashboard.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T732 | [Theme] Expired bearer token is rejected when attempting to apply a new theme to profile (2) | `teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T739 | [Theme] Expired bearer token is rejected when attempting to delete theme and revert to default (2) | `teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T728 | [Theme] Expired bearer token is rejected when attempting to get current profile theme information (2) | `teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T736 | [Theme] Expired bearer token is rejected when attempting to update current theme settings (2) | `teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T730 | [Theme] Omitting the required field 'theme_id' is rejected when attempting to apply a new theme to profile (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T734 | [Theme] Omitting the required field 'theme_name' is rejected when attempting to update current theme settings (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T740 | [Theme] Removing a theme with dependent records leaves no orphaned data (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T738 | [Theme] Repeating the removal of an already deleted theme is handled safely (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py`<br>`teacher-student-automation/service/tests/theme/test_zephyr_edge_student_repeat_removal.py` |
| EI-T733 | [Theme] Script payload in 'theme_id' is neutralised when attempting to apply a new theme to profile (2) | `teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T737 | [Theme] Script payload in 'theme_name' is neutralised when attempting to update current theme settings (2) | `teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T735 | [Theme] Simultaneous updates to one theme resolve deterministically (2) | `teacher-student-automation/service/tests/assignment/test_EI_R29_edge_teacher_assignments.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R30_edge_teacher_theme.py`<br>`teacher-student-automation/service/tests/theme/test_EI_R37_edge_student_theme.py` |
| EI-T750 | [Features] Empty result set is returned correctly when attempting to retrieve district subscription plan for the authenticated student | `teacher-student-automation/service/tests/features/test_EI_R38_edge_student_features_empty.py` |
| EI-T742 | [Features] Empty result set is returned correctly when attempting to retrieve effective feature flags for the authenticated student | `teacher-student-automation/service/tests/unit/test_request_log_redaction.py` |
| EI-T746 | [Features] Empty result set is returned correctly when attempting to retrieve school and district plan for the authenticated student | `teacher-student-automation/service/tests/features/test_EI_R38_edge_student_features_empty.py` |
| EI-T748 | [Features] Empty result set is returned correctly when attempting to retrieve school details for the authenticated student | `teacher-student-automation/service/tests/features/test_EI_R38_edge_student_features_empty.py` |
| EI-T749 | [Features] Expired bearer token is rejected when attempting to retrieve district subscription plan for the authenticated student | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_features_expired_bearer.py` |
| EI-T741 | [Features] Expired bearer token is rejected when attempting to retrieve effective feature flags for the authenticated student | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_features_expired_bearer.py` |
| EI-T745 | [Features] Expired bearer token is rejected when attempting to retrieve school and district plan for the authenticated student | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_features_expired_bearer.py` |
| EI-T747 | [Features] Expired bearer token is rejected when attempting to retrieve school details for the authenticated student | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_features_expired_bearer.py` |
| EI-T743 | [Features] Malformed feature name identifier is rejected when attempting to get effective status for a single feature (2) | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_feature_identifiers.py` |
| EI-T744 | [Features] Unknown feature name identifier returns not found when attempting to get effective status for a single feature (2) | `teacher-student-automation/service/tests/features/test_zephyr_edge_student_feature_identifiers.py` |
| EI-T752 | [Assignments] Duplicate submission does not create a duplicate assignment (3) | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T760 | [Assignments] Duplicate submission does not create a duplicate assignment (4) | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T766 | [Assignments] Duplicate submission does not create a duplicate assignment (5) | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T761 | [Assignments] Expired bearer token is rejected when attempting to answer assignment | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T753 | [Assignments] Expired bearer token is rejected when attempting to create new assignment | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py`<br>`teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T777 | [Assignments] Expired bearer token is rejected when attempting to delete assignment by ID | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T767 | [Assignments] Expired bearer token is rejected when attempting to share assignment | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T773 | [Assignments] Expired bearer token is rejected when attempting to update assignment details | `teacher-student-automation/service/tests/account/test_zephyr_edge_expired_bearer_sweep_2.py` |
| EI-T775 | [Assignments] Malformed assignment identifier is rejected when attempting to delete assignment by ID | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T755 | [Assignments] Malformed assignment identifier is rejected when attempting to get specific assignment by ID | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T757 | [Assignments] Malformed assignment identifier is rejected when attempting to retrieve adoptive Next Item | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T769 | [Assignments] Malformed assignment identifier is rejected when attempting to show assignment analytics | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T763 | [Assignments] Malformed submission identifier is rejected when attempting to review submission | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T759 | [Assignments] Omitting the required field 'assignment_id' is rejected when attempting to answer assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T751 | [Assignments] Omitting the required field 'semester' is rejected when attempting to create new assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T771 | [Assignments] Omitting the required field 'semester' is rejected when attempting to update assignment details | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T765 | [Assignments] Omitting the required field 'type' is rejected when attempting to share assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T762 | [Assignments] Script payload in 'assignment_id' is neutralised when attempting to answer assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T754 | [Assignments] Script payload in 'semester' is neutralised when attempting to create new assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T774 | [Assignments] Script payload in 'semester' is neutralised when attempting to update assignment details | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T768 | [Assignments] Script payload in 'type' is neutralised when attempting to share assignment | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T776 | [Assignments] Unknown assignment identifier returns not found when attempting to delete assignment by ID | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T756 | [Assignments] Unknown assignment identifier returns not found when attempting to get specific assignment by ID | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T758 | [Assignments] Unknown assignment identifier returns not found when attempting to retrieve adoptive Next Item | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T770 | [Assignments] Unknown assignment identifier returns not found when attempting to show assignment analytics | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T772 | [Assignments] Unknown assignment identifier returns not found when attempting to update assignment details | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T764 | [Assignments] Unknown submission identifier returns not found when attempting to review submission | `teacher-student-automation/service/tests/assignment/test_EI_R39_edge_shared_assignments.py` |
| EI-T1 | User authenticates with valid email and password and receives an access token | `teacher-student-automation/service/tests/account/test_zephyr_positive_auth_login_profile.py` |
| EI-T2 | Session is rotated using the httpOnly refresh-token cookie | `teacher-student-automation/service/tests/account/test_EI_T2_session_rotation_refresh_token_cookie.py` |
| EI-T3 | User logs out and the refresh token is revoked with session cookies cleared | `teacher-student-automation/service/tests/account/test_EI_T3_logout_revokes_refresh_token_clears_cookies.py` |
| EI-T4 | Authenticated user retrieves their current profile | `teacher-student-automation/service/tests/account/test_zephyr_positive_auth_login_profile.py` |
| EI-T4 | Authenticated user retrieves their current profile | `teacher-student-automation/service/tests/account/test_zephyr_positive_auth_login_profile.py` |
| EI-T7 | Teacher adds a profile picture when none exists | `teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T11 | Teacher changes their password by supplying the current password | `teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T9 | Teacher deletes their profile picture using a matching teacher identifier | `teacher-student-automation/service/services/teacher/account_service.py`<br>`teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T6 | Teacher searches for users by name or email filtered by role | `teacher-student-automation/service/services/teacher/account_service.py`<br>`teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T8 | Teacher updates an existing profile picture | `teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T10 | Teacher updates their own account information | `teacher-student-automation/service/tests/account/test_EI_R44_positive_teacher_accounts.py` |
| EI-T14 | Teacher fetches assignment statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R45_positive_teacher_dashboard.py` |
| EI-T12 | Teacher fetches class statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R45_positive_teacher_dashboard.py` |
| EI-T13 | Teacher fetches student statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R45_positive_teacher_dashboard.py` |
| EI-T15 | Teacher fetches submission statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R45_positive_teacher_dashboard.py` |
| EI-T30 | Teacher accepts a student's request to join a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T32 | Teacher approves a student's request to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T20 | Teacher creates a class announcement | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T16 | Teacher creates a new class with required details and schedules | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T25 | Teacher deletes a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T21 | Teacher deletes a class announcement | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T18 | Teacher fetches a single class by its class code | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T17 | Teacher fetches all classes with pagination applied | `teacher-student-automation/service/tests/classes/test_teacher_class_messages_find_assignments.py` |
| EI-T19 | Teacher fetches the announcements for a specific class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T33 | Teacher fetches the assignments belonging to a specific class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T22 | Teacher fetches the gradebook for a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T23 | Teacher fetches the student roster for a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T31 | Teacher removes a student from a class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T28 | Teacher removes the cover photo from a class card | `teacher-student-automation/service/tests/classes/test_teacher_class_photo_lifecycle.py` |
| EI-T27 | Teacher replaces the cover photo on a class card | `teacher-student-automation/service/tests/classes/test_teacher_class_photo_lifecycle.py` |
| EI-T29 | Teacher restores a soft-deleted class | `teacher-student-automation/service/tests/classes/test_EI_R46_positive_teacher_classes.py` |
| EI-T24 | Teacher updates the details of an existing class | `teacher-student-automation/service/tests/classes/test_teacher_class_update_details.py` |
| EI-T26 | Teacher uploads a cover photo for a class card | `teacher-student-automation/service/tests/classes/test_teacher_class_photo_lifecycle.py` |
| EI-T41 | Teacher clears all applied question filters | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T36 | Teacher creates a new question in their question bank | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T39 | Teacher deletes a question from their bank | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T37 | Teacher fetches a specific question by its identifier | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T34 | Teacher fetches all accessible questions using catalogue filters | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T35 | Teacher fetches staff-authored questions using catalogue filters | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T40 | Teacher retrieves question filter options with result counts | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T38 | Teacher updates an existing question | `teacher-student-automation/service/tests/question/test_EI_R47_positive_teacher_question.py` |
| EI-T42 | Teacher uploads an image to embed in a question | `teacher-student-automation/service/tests/questions/test_zephyr_positive_question_image_upload.py` |
| EI-T47 | Teacher commits a reviewed import and the questions are created | `teacher-student-automation/service/tests/question-import/test_EI_R48_positive_question_import_commit_gap.py` |
| EI-T44 | Teacher pastes a single question and an import job is started | `teacher-student-automation/service/tests/question-import/test_EI_T43_upload_question_file_starts_import_job.py`<br>`teacher-student-automation/service/tests/question-import/test_EI_T44_paste_single_question_starts_import_job.py` |
| EI-T45 | Teacher polls the progress of a question import job | `teacher-student-automation/service/tests/question-import/test_EI_T45_poll_import_job_progress.py` |
| EI-T46 | Teacher reviews the proposed questions from an import before anything is saved | `teacher-student-automation/service/tests/question-import/test_EI_T46_review_proposed_questions_before_save.py` |
| EI-T43 | Teacher uploads a question file and an import job is started | `teacher-student-automation/service/tests/question-import/test_EI_T43_upload_question_file_starts_import_job.py` |
| EI-T49 | Teacher applies a new theme to their profile | `teacher-student-automation/service/tests/theme/test_EI_R49_positive_teacher_theme.py` |
| EI-T51 | Teacher deletes their theme and reverts to the default | `teacher-student-automation/service/tests/theme/test_EI_R49_positive_teacher_theme.py` |
| EI-T48 | Teacher fetches their current profile theme | `teacher-student-automation/service/tests/theme/test_EI_R49_positive_teacher_theme.py` |
| EI-T50 | Teacher updates their current theme settings | `teacher-student-automation/service/tests/theme/test_EI_R49_positive_teacher_theme.py` |
| EI-T55 | Teacher fetches the details of their school | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T53 | Teacher fetches the effective status of a single district feature | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T57 | Teacher fetches the teacher-made assignment quota for a class | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T56 | Teacher fetches their district subscription plan | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T52 | Teacher fetches their effective feature flags | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T54 | Teacher fetches their school and district plan information | `teacher-student-automation/service/tests/features/test_EI_R50_positive_teacher_features.py` |
| EI-T119 | Analytics are returned for a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T120 | Assignment details are updated through the shared assignments service | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T121 | Assignment is deleted through the shared assignments service | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T118 | Assignment is shared with another user | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T113 | New assignment is created through the shared assignments service | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T114 | Specific assignment is retrieved by its identifier through the shared service | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T117 | Submission is retrieved for review by its submission identifier | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T70 | Teacher adds a comment on a student's answer to a question | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T74 | Teacher approves a pending late submission with a late penalty | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T58 | Teacher creates a new assignment with required details and questions | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T60 | Teacher creates an assignment on behalf of staff | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T66 | Teacher deletes an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T72 | Teacher deletes their comment on a student's answer | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T62 | Teacher fetches a single staff-created assignment by its identifier | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T59 | Teacher fetches all assignments created for a class | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T69 | Teacher fetches an individual student's submission for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T68 | Teacher fetches item analysis analytics for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T63 | Teacher fetches one of their own created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T67 | Teacher fetches the analytics summary for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T61 | Teacher fetches the catalogue of staff-created assignments | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T73 | Teacher lists pending late submissions for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T65 | Teacher overrides a question's point value for a single assignment | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T75 | Teacher rejects a pending late submission with a reason | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T64 | Teacher updates an existing assignment's details | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T71 | Teacher updates their existing comment on a student's answer | `teacher-student-automation/service/tests/assignment/test_EI_R51_positive_teacher_assignments.py` |
| EI-T79 | Student adds a profile picture when none exists | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T82 | Student changes their password by supplying the current password | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T81 | Student deletes their profile picture | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T76 | Student fetches their own account data | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T77 | Student searches for teachers by name with pagination | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T80 | Student updates an existing profile picture | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T78 | Student updates their contact person information | `teacher-student-automation/service/tests/account/test_EI_R52_positive_student_accounts.py` |
| EI-T88 | Student fetches assignment statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T87 | Student fetches class statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_student_dashboard_statistics.py` |
| EI-T89 | Student fetches submission statistics for the dashboard | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T83 | Student fetches their achievement badges | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T84 | Student fetches their grade distribution as histogram buckets | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T85 | Student fetches their overall and per-class GPA | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T86 | Student fetches upcoming assignments for the dashboard calendar | `teacher-student-automation/service/tests/dashboard/test_EI_R15_negative_student_dashboard.py` |
| EI-T94 | Student cancels a pending request to join a class | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T90 | Student fetches all classes they are enrolled in with pagination | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T91 | Student fetches an enrolled class by its class code | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T95 | Student fetches the announcements for a class they are enrolled in | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T92 | Student joins a class using its class code | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T93 | Student requests to leave a class | `teacher-student-automation/service/tests/classes/test_EI_R54_positive_student_classes.py` |
| EI-T115 | Next adaptive item is served based on the previous response | `teacher-student-automation/service/tests/assignment/test_next_adaptive_item_served.py` |
| EI-T96 | Student fetches all assignments issued to a class | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T98 | Student fetches the details of a specific assignment | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T99 | Student fetches the questions for an assignment in order to answer it | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T103 | Student fetches their submission for an assignment to review it | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T97 | Student fetches their total average grade for a class | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T102 | Student reports a browser-lockdown violation during an assignment attempt | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T100 | Student saves their answers for an assignment in progress | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T116 | Student submission is recorded through the shared answer service | `teacher-student-automation/service/tests/assignment/test_shared_answer_service_records_submission.py` |
| EI-T101 | Student submits their answers for an assignment | `teacher-student-automation/service/tests/assignment/test_EI_R55_positive_student_assignments.py` |
| EI-T105 | Student applies a new theme to their profile | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T107 | Student deletes their theme and reverts to the default | `teacher-student-automation/service/tests/theme/test_student_theme_lifecycle.py` |
| EI-T104 | Student fetches their current profile theme | `teacher-student-automation/service/tests/theme/test_EI_T104_student_fetch_current_theme.py` |
| EI-T106 | Student updates their current theme settings | `teacher-student-automation/service/tests/theme/test_EI_R18_negative_student_theme.py` |
| EI-T111 | Student fetches the details of their school | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T109 | Student fetches the effective status of a single district feature | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T112 | Student fetches their district subscription plan | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T108 | Student fetches their effective feature flags | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |
| EI-T110 | Student fetches their school and district plan information | `teacher-student-automation/service/tests/features/test_EI_R19_negative_student_features.py` |

</details>

## Method & limits

- A case counts as automated when `automation_coverage_report.csv` marks it `Yes`: an API test in `teacher-student-automation/service` carries its `EI-T###` key in a test function name (or an older test mentions the key). The CSV is refreshed as each batch lands; this file is generated from it by `scripts/zephyr_coverage_md.py`.
- The UI layer (section 7) is separate: each Positive case has either a UI test in `teacher-student-automation/client` or an `API-ONLY` line with the reason there is no screen. UI tests do not change the coverage figures above.
- JIRA-ID-only (`EI-###`) or name-only references are not counted; a key mentioned only in a comment would be.
- Admin-suite tests that reference only their own ids (EI-TC-###, EI-####) cannot be tied to a sheet row without a mapping to the Zephyr keys.
- Results in section 7 are from the last run of each test, recorded in `automation_logs.txt`. They are automation results, not manual-testing results, and are not written to the Google Sheet (which tracks manual testing only).
- Mermaid charts render on GitHub, VS Code (Markdown Preview Mermaid) and most viewers; the bars and tables work everywhere.
- Per-row data: `automation_coverage_report.csv`.
