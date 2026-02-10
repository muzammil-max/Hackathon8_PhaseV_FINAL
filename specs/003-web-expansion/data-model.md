# Data Model: Phase 2 Web Expansion

**Status**: Draft
**Source**: specs/003-web-expansion/spec.md

## Entities

### User
Represents a registered user of the system.

| Field | Type | Required | Unique | Description |
|-------|------|----------|--------|-------------|
| id | UUID | Yes | Yes | Primary Key |
| email | String | Yes | Yes | User's email address |
| password_hash | String | Yes | No | Hashed password |
| created_at | DateTime | Yes | No | Timestamp of registration |
| updated_at | DateTime | Yes | No | Timestamp of last update |

**Relationships:**
- One-to-Many with **Task** (One User has many Tasks)

### Task
Represents a todo item. Preserves Phase 1 fields plus owner linkage.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | UUID | Yes | Primary Key |
| title | String | Yes | Task description/title |
| status | Enum | Yes | `TODO`, `IN_PROGRESS`, `DONE` (Default: `TODO`) |
| priority | Enum | No | `LOW`, `MEDIUM`, `HIGH` (Optional) |
| owner_id | UUID | Yes | Foreign Key to User.id |
| created_at | DateTime | Yes | Creation timestamp |
| updated_at | DateTime | Yes | Last update timestamp |

**Relationships:**
- Many-to-One with **User** (Task belongs to one User)

## Validation Rules

1. **Email**: Must be a valid email format.
2. **Title**: Must not be empty, max length 255 chars.
3. **Status**: Must be one of the allowed enum values.
4. **Owner**: Must exist in the User table (Foreign Key constraint).
