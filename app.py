from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def basic():
    if request.method == 'POST':
        width = (int)(request.form['width'])
        height = (int)(request.form['height'])
        color = (str)(request.form['color'])
        format = (str)(request.form['format'])
        
        if color == 'red':
            img_arr = np.ones((width, height, 3)) * np.array([255, 0, 0])
        elif color == 'green':
            img_arr = np.ones((width, height, 3)) * np.array([0, 255, 0])
        elif color == 'blue':
            img_arr = np.ones((width, height, 3)) * np.array([0, 0, 255])
        else:
            return jsonify({'error': 'Invalid color parameter'}), 400
        
        
        if format == 'png':
            img = Image.fromarray(img_arr, mode='RGB')
            # save the image as a png file
            img.save('my_image.png', 'JPEG')

        elif format == 'jpeg':
            img = Image.fromarray(img_arr, mode='RGB')
            # save the image as a JPEG file
            img.save('my_image.jpeg', 'JPEG')
            
        elif format == 'gif':
            img = Image.fromarray(img_arr, mode='RGB')
            # save the image as a GIF file
            img.save("animation.gif", format="GIF", duration=100, loop=0)

        else:
            return jsonify({'error': 'Invalid  Format'}), 400
        
        print(img_arr)
        
        img_str = str(img_arr)
        

        return render_template('index.html', img_arr=img_str,image=img)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    