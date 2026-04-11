from flask import Flask, render_template, request
from data_loader import load_data

app = Flask(__name__)

@app.route('/')
def index():
    postcode = request.args.get('postcode', 'L40TH').strip()
    sort_by = request.args.get('sort', '')
    min_rating = request.args.get('min_rating', type=float)
    selected_tags = request.args.getlist('search')

    all_restaurants = load_data(postcode)

    available_tags = set()
    for res in all_restaurants:
        tags = [t.strip() for t in res.get('cuisines', '').split(',')]
        available_tags.update(tags)
    
    filter_options = sorted(list(available_tags))
    
    if selected_tags:
        restaurants = [
            r for r in all_restaurants 
            if any(tag.lower() in r.get('cuisines', '').lower() for tag in selected_tags)
        ]
    else:
        restaurants = all_restaurants

    if min_rating:
        restaurants = [r for r in restaurants if r.get('rating') and r.get('rating') >= min_rating]

    if sort_by == 'rating_desc':
        restaurants = sorted(restaurants, key=lambda x: x.get('rating') or 0, reverse=True)
    elif sort_by == 'name_asc':
        restaurants = sorted(restaurants, key=lambda x: x.get('name', '').lower())

    return render_template('index.html', restaurants=restaurants, postcode=postcode, filter_options=filter_options)

if __name__ == "__main__":
    app.run(debug=True)