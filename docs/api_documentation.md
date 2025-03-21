# ...existing documentation...

## POST /activities/{activity_name}/unregister

Unregister a student from an activity.

### Parameters
- `activity_name` (string): The name of the activity.
- `email` (string): The email of the student to unregister.

### Responses
- `200 OK`: Successfully unregistered the student.
  ```json
  {
    "message": "Unregistered {email} from {activity_name}"
  }
  ```
- `400 Bad Request`: The student is not signed up for the activity.
  ```json
  {
    "detail": "Student is not signed up for this activity"
  }
  ```
- `404 Not Found`: The activity does not exist.
  ```json
  {
    "detail": "Activity not found"
  }
  ```

# ...existing documentation...
