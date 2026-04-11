## 🍴 Restaurant Finder App

This application is a restaurant discovery tool built for the Just Eat Takeaway.com Early Careers Program. It interfaces with the official Discovery API to fetch live restaurant data based on a user-provided UK postcode. The project was developed to provide a clean, user-friendly interface that focuses on clear data presentation.

### Build and Run 
1. Clone the Repository:
git clone https://github.com/christinasamara/restaurant-discovery-service-jet

2. Set up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate (Mac/Linux) or venv\Scripts\activate (Windows)

3. Install Dependencies:
pip install flask requests

4. Run the Application:
python app.py

5. View the App:
Open your browser and navigate to http://127.0.0.1:5000

### Technologies Used
* Python & Flask: Chosen as the backend framework for its speed, simplicity and API handling.
* Bootstrap 5: Used for the frontend grid system to ensure the interface is responsive across mobile and desktop devices.
* 
* Jinja2 Templates: Used to dynamically render restaurant cards and handle conditional logic for empty search states or error messages.

### Functionality
* Postcode Search: Users can enter a UK postcode to see a list of local dining options.
* Data Focus: The interface limits the display to the first 10 restaurants returned.
* Filtering: Users can filter results by specific tags like "Deals," "Rating," or specific cuisines.
* Sorting: The interface allows users to sort restaurants by their star rating or the volume of reviews.
* Informative Cards: Each card displays the restaurant's logo, name, cuisine types, numeric rating with review count, and full address.

