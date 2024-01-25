# Log Parsing Script

## Description

This script reads input from stdin line by line and computes metrics based on a specified input format. The input format should be in the following structure:

```py
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the format is not as specified, the line will be skipped. After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints the following statistics:

- Total file size: `<total size>`, where `<total size>` is the sum of all previous `<file size>` values.
- Number of lines by status code:

  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
  - If a status code doesn’t appear or is not an integer, nothing is printed for that status code.
  - Format: `<status code>: <number>`.
  - Status codes are printed in ascending order.

## Usage

1. **Run the log generator:**

   ```bash
   ./log_generator.py | ./log_parser.py
   ```

   Note: Replace `log_generator.py` and `log_parser.py` with the actual names of your generator and parser scripts.

2. The script will process the input and print statistics every 10 lines or upon receiving a keyboard interruption.

## Example

```bash
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
...
```
