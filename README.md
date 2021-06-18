# Data team coding exercise

## Background

You've been hired as a data engineer for **PLAYWIBRIX** a company who manufacture plastic components for construction toys.

There are grander plans for their data... but for now you've been tasked to process some information about components and orders, and create a simple output detailing how many units of each coloured component that were ordered on 3rd June 2021.

You've been given two data sets (available in https://github.com/qmetric/data-team-coding-exercise/tree/main/data):

`components.csv` - A reference data set in CSV containing some information about the components the company manufactures. For this task you'll be interested in the component ID and the colour of the component.

`orders.json.txt` - A file containing lines of JSON records. Each record represents an order of a number of units of different components. The file covers a period over 2nd to 4th June 2021

So just as an example, your output could look like:

```
Red: 500
Orange: 700
...
```

---

## Notes and Hints

Please use (preferably) Python, or Java to complete this exercise.

**You are free to use any data processing frameworks or libraries as you like.**

Please provide instructions to run your code to produce the output required.

Aside from the practicalities of the exercise, we will be assessing your approach to software engineering... but please don't spend longer than a couple of hours on this task.

Most of all, we'd really love to see a clean, tested, codebase, with a maintainable design. And expect to extend your submission in a future exercise.

Good luck!
