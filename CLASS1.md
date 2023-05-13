# Class #1

## Types of programming languages

Ordered from from most, to least abstracted.

### Assembly

Least abstracted from the underlying hardware, assembly is very machine and architecture dependent. It's basically a system of human-readable mnemonics that translates directly to binary machine code.

Languages: ARM, MIPS, x86

### Compiled

Compiled languages are traditional programming languages that provide a little more of a friendly wrapper around assembly. The hard work of adapting to different hardware is handled by the compiler, so the programmer mostly doesn't have to deal with it. The compiler takes your code and outputs assembly/binary that can execute on the target computer (normally the one you're on, but you can also compile for another system- that's called "cross-compiling").

**Languages: C++, C, Rust, Go**

### Bytecode

Bytecode languages are a newer type of programming language that sit right between compiled and interpreted languages. They "compile" down to an intermediate interpretation (bytecode) but that format still requires a "runtime" to execute, like interpreted languages. They're generally faster than interpreted languages, but not as fast as compiled, but they have a more friendly syntax than compiled languages.

**Languages: Java, C#**

### Interpreted

Interpreted languages are, as the name suggests, *interpreted*. Your program isn't actually run by the computer, but by a program (the interpretor) that runs on the computer. For languages like Python, this is the python executable, or Javascript, it's the browser. Interpreted languages are probably the easiest types of language to learn because the interpretor handles a lot of the lower level concepts for you.

**Languages: Python, Javascript**

### Other

There are also a huge number of languages that don't fit neatly into these categories or that aren't exactly "languages". These pseudo languages or formats are used to do things like lay out user interfaces, automate system tasks, structure data, or query databases. There is no clear line between programming languages and these "sort-of" languages, and if you get experienced enough at programming, you'll probably have to learn one or more of them. 

| Name       | Description                 |
|--          |--                           |
| SQL        | Used to query databases     |
| Bash       | Scripting for Linux         |
| Powershell | Scripting for Windows       |
| HTML       | Layout webpages             |
| TOML       | Often used for config files |
| CSS        | Style websites/UIs          | 
| SASS       | Elaboration of CSS          | 
| XML        | Structured data             | 
| JSON       | Structured data             | 
| Markdown   | Used for formatting text    | 

**A note on "Scripting":**

While there is no clear line where an interpreted language becomes a "script" or where a script becomes a "program", generally, I consider scripts of sufficient complexity to be programs. So I might call a one-off python script a "script" and a sufficiently elaborate bash script a "program", even though I've listed Python here as a programming language, and I consider Bash to be a scripting language. It's semantics, basically.

## Types of programs

The output from a compilation process can be a number of things. Some languages don't really have an "output" that's significantly different from the input- Python, for example, mostly just has Python scripts (although they've been creeping into bytecode territory for performance reasons). C++ has a binary executable file. Some compiled files aren't executable (you can't run them), but just used by other programs when *they* run. We call these files "libraries."

**Scripts**

* Run by an interpreter
* Basically just code in a file
* Plain text- you can open and read them

**Executables**

* Run by the operating system
* Basically binary blobs in the file system
* You can't open them and read them

**Libraries**

* Not run at all
* Used as a component in a larger program
* Can be *included* with the program (static library; *.a* or *.lib*)
* Can be used by *multiple* programs (shared library; *.dll* or *.so*)

## How projects are structured

Projects are organized a little differently depending on the language and the preferences of the programmer. Most projects are a folder with sub folders in them for different kinds of files:

* Project organization files like a README.md, or LICENSE.md
* Reference documents
* Assets like images, logos or fonts. 
* Tests for the project, sometimes alongside the source code, sometimes in a subdirectory called "tests" or "test". 
* Source code, often in a directory named "src", "source" or the name of the project.
* Examples or documentation for the project.

Most projects are built, tested and released using *build tools*. These tools streamline all the small tasks necessary to compile or package a program from source code.

Example: [ag-lcd](https://github.com/mjhouse/ag-lcd)

## How projects are developed

Generally, software is developed by a group of programmers working together. This means that many different people are changing the source code in different and sometimes conflicting ways, across many different computers. To make this possible, **version control tools** were developed, the most common of which is called **git**. Git, and Github (the website that hosts programming projects, called "repositories") are used to keep track of the hundreds of small changes that have been done to a particular project. 

Using git, you can see everything that anyone has done to the software and return the project to any earlier state that it has ever been in. If necessary, you can roll back undesireable changes to the source code and then continue from the new state. Git is a lot like having save points for your work.

Example: [blockly-games](https://github.com/google/blockly-games/commits/master)

## Open source software

You may have noticed that the above two sections mentioned repeatedly how teams of people might work together to build software, but didn't spend much time on how those people get paid. Much (maybe even most) or the software made today is *open source*. This means that it's developed by programmers and then the source code is provided for free to the public. There are upsides and downsides to this arrangement and a variety of opinions on the practice. 

The main takeaway is that as a programmer, you have no end of software to incorporate into your own projects, modify or hack.