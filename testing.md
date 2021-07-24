<h1>WILD ARGENTINA</h1>
<h2>Backend Development Milestone Project</h2>

<h1>Testing</h1>


## User Experience (UX)

## User stories testing

### First time visitor

* "As a First Time Visitor, I expect the purpose of the website to be explicit"
   * The user is received by an images slider, with the first slide showcasing a WILD ARGENTINA banner, and the following the names and picture of the different regions.
   * Website's header reads WA.
   * "About WA" section is in the home page, where the mission and objectives of the organization are displayed.

* "As a First Time Visitor, I consider smooth navigation through content to be a key aspect"
   * A practical fixed positioned navbar that collapses into a burger button for small screens fulfill this purpose.
   * Website's header will take the user to the home page, aswell as the "home" anchor. 
   * Scrolldown anchor will take the user to navigation section.
   * Navigation section serves as an attention call to the website's features.

* "As a First Time Visitor, I want the content of the website to be relevant and concise"
   * Each region counts with a short summary of information about their main characteristic.
   * User input for added experiences summaries is limited.

* "As a First Time Visitor, I want to browse  places, foods and experiences"
   * In the "Browser" page, the user can freely navigate through every experience available, aswell as querying by using the searchbar.
   * "Discover" page will filter content by region on a separate page. (for future features)

### Returning visitor

* "As a Returning Visitor, I would like to see new entries and updates"
   * All experiences are shown on the "Browse" page.

* "As a Returning Visitor, I want to have ease of access to contact the bakery"
   * The contact form is connected to emailJS API, sending emails to the registered mailbox every time an user submits a form.
   * The user will receive an email confirming successful form submission.
   * The user will receive a website alert on submission.

* "As a Returning Visitor, I'd like to check Wild Argentina's activity on social media"
   * Social media anchors are available at footer. Instagram, Facebook and LinkedIn.

* "As a Returning Visitor, I want to be part of the Wild Argentina community"
   * Users can register in the website through the contact form, where they can upload their information and customize their profile.

### Frequent user

* "As a Frequent User, I want to have control over my information"
    * Once registered, users can share, edit and delete their experiences, aswell as their personal profile information.
    * My experiences section in "Profile" page displays the latest added experiences from the user.

* "As a Frequent User, I want to check new features"
   * Future features include: 
    * User's travel journal. For those users who would like to read about someone else's adventures.
    * Trip maker functionality with travel map, where users will be able to make a schedule of activities.
    * Saved experiences section.
    * Experience's comment section.
    * Pagination for experiences.
    * Expanded information area for each region, with relevant media and links.
    * Awareness section. Where users can be informed on how to preserve the enviroments visited, and how to help the local communities.
    * Aesthetic animations.
    * Pick location interactive map in "Share" form. (instead of latitude/longitude input fields)

## Functionality Testing
##### -- (Check = Working as expected) -- 

### Navigation

#### base.html

* Clicked each navbar item - Check
* Clicked each navbar item (mobile) - Check
* Clicked header to ensure that it redirects to home page - Check
* Clicked header to ensure that it redirects to home page. (mobile) - Check
* Clicked social media links in footer - Check

#### index.html

* Clicked each anchor in navigation section - Check

#### Contact Form

* Clicked contact button trigger, modal form pop up - Check
* Validation functional - Check

![form-validation.png](/static/images/doc-img/form-validation.png)

* Submit button triggers modal pop up indicating success or failure - Check

##### emailJS
* Feature is expected to send form information to a mailbox through emailJS API.
  * Filled and submitted form for testing. Email received in mailbox. - Check
 ![new-message.png](/static/images/doc-img/new-message.png)
* Feature is expected to send a confirmation email to the user.
  * Filled and submitted form for testing. Email received in personal mailbox. - Check
 ![email-sent.png](/static/images/doc-img/email-sent.png)


![alert.png](/static/images/doc-img/alert.png)

#### browse.html

* Clicked "Read More" anchor at individual experiences - Check
* Search bar queries the database for words found in several fields (region_name, experience_name, category_name, location_name, experience_description, by[username]) - Check
* Reset button at search bar resets the displayed images to default behaviour - Check

![browse.jpg](/static/images/doc-img/browse.jpg)

#### discover.html

* Clicked "Discover Experiences" button at every region - Check

#### view_experience.html

* Clicked scrolldown anchor button - Check
* Clicked every picture in gallery to ensure they replace the expanded one - Check

![gallery.png](/static/images/doc-img/gallery.png)

* Google Maps API. Feature is expected to show a map over the location, with a marker and a pop-up window on click - Check
    * Street view and satellite features fully responsive - Check

![map.png](/static/images/doc-img/map.png)

#### login.html

* Clicked "New here? Register Account" anchor - Check
* Log in form validation active - Check
![login.png](/static/images/doc-img/login.png)
* Log in submission functional, user added in session cookie - Check

* Data handling login function:
    * Checks if username exists in database "users" collection.
    * Ensures hashed password matches user input
    * If successful, logs in user into account and alerts "Welcome, {username}" 
    * User information is retrieved from database and displayed in profile.
    * If "Invalid password match" alerts "Incorrect Username and/or Password"
    * If "Username doesn't exist" alerts "Incorrect Username and/or Password"
    * Redirects user to profile page.

* Users collection in database:
![users-collection](/static/images/doc-img/users-collection.png)
* Clicked Logout button - Check
* Logout method fully functional - Check

#### register.html

* Clicked "New here? Register Account" anchor - Check
* Register form validation active - Check
![registered.png](/static/images/doc-img/registered.png)
* Register form submission functional, user added to session cookie - Check
* User added to database.
![user-added.png](/static/images/doc-img/user-added.png) 

* Data handling register function:
    * Checks if username exists in database "users" collection.
    * If username exists in database, alerts "Username already exists"
    * Else, generates password hash from user input.
    * User added to session cookie.
    * Redirects user to profile page.

#### profile.html

* Clicked "EDIT PROFILE" anchor, redirects to edit_profile page - Check
* Clicked "CANCEL" button, redirects to profile - Check
* Edit profile form validation functional - Check
![editprofile-validation.png](/static/images/doc-img/editprofile-validation.png)
* User updated to database - Check
![user-edited.png](/static/images/doc-img/user-edited.png)
* Clicked "DELETE PROFILE" anchor, defensive modal pops up - Check
![delete-popup.png](/static/images/doc-img/delete-popup.png) 
    * Clicked "CANCEL", defensive modal closes - Check
    * Clicked "DELETE", profile deleted from database - Check

* Data handling edit_profile function:
    * Gets user's information from database "users" collection.
    * Populates form values with profile's information.
    * Username has readonly attribute.
    * Updates user new information to database "users" collection. 

#### share.html

* Share new experience form validation functional - Check
![share-validation.png](/static/images/doc-img/share-validation.png) 
* Experience added to database - Check
![xp-added.png](/static/images/doc-img/xp-added.png) 
* Experience card rendered to browse.html, region.html and profile.html - Check
* Clicked "EDIT" anchor, redirects to edit_experience page - Check
* Edit experience form validation functional - Check
![editxp-validation.png](/static/images/doc-img/editxp-validation.png)
* Clicked "READ MORE" anchor, redirected to experience's view_experience.html - Check
* Clicked "DELETE" anchor, defensive modal pops up - Check
![xp-deleted.png](/static/images/doc-img/xp-deleted.png) 
    * Clicked "CANCEL", defensive modal closes - Check
    * Clicked "DELETE", experience deleted from database - Check

### Known Bugs

#### emailJS

* Contact form will submit when filled with whitespaces. Didn't managed to fix it on time for submission.
    
* Jinja iteration generates an id repetition for the defensive modal in "DELETE" anchor for experiences. Didn't managed to fix it on time for submission. Opted instead for removing the modal to be able to validate the html code.
    ![xp-deleted.png](/static/images/doc-img/xp-deleted.png) 

### Code Validation

*  ![Valid HTML!](/static/images/doc-img/valid-html.png) HTML has been validated by [W3C validator](https://validator.w3.org/)

*  ![Valid CSS!](/static/images/doc-img/valid-css.jpg) CSS has been validated by [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

### Responsiveness
The responsiveness of the website has been tested with Chrome Developer Tools and Chrome Responsive Viewer.
* Fully responsive on all tested devices - Check
