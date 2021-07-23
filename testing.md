<h1>WILD ARGENTINA</h1>
<h2>Backend Development Milestone Project</h2>

<h1>Testing</h1>


## User Experience (UX)

## User stories testing

### First time visitor

* "As a First Time Visitor, I expect the purpose of the website to be explicit"
   * The user is received with the slider of images, with the first slide showcasing a WILD ARGENTINA banner, and the following the names and picture of the regions.
   * Website's header reads WA.
   * "About WA" section in the home page, where the mission and objectives of the organization are displayed.

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
   * The latest entries are shown on top of the "Browse" page, aswell as for every region in the "Discover" page.

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
* As a Frequent User, I want to check new features.
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

### Navigation

#### base.html

* Clicked each navbar item - Check
* Clicked each navbar item (mobile) - Check
* Clicked header to ensure that it redirects to home page - Check
* Clicked header to ensure that it redirects to home page. (mobile) - Check
* Clicked social media links in footer - Check

#### browse.html

* Clicked "Read More" anchor at individual experiences - Check
* Search bar queries the database for words found in several fields (region_name, experience_name, category_name, location_name, experience_description, by[username]) - Check
* Reset button at search bar resets the displayed images to default behaviour - Check

![browse.jpg](/static/images/doc-img/browse.jpg)

#### discover.html

* Clicked "Discover Experiences" button at individual region - Check

#### view_experiences.html

* Clicked every picture in gallery to ensure they replace the expanded one - Check

![gallery.png](/static/images/doc-img/gallery.png)


### Code Validation

*  [Valid HTML!](/assets/images/valid-html.png) HTML has been validated by [W3C validator](https://validator.w3.org/)
*  ![Valid CSS!](/static/images/valid-css.jpg) CSS has been validated by [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

### Responsiveness
The responsiveness of the website has been tested with Chrome Developer Tools and Chrome Responsive Viewer.
* Fully responsive on all tested devices - Check

### Links
* Clicked all anchor elements. They work as expected on every browser. - Check