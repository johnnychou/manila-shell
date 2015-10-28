Manila User Shell
======
## Introduction
Python Version: 2.7, 3.5

## Usage

There are three method can test command line tool.

1. **Run directly**: `python -m manila-shell`
2. **Install with develop**: `python setup.py develop`, then you can use `manila-shell` command.
3. **Install**: `python setup.py install`, then you can use `manila-shell` command.

## Commands

```
volume set <VOLNAME> <KEY> <VALUE>
volume reset <VOLNAME> [option] [force]
volume info [all|<VOLNAME>] --xml 
volume start <VOLNAME> [force]
volume stop <VOLNAME> [force]
volume quota <VOLNAME> {enable|disable|list [<path> ...]| list-objects [<path> ...] | remove <path>| remove-objects <path> | default-soft-limit <percent>} |
volume quota <VOLNAME> {limit-usage <path> <size> [<percent>]} |
volume quota <VOLNAME> {limit-objects <path> <number> [<percent>]} |
volume quota <VOLNAME> {alert-time|soft-timeout|hard-timeout} {<time>}
volume list
snapshot list [volname]
snapshot activate <snapname> [force]
snapshot clone <clonename> <snapname>
--version
```

## Develop

### Coding Style

Please Use [PEP8](https://www.python.org/dev/peps/pep-0008/) Coding Style and [EditorConfig](http://editorconfig.org/).

Run `python setup.py flake8`

### Commit Message

Please follow [angular changelog format](https://github.com/ajoslin/conventional-changelog/blob/master/conventions/angular.md).

There are three type prefix can be used:
* **feat**: New feature
* **fix**: Fix issue
* **perf**: Performance issue

Other prefixes can be used for non-changelog tasks:
* **chore**: Update document, Release, etc.
* **style**: Coding style
* **refactor**: Refactor function
* **test**: Testing

## Reference:

+ Python Module: [Argparser](https://docs.python.org/2/library/argparse.html)
+ Python Module: [Cmd](https://docs.python.org/2.7/library/cmd.html)
+ Python PEP8 Standard: [PEP8](https://www.python.org/dev/peps/pep-0008/)
+ Pythonic Introduction: [Python 慣用語](http://seanlin.logdown.com/tags/Python?page=1)
