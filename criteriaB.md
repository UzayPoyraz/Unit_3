Criteria B: Designing
===

## The sketch of the application:
Unfortunately, I do not have the photos of the sketches made for the application, but from the recordings there are multiple feedback I got and instead of making anew sketch, I designed the draft of the application in Qt designer according to the feedback I recieved.


## Feedback:
The client overall liked the design of the application and it met the criterias but a little issue that was mentioned was, there were too many windows.
This not only makes the application more complicated, it is also a disadvantage on the programers side because it takes more work to develope it.

**Changes I made:** My initial plan was to have 6 different ways of inspecting the list: These were Brand, Material, Used, Unused, Useable corner and the intire list. The list prioritzed the collums according to which one you pressed. Unfortuneately, this meant that there was going to be 6 more windows to the program, which made it complicated so I scratched that idea. Instead of dividing the list in 6 different sections, I decided to stick with only one of them: the full list. This way the program's usability increased because there were less option to pick from so the user is not confused.


## My draft design:
Finally after considering the feedback, I established a draft design which included everything the client wants without making it complicated. The Design can be seen in the **GuiOfProgram** folder on my repository. I divided every window and uploaded them seperately so it is easier to inspect. The design might look dull but the criteria does not require a good design but a functional one.


## Explanation of the user interface:
The User interface is divided into 6 windows, these are:

**Login:** I decided to add a Login so that the application is secure and it can be used by many users

**Register:** I also put a register part for new users or creating an account in general

**Menu:** The menu has three buttons, these are List, Edit, Add/Delete respectively, once you click any of them they will redirect you to another window.

**List:** This windows shows the entire database of the program. The table is devided in 5 sections: Brand, Material, Used, Unused and Useable corner.

**Edit:** In this window you can edit erasers by simply writing the properties of the eraser, selecting, and adding the new updated information.

**Add/Delete:** This window looks the same as the editting window but it has different buttons and fuctions. In this window you can Add a pencil to the database by edtering the details of the 5 sections. additionally, you can delete an eraser by writing it's 5 details.

