Description
==================
This python script searches for given regex pattern in file(s) or stdin

| Parameter:      | Type:     | Description:                                 | Example:           |
|:----------------|:----------|:---------------------------------------------|:-------------------|
| -r --regex      | mandatory | regex pattern                                | [0-9][0-9][0-9]    |
| -f --file       | mandatory | file name to work on. multiple files allowed | file.txt / "f1 f2" |
| -c --color      | optional  | highlighted output                           | -c                 |
| -u --underscore | optional  | prints '^' behind a match                    | -u                 |
| -m --machine    | optional  | generates machine readable format:           | -m                 |
|                 |           |     file_name:line_numer:start_position:match|                    |

Usage examples:
---------------
python3 finder.py -f "file.txt" -r "[0-9][0-9][0-9] -c -u"
  
Contributing
------------
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write you change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------
Authors: Yuri Bernshtein
License: GPL v3
