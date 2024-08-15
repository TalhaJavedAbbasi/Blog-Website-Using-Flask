from flask import Flask,render_template, request
import requests
app = Flask(__name__)
response = requests.get("https://api.npoint.io/6fda88c56d9c919a5b44")
response.raise_for_status()
blogs_data_dict = response.json()


@app.route('/')
def get_index_html():
    return render_template('index.html', blogs_data=blogs_data_dict)


@app.route('/about')
def get_about_html():
    return render_template('about.html')


@app.route('/contact', methods=['GET','POST'])
def get_contact_html():
    if request.method == 'POST':
        return render_template('contact.html', method=request.method)
    else:
        return render_template('contact.html')


def receive_data():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['phone'])
    print(request.form['message'])
    return '<h1>Form submitted successfully😍</h1>'


@app.route('/post/<int:blog_id>')
def get_post_html(blog_id):
    # Find the blog post by id
    blog_post = next((blog for blog in blogs_data_dict if blog["id"] == blog_id), None)
    if blog_post:
        return render_template('post.html', blog_post=blog_post)
    else:
        return "Blog post not found", 404


if __name__ == '__main__':
    app.run(debug=True)
