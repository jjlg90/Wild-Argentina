<h1>Wild Argentina</h1>
<h1>Backend Development Milestone Project</h1>

![responsive-mockup](/static/images/responsive-mockup.png)

This project consists of a website for traveler's community WILD ARGENTINA, where users can browse, discover and share experiences lived in different regions of Argentina. WILD ARGENTINA is all about connection to nature, tradition and Argentina's vast diversity.
Check out the [Live Project](https://wild-argentina.herokuapp.com/index)

#### Disclaimer
WILD ARGENTINA traveler community does not exist. The creation of this project is purely educative. 

## User Experience (UX)

## User stories

### First time visitor
* As a First Time Visitor, I expect the purpose of the website to be explicit.
* As a First Time Visitor, I consider smooth navigation through content to be a key aspect.
* As a First Time Visitor, I want the content of the website to be relevant and concise. 
* As a First Time Visitor, I would like to browse places, foods and experiences.

### Returning visitor
* As a Returning Visitor, I expect to see new entries and updates.
* As a Returning Visitor, I want to be able to share my own experiences.
* As a Returning Visitor, I would like to check activity on social media platforms.
* As a Returning Visitor, I want to check each experience geographic location.


### Frequent user
* As a Frequent User, I would like to interact with other members of the community.
* As a Frequent User, I want to have access to new features.
* As a Frequent User, I expect to have control over my information.
* As a Frequent User, I want to be able to get the exact location for each experience.
* As a Frequent User, I would like to have the possibility of saving experiences for quick access.
* As a Frequent User, I want to be able to easily share experiences.

 
 ### Strategy

 #### Project Goals 
 To provide WILD ARGENTINA with a presentation website, where its users can can browse, discover and share experiences.
 
 #### Developer Goals: 
 To showcase an attractive, well-designed flask based python application that's easily updated and maintained.

### Scope 

#### Features
* The project is presented in a multipage layout, based on flask and controlled by python to communicate to a backend database served by MongoDB.
Rendered templates customized with HTML5, CSS3, Javascript and Jinja.
* Fully responsive on different screen sizes.
* It counts with a contact form inside a modal pop-up.
* Full CRUD functionality. (Create, Read, Update and Delete experiences and profiles)

#### Future Features
* User's travel journal. For those users who would like to read about someone else's adventures.
* Trip maker functionality, where users will be able to make a schedule of activities.
* Experience's comment section.
* Pagination for experiences.
* Expanded information area for each region, with relevant media and links.
* Awareness section. Where users can be informed on how to preserve the enviroments visited, and how to help the local communities.
* Aesthetic animations.

### Structure 

#### Information
 The content is distributed throughout several pages.

* Main page:
    * Image slider showcasing organization's header and the different regions to discover.
    * Navigation section, where the user can choose to Browse, Discover or Share experiences.
    * About WA section, where the mission and objectives of the organization are made known to the user.

* Discover:
    * List of regions, alongside with images and description, for the user to choose one and have access to all experiences in each one.

* Browse:
    * Search bar to query the experience collection in the database.
    * Experiences section, where all latest experiences are displayed in big clickable cards.
 
* Experience:
    * When an experience is selected, the user will be redirected to the experience page, where pictures, information, upload date and exact geographical location is displayed.

### Skeleton
For the wireframes, Figma software has been used to lay out the foundations of the website.

![Wireframes](/static/images/wireframes.jpg)

### Surface
 The content is easy to navigate and is neatly divided in sections.

 The colour palette is dark, looking to highlight the brightness of the images to attract attention to them. 

* Blue and Grey for backgrounds
    * #263238
    * #607d8b 
    * #546e7a 
    * #455a64 
    * #37474f 
    * #424242
    * #212121

* White and Yellow for fonts
    * #fafafa
    * #faff00 

* Red and Green for buttons
    * #f44336
    * #4caf50


The fonts are:
* Montserrat. Bold and with a strong connection to the content. "The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires 
  inspired Julieta Ulanovsky to design this typeface and rescue the beauty of urban typography that emerged in the first half of the twentieth century."
* Lora. In order to provide a nice contrast with the headers, with its brushed curves and roots in calligraphy, Lora is a well-balanced contemporary serif.


## Technologies

### Languages

-  [HTML5](https://en.wikipedia.org/wiki/HTML5)
-  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-  [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies

* [Jinja 3.0.1](https://en.wikipedia.org/wiki/Jinja_(template_engine)) 
    * Template engine for python.
* [Flask 2.0.1](https://en.wikipedia.org/wiki/Flask_(web_framework)) 
    * Web framework for python.
* [MaterializeCSS 1.0.0](https://materializecss.com/) 
    * Responsive design and css styling.
* [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
    * Document oriented database.
* [Heroku](https://en.wikipedia.org/wiki/Heroku)
    * Cloud platform service.
* [Jquery CDN](https://code.jquery.com)
    * Javascript.
* [W3Schools](https://www.w3schools.com/)
    * CSS documentation.
* [Figma:](https://figma.com/)
    - Figma was used to create the wireframes.
* [GitHub:](https://github.com/)
    * Code repository.
* [Gitpod](https://gitpod.io/)
    * Gitpod was used as IDE and for version control. 
* [Font Awesome:](https://fontawesome.com/)
    * Font Awesome was used solely for social media icons in footer.
* [Google Fonts:](https://fonts.google.com/)
    * Google fonts was used to import "Montserrat" and "Lora" family fonts.
* [Chrome Developer Tools:](https://developers.google.com/web/tools/chrome-devtools)
    * Used to debug and style.
* [EmailJS:](https://www.emailjs.com/)
    * Provided backend email service to contact form.
* [Google Maps JavaScript API:](https://developers.google.com/maps)
    * Provided backend map service.

## Testing

__[Click here to read testing documentation.](testing.md)__

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jjlg90/Wild-Argentina)
2. At the top of the Repository, just above the "Settings" button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jjlg90/Wild-Argentina)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/jjlg90/Wild-Argentina
```

7. Press Enter. Your local clone will be created.

### Connecting to MongoDB
1. Log in to MongoDB.
2. Within the "Cluster1" tab selected, click on "Connect".
3. Select "Connect your application".
4. Select _Python_ version 3.6 or later.
5. Copy _connection string_ and then paste it to env.py
6. Create an instance of PyMongo and pass the application to that instance.
* Like:  `mongo = PyMongo(app`)

### Heroku Deployment

Preparing Local workspace for Heroku:
1. Create *__requirements.txt__*  file.
CLI: `pip freeze --local > requirements.txt`

2. Creating *__Procfile__* file.
Type in file `web: python app.py` and save.

Create Heroku application:
1. Log in Heroku.
2. Click `New` button. 
2. Select `Create a new app`.
3. Enter the app name.
4. Select region.
5. Under `Settings`, __click__ `Config Vars` to add Configuration Variables from the env.py file.
6. In your CLI install Heroku by typing `npm install -g heroku`  
7. Select `Deploy` option.
8. Under `Deployment method` select the __GitHub__ option.
9. Select Automatic deploys from the main branch and select `Deploy Branch`.
10. Click `Open App` button located in the top-right corner of your Heroku account.

## Credits

#### Media
Pictures and videos were taken from the following websites.

### Acknowledgements

* My Mentor Oluwafemi Medale who guided me through development.
* [Stack Overflow](https://stackoverflow.com/) helped me to find answers about structure and styling from other people's inquiries, posts and threads.