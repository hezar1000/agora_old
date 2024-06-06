===========================================
Should we keep using this README?

===========================================
Tasks that Alice is working on:

Spot checks:
- Enter the spot check probability
- Hand code the number of spot checks for each TA.
- Let each TA request a review.
- Enter the hours for each TA and the hours for each review
- May be useful to display statistics on time.

* Question: Do we want to allow different rubrics for different types of reviews?  If the rubrics are different, how do we compare different reviews?

===========================================

Modules
========

URL convention: 
    * The ID of an object always comes immediately after the object type.
    * For example, the URL for editing submission 4 of assignment 20 is:
        assignment/20/submission/4/edit/
      In urls.py of the peer_assignment module, this URL would be specified as
        20/submission/4/edit/

peer_assignment:
--------------
* This module handles the assignments, e.g. creating, modifying, making them visible.

* The independent/supervised status of each student is at the assignment level.  The reason of not storing this information at the course level is to have fine grained data on how a student changes between the two states throughout the course.

* Homepage.

* Create new assignment.  
    * Fields in the form: Course, Name, Browsable, Deadline, and Files.
    * This form is implemented by ourselves rather than using Django forms because there are only a few fields and we can easily allow a multiple file picker.  

* Display the list of existing assignments for a course.
    * On the cours page, we already display this as a table.
    * Fields: display name, deadline, files, browsable, and options (show/hide, edit, delete). 
    * Files are displayed as links and can be downloaded.
    * A student can only see browsable assignments.

* Edit an existing assignment.
    * Display the existing properties of the assignment and let people change it.  

* Create a new assignment submission.
* Display an assignment submission.
* Edit an existing assignment submission.

peer_auth:
-----------
* This module handles users, e.g. authenticating, editing their information.

* What do superuser and staff mean?
    * There is a single superuser, who is an admin person.  
    * Every instructor is a staff but not a superuser.  Staff is able to create a course. 
    * Everyone else (students and TAs) is not a superuser and not a staff.

+ Edit user information page:
    * Title: User First_name Last_name
    * Form shows the current information and allows the person to update the information.
    * If the user is staff:
        * Fields: user ID, email, first name, last name
    * If the user is not a staff:
        * Fields: student ID, email, first name, last name
        * Student ID is not modifiable. Displays a message that "only instructor can modify the ID."

* Use the login_required decorator to check whether a user is authenticated.

peer_panel:
-----------

* Added We need a consistent way to handle success/fail/warning messages after a submit. 
    * DONE: After creating a course successfully, show a message saying that "course .... created successfully."
    * DONE: Add a message to notify the user that a course is NOT browsable when created. 

* Homepage
    * The second button on the menu bar is "Courses".  
        * Clicking on this button will lead us to a page with a list of course display names with no other information.
        * Each course name in the list should not be clickable.
        * If I'm not logged in, the top right corner should display Log In and Sign Up.
        * If I am logged in, the top right corner should display Log Out.

    * In the middle, we have the name of our software: The Next-Generation Agora.
    * The Get Started button opens the signup page.

* "course/all"
    * Once I am logged in, I am directed to this page.

    * MTANG icon
    * Home link: On the top left corner takes me back to this page.
    * Admin link: If I am "a staff", then Admin link is displayed.

    * Sections of this page:
        * User information
        * Create a course or enroll in a course. (see peer_course)
        * List of courses (see peer_course)

peer_course:
------------
* This module handles courses, e.g. creating, editing, showing users, editing configurations.

* A user could have different roles in different courses.  A student can be a student in one course and a TA in another course.  This relationship is managed by the CourseMember table.

* List of courses:
    * Clicking "(display) name" opens the course home page.
    * (for an instructor or a TA):
        * Fields: (display) name, student access code, TA access code, browsable, role
        * Options: manage users, edit course configurations, hide from students/make visible to students, archive.
    * (for a student):
        * Fields: (display) name, status message.
        * Only display browsable courses, and do not display browsable column in the table.
    * Note: We do not ever want to delete a course.  I've changed the "delete" action to "archive".  Set "archived" to be true when a course is archived.

* Create a course (if the current user is an instructor)
    * The user needs to specify a course display name to create the course.
    * By default, a newly created course is NOT browsable and NOT archived.
    * A course is browsable if a student can see it.
    * QUESTION: What does "archived" mean?

* Enroll in a course (if current user is a student)
    * When we create a course, we create 2 enrollment codes, one for students, and one for TAs.
    * Students and TAs use different codes to enroll because they have different user types in the CourseMember table.

peer_review:
------------
* This module handles peer reviews for an assignment.

* Need to store a grading rubric for each assignment.
    * How is a grading rubric represented?
    * It consists of many multiple-choice questions.  Each question requires one answer.
    * It also includes a comment field.  
    * Every rubric multiple-choice question is associated with an assignment.
    * An assignment has exactly one rubric comment.

* Every "GradingAssignment" is associated with an submission.  The submission is for an assignment, and the assignment has a rubric.

* Create a peer review:
    * Given a submission and a grader, create a peer review assignment.

* An instructor should see
    * All the assigned peer reviews.
    * The list of peer reviews assigned to the instructor.

* A TA should 
    * All the assigned peer reviews.
    * the list of peer reviews assigned to him/her.

* A student should see 
    * the list of peer reviews assigned to him/her.
    * the peer reviews for his/her submission.

* Rubric model:
    * A rubric contains many rubric questions.
    * Each rubric question has a title and a text description.  It also has several multiple choice items.
    * Each multiple choice item has a text description and a number of marks (optional).


* Rubric functionalities:
    * Create a new rubric question with any number of multiple choice items.
    * View the list of rubric questions
    * Edit each rubric question and its multiple choice items.

    * Create a new rubric to contain any number of existing rubric questions.
    * View the list of rubrics.
    * Edit an existing rubric to change the rubric questions associated with it.

Others
-----------------

* Notes by Alice:  
    * Let's indent the files properly so that they are easier to read.
    * Put comments whenever possible.

* Alice: I used Django 1.11 without problem.

==========================
Install instructions:
- install python3
- install pip3
- install latest version of Django through pip3
- git clone the repository from bitbucket called agora
- go into the cloned folder and run 
- run migrations
"python3 manage.py makemigrations"
"python3 manage.py migrate"
- run the django app
"python3 manage.py runserver"
==========================

=================

Notes from meetings

Integration:  
- We may want to integrate this with some LMS.  
- Ask Anthony Winstanley about it.
- Which LMS is popular?  Make sure that we architect things to make it easy to do.
- What does a LMS do?  Manage students and associate them with grades.
- Perhaps the integration involves getting user information from somewhere else rather than letting people register themselves.
- Anthony: what's the best authentication system? 

- We want to be able to perform validations on assignment submissions, in terms of checking number of characters and file sizes.

What types of things might people input as part of a submission?
- Textfield
- Hyperlinks
- Files

=================
Useful resources:


* Nested formsets:
http://www.yergler.net/blog/2013/09/03/nested-formsets-redux/

* The right approach to edit files:
-- show the current value of this field by just printing the filename or URL, a clickable link to download it, or if it's an image: just show it, possibly as thumbnail
-- the <input> tag to upload new files and a message making it clear that all existing files will be deleted and replaced by the new files.

See the answer by Wim in the following post:
-- https://stackoverflow.com/questions/1696877/how-to-set-a-value-to-a-file-input-in-html

* Splitted date time field on Django model forms
http://toshlyons.com/web-development/django-split-datetime-fields
* Dynamically add a field to a form
https://stackoverflow.com/questions/6142025/dynamically-add-field-to-a-form
* How to change the name of a Django app?
https://stackoverflow.com/questions/8408046/how-to-change-the-name-of-a-django-app
* A nice post about static and media files in Django
https://timmyomahony.com/blog/static-vs-media-and-root-vs-path-in-django/
* Django inline model form
http://www.catharinegeek.com/how-to-set-initial-data-for-inline-model-formset-in-django/

* Potentially useful posts:
https://stackoverflow.com/questions/39258965/how-can-i-process-a-multiple-files-from-a-file-field-in-django
https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
