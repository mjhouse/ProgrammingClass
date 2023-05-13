
## Memory

All programs use memory when they run. Memory is the space set aside by your computer to hold things while the computer is on- it's your RAM. This is not the same thing as the storage space on disk, which is just used to persist things while the computer is turned off. Everything that your program uses is stored in memory- numbers, text, even the program itself. There are two kinds of memory your program can access- the **Stack** and the **Heap**. In many dynamic languages (and even compiled languages, really), you won't have to worry about the difference, but it's good to know that it exists.

**Stack**

* Quicker than the heap
* Used automatically when you use data like numbers and text in your program
* Has limits (but they're probably higher than you'll need to go)
* Goes away when the program ends

**Heap**

* Slower than the stack
* Used explicitly (in compiled languages) with keywords like 'new'
* Has much higher limits
* Can sometimes NOT go away when the program ends, leading to "memory leaks"
