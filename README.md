# devtrack

DevTrack is a simple Django backend API for tracking engineering issues. It allows reporters to file issues, set priorities, and track issue status.

## How to Run the Project

1. Clone the repository:

```bash
git clone <repository-url>
cd devtrack
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install django
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Reporter Endpoints

#### Create Reporter

```http
POST /api/reporters/
```

Creates a new reporter.

#### Get All Reporters

```http
GET /api/reporters/
```

Returns all reporters.

#### Get Reporter By ID

```http
GET /api/reporters/?id=1
```

Returns a single reporter matching the provided ID.

### Issue Endpoints

#### Create Issue

```http
POST /api/issues/
```

Creates a new issue and returns a priority-based message.

#### Get All Issues

```http
GET /api/issues/
```

Returns all issues.

#### Get Issue By ID

```http
GET /api/issues/?id=1
```

Returns a single issue.

#### Filter Issues By Status

```http
GET /api/issues/?status=open
```

Returns all issues with the specified status.

## Design Decision

I used inheritance for issue priorities by creating `CriticalIssue` and `LowPriorityIssue` classes that extend the base `Issue` class. This allows different issue types to provide their own implementation of the `describe()` method while reusing the common validation and data handling logic from the parent class. This demonstrates object-oriented programming concepts such as inheritance and method overriding while keeping the code easy to maintain.
