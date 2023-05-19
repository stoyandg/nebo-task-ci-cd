from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
    "https://newsroom.unsw.edu.au/sites/default/files/styles/full_width__2x/public/thumbnails/image/3500028168_c85a03256a_b_2.jpg?itok=LeG6fxCZ",
    "https://petapixel.com/assets/uploads/2022/11/DSC9127_1.jpeg",
    "https://images.all-free-download.com/images/graphiclarge/cat_cats_eyes_cat_face_269574.jpg" 
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=6001)