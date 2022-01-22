# todo-cli
A simple implementation of priority queue in a to-do application with a CLI interface.

## Installation
* Clone the repo
* Set an alias: `alias todo="python3 <Project directory here>"` in `.bashrc` file

## Usage
* To add a task, simply use the command `todo taskname --p priority`
* Ex: `todo 'Clean fishtank' --p 3`
* To get a task, use the command `todo pop`
* Supports 3 priority levels: 1(High), 2(Medium), 3(Low)
* Tasks will be popped based on priority
* Not setting up a priority would default to 2

## How it works
* The project uses a priority queue to maintain the to-do tasks
* Python's built-in library `argparse` is used to collect input through CLI
* `pickle` library is used for consistent data storage across sessions