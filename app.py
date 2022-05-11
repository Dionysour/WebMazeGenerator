from flask import Flask, render_template, request
from Generator import Generator
import sys
import os


app = Flask(__name__)
image_folder = os.path.join('MazeGenerator/maze_images')
app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/', methods=['POST', 'GET'])
def index():
    generator = Generator()
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'maze_image.jpg')
    rad = 20
    cell_size = 10
    wall_width = 5
    gen_algo = 'DFS'
    if request.method == 'POST':
        rad = int(request.form['radius'])
        cell_size = int(request.form['cell_size'])
        wall_width = int(request.form['wall_width'])
        gen_algo = request.form['generator']
        if rad <= 90:
            generator.web_init(rad, cell_size, wall_width, gen_algo)
            generator.dump_maze_image('static/maze.png')
        return render_template('base.html', src=image_path, rad=rad,
                               cell_size=cell_size, wall_width=wall_width,
                               gen=gen_algo)
    else:
        return render_template('base.html', src=image_path, rad=rad,
                               cell_size=cell_size, wall_width=wall_width,
                               gen=gen_algo)


if __name__ == '__main__':
    print('asdddddddddddddddddddddddddddddddddd')
    generator = Generator()
    generator.web_init(20, 10, 5, 'dfs')
    generator.dump_maze_image('static/maze.png')
    app.run(debug=True)
