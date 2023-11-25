from PIL import Image
import os


def resize_in_dir(indir, outdir):
    target = (384, 384)

    os.makedirs(outdir, exist_ok=True)
    num = len(os.listdir(indir))
    # Loop through each image in the input directory
    for i, filename in enumerate(os.listdir(indir)):
        print(i, '/', num)
        if filename.endswith(".jpg"):
            # Open the image
            image_path = os.path.join(indir, filename)
            img = Image.open(image_path)

            # Resize the image
            img_resized = img.resize(target)

            # Save the resized image to the output directory
            output_path = os.path.join(outdir, filename)
            img_resized.save(output_path)


if __name__ == '__main__':
    resize_in_dir('test/images/', 'testn/images/')
    resize_in_dir('train/images/', 'trainn/images/')
    resize_in_dir('valid/images/', 'validn/images/')